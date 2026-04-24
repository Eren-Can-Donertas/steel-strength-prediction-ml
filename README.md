

# AI Mini Project: Prediction of Ultimate Tensile Strength (UTS) of Steel Using Linear Regression

## Course Information
**Course:** MAK 307 – Design, Production and Artificial Intelligence Applications  
**Project Type:** Introductory AI Mini Project  
**Department:** Mechanical Engineering  

---
## Group Members
- Eren Can Dönertaş

## 1. Introduction

This project was prepared as a simple Artificial Intelligence application for a mechanical engineering problem. The main purpose of the study is not to build the most advanced machine learning system, but to understand and demonstrate the complete workflow of an AI-based engineering project.

In this study, we selected steel property datasets and used a basic regression model to predict **Ultimate Tensile Strength (UTS)**. The project includes the essential stages of a beginner-level AI pipeline:

- reading data,
- understanding the dataset,
- preprocessing the data,
- selecting features and target,
- training a model,
- making predictions,
- evaluating the model,
- saving outputs,
- and interpreting the results.

So even if the final predictive performance is not very strong, the project is still meaningful because it demonstrates the full engineering AI workflow clearly.

---

## 2. Problem Definition

In mechanical engineering, **Ultimate Tensile Strength (UTS)** is one of the most important mechanical properties of a material. It represents the maximum stress that a material can withstand before fracture under tensile loading.

In this project, the goal is to predict:

- **Target variable:** `UTS (MPa)`

using available material-related input variables such as:

- steel grade,
- condition,
- chemical composition ranges,
- and some additional alloy element values.

This problem is relevant because predicting material strength from composition and material conditions can support preliminary engineering analysis, material selection, and design decisions.

---

## 3. Datasets Used

Two datasets were used in this project:

1. **Carbon Steel Dataset**
2. **Stainless Steel Dataset**

Both datasets contain a target column called:

- `UTS (MPa)`

The input features were selected from the available material-related columns, such as:

- `SAE Grade`
- `Conditions`
- `C (Min)`, `C (Max)`
- `Mn (Min)`, `Mn (Max)`
- `P (Min)`, `P (Max)`
- `S (Min)`, `S(Max)`
- `Si (Min)`, `Si (Max)`
- `Ni (Min)`, `Ni (Max)`
- `Cr (Min)`, `Cr (Max)`
- `Mo (Min)`, `Mo (Max)`
- `Ti (Min)`, `Ti (Max)`
- `N` (if present)

The idea was to use tabular engineering data that is understandable and suitable for a simple prediction task.

---

## 4. Project Folder Structure

The project is organized as follows:

```text
AI_Project_Group_1/
├── data/
│   ├── steel_property_and_composition_data.csv
│   └── steel_property_and_composition_stainless_steel.csv
├── results/
│   ├── carbon_steel/
│   │   ├── predictions.csv
│   │   └── predicted_vs_actual.png
│   └── stainless_steel/
│       ├── predictions.csv
│       └── predicted_vs_actual.png
├── src/
│   ├── main.py
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   └── metrics_helper.py
└── requirements.txt
```

This structure makes the project easier to run, understand, and maintain.

---

## 5. Libraries Used

The project uses the following Python libraries:

- `pandas`
- `numpy`
- `matplotlib`
- `scikit-learn`

### Why these libraries were used
- **pandas** was used for reading and processing CSV files.
- **numpy** was used for numerical operations.
- **matplotlib** was used for plotting actual vs predicted values.
- **scikit-learn** was used for train-test split, linear regression, and evaluation metrics.

---

## 6. Installation

Before running the project, the required libraries must be installed.

### Option 1: Using requirements.txt
```bash
pip install -r requirements.txt
```

### Option 2: Direct installation
```bash
pip install pandas numpy matplotlib scikit-learn
```

If `pip` does not work directly, the following can also be used:

```bash
python -m pip install pandas numpy matplotlib scikit-learn
```

---

## 7. How to Run the Project

Run the project from the root directory using:

```bash
python src/main.py
```

### What happens when this command runs
When the project is executed:

