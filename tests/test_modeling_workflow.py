"""Regression checks for patient leakage and the voice transformation."""
import unittest
import numpy as np
from modeling_workflow import candidate_specs, load_split
from sklearn.model_selection import GroupKFold


class ModelingChecks(unittest.TestCase):
    def test_patients_never_cross_evaluation_boundaries(self):
        X, X_test, y, _, patients, test_patients = load_split()
        self.assertTrue(set(patients).isdisjoint(test_patients))
        self.assertFalse({'subject#', 'motor_UPDRS', 'total_UPDRS'} & set(X.columns))
        self.assertListEqual(list(X.columns), list(X_test.columns))
        for train, valid in GroupKFold(5).split(X, y, patients):
            self.assertTrue(set(patients.iloc[train]).isdisjoint(patients.iloc[valid]))
            for inner_train, inner_valid in GroupKFold(3).split(
                    X.iloc[train], y.iloc[train], patients.iloc[train]):
                self.assertTrue(set(patients.iloc[train].iloc[inner_train]).isdisjoint(
                    patients.iloc[train].iloc[inner_valid]))

    def test_log_pipeline_actually_transforms_voice(self):
        X, *_ = load_split()
        pipe, _ = candidate_specs(X.columns)['Lasso / Log voice + demographics']
        # ColumnTransformer must preserve names so the following step recognizes voice features.
        selected = pipe.named_steps['select'].fit_transform(X)
        transformed = pipe.named_steps['log'].fit_transform(selected)
        for col in ['NHR', 'Jitter(%)', 'Shimmer']:
            np.testing.assert_allclose(transformed[col], np.log(X[col]))
        np.testing.assert_array_equal(transformed.age, X.age)
        np.testing.assert_array_equal(selected.NHR, X.NHR)


if __name__ == '__main__':
    unittest.main()
