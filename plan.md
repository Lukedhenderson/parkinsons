## plan 
### Introduction

- State the question: How well can we predict the motor and total UPDRS scores (‘motor_UPDRS’ and ‘total_UPDRS’) from the 16 voice measures in this dataset? WE need to decide if we are going to predict motor and total or pick one and justify why.
- Describe the dataset and all featers
- Define what sucess is and our goal

### Data Exploration & Preprocessing — 40 points

- **Cleaning (10 pts):** Check missing values, duplicates, numeric types, invalid values, and outliers. Document all checks and write significance and purpose of each.
- **Exploration (10 pts):** Show target distributions, recordings per patient, feature distributions, a correlation heatmap, and selected feature–target plots. Look for skew, redundant measurements, and differences between patients. Use training data for decisions that affect modeling.
- **Feature engineering (20 pts):** Compare the original features against a few justified alternatives: log-transform skewed voice measurements, remove highly redundant features, and try selected squared terms or interactions for nonlinear regression. Compare voice-only features against voice plus age, sex, and recording time. Standardize inputs for scale-sensitive models such as KNN and SVR.
- **Prevent leakage:** Split by `subject#` so a patient never appears in both training and testing. Keep the ID only for grouping, exclude both UPDRS columns from predictors, and fit preprocessing and feature selection inside training folds.

**Key accomplishment:** Demonstrate whether feature changes improve validation performance.

### Modeling — 40 points

- Establish a baseline that always predicts the training-set mean.
- Compare class-related methods using their **regression versions**: linear regression, KNN, decision tree, random forest, and support vector regression.
- Use the same patient-grouped cross-validation folds for fair comparisons.
- Tune meaningful parameters: neighbor count, tree depth/minimum leaf size, forest settings, and SVR's `C`, `epsilon`, and kernel settings.
- Use **MAE as the primary metric**, supported by RMSE and R². Compare training and validation performance to identify overfitting.
- Use scikit-learn pipelines and record untuned versus tuned results.

**Optional extension:** Use K-means or DBSCAN to explore voice patterns or unusual recordings. These can add depth if cleaning is minimal, but prioritize the regression comparison.

### Results & Analysis — 10 points

- Select the final approach using cross-validation, then evaluate it once on the untouched patient-held-out test set.
- Present a compact comparison table with baseline, model, feature set, tuning, and performance. Distinguish cross-validation results from final test results.
- Include predicted-versus-actual and residual plots.
- Examine errors by patient and severity range; explain where predictions struggle.
- Summarize which features and tuning choices helped, and acknowledge that thousands of recordings still represent only 42 patients.

### Quality & Submission — remaining 10 points

- Organize the notebook into the four sections above, with short explanations, labeled plots, reproducible settings, and a successful top-to-bottom run.
- Use established ML libraries rather than implementing algorithms from scratch.
- Submit the notebook and team-written process PDF (**maximum five pages; AI writing prohibited**) by **November 19, 2026, at midnight**. Slip days cannot be used.
- In the process writeup, explain the team's methodology and decisions and include each member's contributions at the end.
- Prepare everyone to explain the code, decisions, and results at the **December 1, 2026, Q&A**.