1. the carbon steel dataset is loaded,
2. preprocessing is applied,
3. the model is trained,
4. predictions are generated,
5. evaluation metrics are printed,
6. results are saved to the `results/carbon_steel/` folder.

Then the same workflow is repeated for:

- the stainless steel dataset.

So with one command, both datasets are processed and analyzed.

---

## 8. How the Code Works

This project is divided into several Python files. Each file has a clear role.

### 8.1 `main.py`
This is the main file that controls the entire project.

It:
- defines dataset paths,
- loops through both datasets,
- calls preprocessing,
- calls model training,
- generates predictions,
- evaluates results,
- saves outputs.

In short, `main.py` manages the complete pipeline.

---

### 8.2 `preprocess.py`
This file prepares the raw data before model training.

It performs the following operations:

- reads the CSV file,
- strips extra spaces from column names,
- renames inconsistent columns if needed,
- converts text-like numeric values to real numeric values,
- replaces invalid values such as `-`, empty strings, and missing text values with `NaN`,
- removes rows where the target value `UTS (MPa)` is missing,
- selects useful feature columns,
- removes completely empty columns,
- fills missing numeric values,
- fills missing categorical values,
- converts categorical variables into numerical format using one-hot encoding.

### Why preprocessing was necessary
The raw datasets were not ready for direct machine learning use. Some values were missing, some values were stored as text, and some columns were categorical. Since Linear Regression only works with numerical input and does not accept missing values directly, preprocessing was essential.

Without preprocessing:
- the model would fail,
- missing values would cause errors,
- categorical columns could not be used,
- and the data would not be consistent.

So preprocessing is one of the most important parts of the project.

---

### 8.3 `train.py`
This file handles model training.

It:
- splits the dataset into training and test sets,
- creates a `LinearRegression()` model,
- fits the model using the training data,
- returns the trained model and the test data.

### Why train-test split was used
Train-test split is important because a model should not be evaluated on the same data it learned from. The model is trained on one part of the data and tested on another part. This gives a more realistic idea of how well the model performs on unseen samples.

---

### 8.4 `metrics_helper.py`
This file calculates the evaluation metrics:

- **MAE**
- **MSE**
- **RMSE**
- **R²**

It also prints them neatly.

### What these metrics mean
- **MAE (Mean Absolute Error):** average absolute prediction error
- **MSE (Mean Squared Error):** squared average error
- **RMSE (Root Mean Squared Error):** square root of MSE, easier to interpret in the same unit as the target
- **R² (Coefficient of Determination):** shows how well the model explains the variation in the data

---

### 8.5 `evaluate.py`
This file is responsible for output generation.

It:
- evaluates the model predictions,
- saves a CSV file with actual and predicted values,
- creates a scatter plot of actual vs predicted values,
- saves the plot to the results folder.

### Why this file is useful
It helps transform raw model predictions into understandable outputs for the report and presentation.

---

## 9. Machine Learning Method

The model used in this project is:

- **Linear Regression**

### Why Linear Regression was chosen
Linear Regression was selected because:
- it is simple,
- easy to explain,
- suitable for a beginner-level AI project,
- and appropriate for demonstrating the full machine learning workflow.

This project intentionally avoids overly advanced methods because the goal is to learn the process first.

---

## 10. Outputs Produced by the Project

After the code runs, two types of outputs are generated for each dataset:

### 10.1 `predictions.csv`
This file contains:
- actual UTS values
- predicted UTS values

This helps compare the model output numerically.

### 10.2 `predicted_vs_actual.png`
This scatter plot shows:
- **x-axis:** actual UTS
- **y-axis:** predicted UTS

If the model performs very well, the points should be close to the ideal diagonal trend where:

**predicted = actual**

If the points are far from that trend, the model performance is weaker.

---

## 11. Results Obtained

### Carbon Steel Results
- **MAE:** 107.5967
- **MSE:** 58969.5122
- **RMSE:** 242.8364
- **R²:** -0.8399

### Stainless Steel Results
- **MAE:** 149.7434
- **MSE:** 30716.0498
- **RMSE:** 175.2599
- **R²:** -0.2191

---

## 12. Interpretation of the Results

