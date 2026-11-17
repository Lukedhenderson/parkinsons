"""Patient-held-out regression experiments shared by both project notebooks."""
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score
from sklearn.model_selection import GroupKFold, GroupShuffleSplit, GridSearchCV
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, StandardScaler, PolynomialFeatures
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor

SEED = 42
SCORING = {'MAE': 'neg_mean_absolute_error', 'RMSE': 'neg_root_mean_squared_error', 'R2': 'r2'}


def load_split(path='data/parkinsons_updrs.csv'):
    df = pd.read_csv(path)
    if df.isna().any().any() or not np.isfinite(df.to_numpy()).all():
        raise ValueError('Missing or nonfinite input values require investigation.')
    X = df.drop(columns=['subject#', 'motor_UPDRS', 'total_UPDRS'])
    y, groups = df.total_UPDRS, df['subject#']
    a, b = next(GroupShuffleSplit(n_splits=1, test_size=.2, random_state=SEED).split(X, y, groups))
    assert set(groups.iloc[a]).isdisjoint(groups.iloc[b])
    return X.iloc[a], X.iloc[b], y.iloc[a], y.iloc[b], groups.iloc[a], groups.iloc[b]


def log_voice(X):
    """Stateless log of strictly positive jitter, shimmer and NHR measurements."""
    X = X.copy()
    cols = [c for c in X if c.startswith(('Jitter', 'Shimmer')) or c == 'NHR']
    if (X[cols] <= 0).any().any():
        raise ValueError('Voice log transform requires positive measurements.')
    X[cols] = np.log(X[cols])
    return X


def candidate_specs(columns):
    voice = [c for c in columns if c not in ['age', 'sex', 'test_time']]
    # Fixed, justified alternatives avoid selecting features using validation targets.
    representations = {
        'Demographics': (['age', 'sex', 'test_time'], False),
        'Voice only': (voice, False),
        'Voice + demographics': (list(columns), False),
        'Log voice + demographics': (list(columns), True),
    }
    models = {
        'Linear': (LinearRegression(), {}),
        'Ridge': (Ridge(), {'model__alpha': [10, 1000]}),
        'Lasso': (Lasso(max_iter=20000), {'model__alpha': [.1, 1]}),
        'KNN': (KNeighborsRegressor(), {'model__n_neighbors': [50, 400]}),
        'Tree': (DecisionTreeRegressor(random_state=SEED), {'model__max_depth': [2, 5], 'model__min_samples_leaf': [100]}),
        'SVR': (SVR(), {'model__C': [1, 10], 'model__epsilon': [1]}),
        'Forest': (RandomForestRegressor(n_estimators=80, min_samples_leaf=50, random_state=SEED, n_jobs=1), {'model__max_depth': [3, None]}),
    }
    specs = {'Mean baseline': (Pipeline([('model', DummyRegressor())]), {})}
    for feature_name, (cols, use_log) in representations.items():
        for model_name, (model, grid) in models.items():
            pipe = Pipeline([
                ('select', ColumnTransformer([('columns', 'passthrough', cols)], remainder='drop', verbose_feature_names_out=False).set_output(transform='pandas')),
                ('log', FunctionTransformer(log_voice) if use_log else 'passthrough'),
                ('scale', StandardScaler()), ('model', model),
            ])
            specs[f'{model_name} / {feature_name}'] = pipe, grid
    # A small regularized nonlinear expansion tests interactions without a large search.
    specs['Quadratic Ridge / Log voice + demographics'] = (Pipeline([
        ('log', FunctionTransformer(log_voice)), ('scale', StandardScaler()),
        ('quadratic', PolynomialFeatures(degree=2, include_bias=False)),
        ('rescale', StandardScaler()), ('model', Ridge()),
    ]), {'model__alpha': [1000, 10000]})
    return specs


def compare_models(X, y, groups):
    """Tune in inner grouped folds; report identical outer grouped folds for all models."""
    outer = list(GroupKFold(n_splits=5).split(X, y, groups))
    for a, b in outer:
        assert set(groups.iloc[a]).isdisjoint(groups.iloc[b])
    specs, rows = candidate_specs(X.columns), []
    for name, (pipe, grid) in specs.items():
        # Materialize inner splits relative to each outer training subset: no patient leakage.
        fold_scores, default_scores = [], []
        for a, b in outer:
            inner = list(GroupKFold(n_splits=3).split(X.iloc[a], y.iloc[a], groups.iloc[a]))
            search = GridSearchCV(pipe, grid, scoring='neg_mean_absolute_error', cv=inner, n_jobs=1, error_score='raise')
            search.fit(X.iloc[a], y.iloc[a])
            pred = search.predict(X.iloc[b])
            default = pipe.fit(X.iloc[a], y.iloc[a]).predict(X.iloc[b])
            fold_scores.append((mean_absolute_error(y.iloc[a], search.predict(X.iloc[a])),
                                mean_absolute_error(y.iloc[b], pred),
                                root_mean_squared_error(y.iloc[b], pred), r2_score(y.iloc[b], pred)))
            default_scores.append(mean_absolute_error(y.iloc[b], default))
        scores = np.array(fold_scores)
        rows.append({'candidate': name, 'train MAE': scores[:, 0].mean(),
                     'untuned CV MAE': np.mean(default_scores), 'CV MAE': scores[:, 1].mean(),
                     'CV MAE SD': scores[:, 1].std(ddof=1), 'CV RMSE': scores[:, 2].mean(),
                     'CV R2': scores[:, 3].mean()})
        print(f'{name}: nested CV MAE {scores[:, 1].mean():.3f}', flush=True)
    comparison = pd.DataFrame(rows).sort_values('CV MAE').reset_index(drop=True)
    baseline = comparison.loc[comparison.candidate == 'Mean baseline', 'CV MAE'].iloc[0]
    comparison['MAE improvement %'] = 100 * (1 - comparison['CV MAE'] / baseline)
    comparison['MAE tuning gain'] = comparison['untuned CV MAE'] - comparison['CV MAE']
    return comparison, specs


def final_evaluation(comparison, specs, X_train, X_test, y_train, y_test, groups_train, groups_test):
    """Select solely by outer CV MAE; use test labels only for the final report."""
    assert set(groups_train).isdisjoint(groups_test)
    winner = comparison.iloc[0]['candidate']
    pipe, grid = specs[winner]
    folds = list(GroupKFold(n_splits=3).split(X_train, y_train, groups_train))
    search = GridSearchCV(pipe, grid, cv=folds, scoring='neg_mean_absolute_error', error_score='raise')
    search.fit(X_train, y_train)
    prediction = search.predict(X_test)
    baseline = np.full(len(y_test), y_train.mean())
    report = pd.DataFrame([
        {'model': name, 'test MAE': mean_absolute_error(y_test, pred),
         'test RMSE': root_mean_squared_error(y_test, pred), 'test R2': r2_score(y_test, pred)}
        for name, pred in [(winner, prediction), ('Mean baseline', baseline)]
    ])
    errors = pd.DataFrame({'patient': groups_test, 'actual': y_test, 'predicted': prediction})
    errors['residual'] = errors.actual - errors.predicted
    errors['absolute error'] = errors.residual.abs()
    return search, report, errors
