# Breast Cancer ML Optimization Analysis

## Project Overview

This project studies machine learning approaches for classifying tumors as malignant or benign using the Breast Cancer Wisconsin Diagnostic dataset.

The goal of the project was to build a baseline model and then improve its performance using feature engineering model selection and hyperparameter tuning.

## Dataset

The dataset includes 569 samples and 30 numerical features describing tumor characteristics.

Target variable

1 = Malignant
0 = Benign

Two columns were removed during preprocessing because they were not useful for modeling

id
Unnamed

Malignant tumors are cancerous. They grow aggressively and may spread to other parts of the body.

Benign tumors are non cancerous. They grow slowly and usually remain localized.

## Methodology

The workflow followed these steps

1 Data preprocessing  
2 Exploratory data analysis  
3 Baseline model training  
4 Feature engineering using VIF  
5 Training ensemble models  
6 Hyperparameter tuning  
7 Model evaluation and comparison .

## Model Improvements

### Baseline Model

The first model used Logistic Regression with feature scaling implemented through a pipeline.

Evaluation used 5 fold cross validation.

**Baseline Accuracy**

0.9736

---

### Feature Engineering using VIF

The correlation heatmap showed strong relationships between features such as radius perimeter and area which indicated multicollinearity.

Variance Inflation Factor VIF was used to detect and remove highly correlated features.

Features with VIF greater than 10 were removed step by step and the model was trained again.

**Accuracy after VIF filtering**

0.9701

### Random Forest Model

A Random Forest classifier was trained to capture non linear relationships between features.

**Accuracy**

0.9614

---

### Hyperparameter Tuning

Random Forest was tuned using GridSearchCV with 5 fold cross validation.

**Parameters tuned**

n_estimators  
max_depth  
min_samples_split  

The tuned model achieved the same performance.

**Accuracy**

0.9614
---

### Model Comparison

| Model | Accuracy |
|------|------|
| Logistic Regression (Baseline CV) | **0.9736** |
| Logistic Regression (After VIF) | 0.9701 |
| Random Forest | 0.9614 |
| Random Forest Tuned | 0.9614 |


## Feature Importance

Random Forest feature importance analysis shows that features related to tumor size and boundary irregularity have the strongest influence on predictions.

Important features identified by the model

1 area_worst  
2 concave_points_worst  
3 radius_worst  
4 perimeter_worst  
5 concave_points_mean  

Size related features such as area radius and perimeter measure the overall tumor size.

Shape related features such as concave points and concavity describe the irregularity of the tumor boundary.

Malignant tumors often have larger sizes and more irregular shapes which makes these features strong predictors.

## Interactive Demo

A Streamlit application was created to visualize the dataset and model results interactively.

The dashboard allows users to

Preview the dataset  
View distribution of benign and malignant tumors  
Display the most important features used by the model  
Explore feature distributions interactively  

## How to Run the Project

### Clone the repository
```bash
git clone https://github.com/Prayagxraj/breast-cancer-ml-optimisation-analysis.git
```

### Navigate to the project folder
```bash
cd breast-cancer-ml-optimisation-analysis
```

### Create virtual environment
```bash
python -m venv venv
```

### Activate environment

Mac
```bash
source venv/bin/activate
```

Windows
```bash
venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the Streamlit application
```bash
streamlit run app.py
```

---

## Project Structure

```
TASK2_ML_OPTIMIZATION
│
├── data
│   └── data.csv
│
├── notebook
│   └── breast_cancer.ipynb
│
├── report
│   └── results.md
│
├── app.py
└── requirements.txt
```

## Conclusion

The baseline Logistic Regression model achieved an accuracy of approximately 97.36 percent using 5 fold cross validation.

After removing multicollinear features using VIF the accuracy slightly decreased to about 97.01 percent suggesting that some correlated features may still contribute useful predictive information.

The Random Forest model achieved an accuracy of approximately 96.14 percent and hyperparameter tuning produced similar performance.

These results indicate that the dataset is largely linearly separable which explains why Logistic Regression performs slightly better than the more complex Random Forest model.