The code worked successfully from start to finish. It loaded the datasets, cleaned the data, trained the model, made predictions, calculated metrics, and saved results and plots.

So from a workflow perspective, the project was successful.

However, the prediction quality was not very strong.

### Important observation
Both datasets produced **negative R² values**.

This means:
- the model did not explain the data well,
- and its predictions were worse than a simple baseline that predicts around the average target value.

So the project is technically successful, but the predictive performance is limited.

---

## 13. Why the Model Did Not Give Very Good Results

This is one of the most important parts of the project. The model ran correctly, but the final performance was weak. There are several reasons for this.

### 13.1 Small dataset size
The datasets, especially the stainless steel dataset, are relatively small. Machine learning models usually perform better when they are trained on larger and more varied datasets.

With a small dataset:
- the model cannot learn enough patterns,
- the predictions become unstable,
- and unusual samples affect the model more strongly.

---

### 13.2 Limited engineering information
UTS does not depend only on a few chemical composition columns. In real mechanical engineering applications, tensile strength can also depend on:

- heat treatment,
- microstructure,
- manufacturing route,
- cooling conditions,
- previous processing history,
- rolling condition,
- and testing conditions.

If these variables are missing or incomplete, the model cannot fully understand the physical behavior of the material.

---

### 13.3 The relationship may not be purely linear
Linear Regression assumes that the relationship between inputs and output is approximately linear.

But material behavior is often more complex than that.

For example:
- increasing an alloying element may not affect UTS in a purely straight-line way,
- the effect of one variable may depend on another,
- and some mechanical behavior may be nonlinear.

Because of this, Linear Regression may be too simple for this problem.

---

### 13.4 Missing values and imperfect data quality
The raw datasets included:
- missing values,
- inconsistent formatting,
- and columns that were partly empty.

Even though preprocessing fixed many of these issues, some information may still have been lost. Data quality directly affects model quality.

---

### 13.5 Outliers
From the scatter plots, some points appear far away from the overall trend.

These points may represent:
- unusual materials,
- rare conditions,
- extreme samples,
- or noisy data.

Outliers can significantly disturb Linear Regression because the model tries to fit all points with a single linear relationship.

---

### 13.6 Limited feature engineering
In this project, the selected features were mostly direct columns from the dataset. We did not create deeper engineered features such as:
- averages of composition ranges,
- total alloying content,
- grouped metallurgical indicators,
- or process-based combined variables.

So the model may have been missing more meaningful input patterns.

---

### 13.7 Carbon steel and stainless steel are different material families
These two datasets represent different material groups. Their behavior patterns are not identical.

That means:
- a simple approach may work differently on each dataset,
- and the same type of regression model may not be equally suitable for both.

---

## 14. What the Scatter Plots Show

The scatter plots are useful because they visually show model quality.

### If the model were strong:
- the points would cluster around the diagonal,
- actual and predicted values would be close,
- and large errors would be rare.

### What we actually see:
- some points roughly follow the expected trend,
- but many points are noticeably far from the ideal line,
- and some samples have very large prediction errors.

This visual evidence matches the low and negative R² scores.

So the plots confirm that the current model is not strong enough to predict UTS reliably.

---

## 15. Why the Project Is Still Acceptable

Even though the model performance is weak, the project is still valid and acceptable for this course because the goal of the assignment is not to build an advanced industrial system.

This project still demonstrates all the important stages of a basic AI application:

- selecting a dataset,
- understanding the engineering problem,
- preprocessing the data,
- defining features and target,
- training a simple model,
- making predictions,
- evaluating the results,
- plotting the outputs,
- and interpreting limitations.

So the educational objective was achieved.

In other words:
- **the model is not very accurate,**
- but **the project is still successful as a beginner AI workflow demonstration**.

---

## 16. What Could Have Been Done for Better Results

If the goal were higher accuracy rather than simplicity, several improvements could be tried.

### 16.1 StandardScaler
Scaling the input features could help because numerical variables in the dataset may have different value ranges.

A possible improvement would be:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

Then `X_scaled` could be used for training instead of raw `X`.

---

### 16.2 Better feature selection
Some columns may not contribute much to prediction. Others may be more important.

For example, we could:
- keep only the most meaningful alloying elements,
- remove very weak columns,
- group similar features,
- or test different subsets of variables.

---

### 16.3 Better missing-value handling
Instead of only median/mode filling, we could try:
- more careful imputation,
- dropping low-quality rows,
- or using domain knowledge to fill some values.

---

### 16.4 Outlier analysis
Some extreme points may be harming model performance.

Possible improvement:
- detect outliers,
- inspect whether they are real or noisy,
- remove only suspicious ones if justified.

---

### 16.5 More data
This is probably one of the strongest improvements.

With more data:
- the model could learn more patterns,
- performance would likely be more stable,
- and unusual samples would have less negative effect.

---

### 16.6 Better feature engineering
Instead of using only the raw columns, we could create more meaningful features.

Examples:
- average composition values from min/max pairs,
- total alloy content,
- process-condition grouped indicators,
- simplified metallurgical categories.

---

### 16.7 More advanced regression models
If complexity were allowed, better performance might be achieved with models such as:
- Polynomial Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

However, for this project we intentionally kept the method simple.

---

## 17. What Worked Well in This Project

Even though the results were not very accurate, several parts of the project worked well.

### 17.1 The code runs successfully
This is important. The project now runs without crashing and processes both datasets automatically.

### 17.2 The pipeline is complete
The project includes every main AI step:
- input data,
- preprocessing,
- training,
- prediction,
- evaluation,
- visualization,
- saving results.

### 17.3 The outputs are saved properly
For each dataset, the project saves:
- prediction CSV files,
- scatter plots,
- and printed metric results.

This makes the project easy to report and present.

### 17.4 The code structure is clean
Instead of writing everything in one long file, the code is separated into:
- preprocessing,
- training,
- evaluation,
- metrics,
- and main execution.

This is better for readability and project organization.

### 17.5 The project is understandable
The logic is simple enough for a beginner project and easy to explain in class or in a report.

---

## 18. Limitations of the Study

This project has several limitations:

- small dataset size,
- incomplete engineering variables,
- missing values in raw data,
- possible outliers,
- limited feature engineering,
- simple model choice,
- no model comparison,
- no hyperparameter tuning,
- no cross-validation.

Because of these limitations, the project should be interpreted as an **educational prototype**, not as a production-level predictive system.

---

## 19. How to Reproduce the Results

To reproduce the project on another computer:

### Step 1: Put the CSV files inside the `data/` folder
Required files:
- `steel_property_and_composition_data.csv`
- `steel_property_and_composition_stainless_steel.csv`

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the main file
```bash
python src/main.py
```

### Step 4: Check the results
After running, open:

- `results/carbon_steel/predictions.csv`
- `results/carbon_steel/predicted_vs_actual.png`
- `results/stainless_steel/predictions.csv`
- `results/stainless_steel/predicted_vs_actual.png`

---

## 20. Example Summary for Report or Presentation

This project applied a simple Linear Regression model to predict Ultimate Tensile Strength (UTS) of carbon steel and stainless steel materials using tabular engineering data. The project successfully completed the full AI workflow, including preprocessing, training, prediction, evaluation, and visualization. Although the model ran correctly and produced all expected outputs, the final predictive performance was limited. Negative R² values showed that the linear model could not capture the relationship strongly enough. The likely reasons include small dataset size, missing variables, outliers, and the complex nonlinear nature of material behavior. In future work, scaling, better feature engineering, more data, and more advanced regression methods could improve the results.

---

## 21. Final Conclusion

This project successfully demonstrates how Artificial Intelligence can be applied to a simple mechanical engineering problem using Python.

The most important success of the project is that it clearly shows the full process of:
- using an engineering dataset,
- preparing it for machine learning,
- training a regression model,
- generating predictions,
- evaluating the results,
- and interpreting model limitations honestly.

Even though the final accuracy was not strong, the project still achieved its main purpose as an introductory AI study. It shows both:
- **what works,**
- and **why simple models may fail on real engineering data.**

That makes the project educationally valuable and realistic.

---
