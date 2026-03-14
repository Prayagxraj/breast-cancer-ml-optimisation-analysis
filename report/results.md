

                                                    Model Comparison and Improvements


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Dataset :


The experiment was conducted using the Breast Cancer Wisconsin Diagnostic dataset.
Dataset Contains 569 samples and 30 numerical features describing tumor characteristics.
The target variable was  (diagnosis) and it was converted from Categorial variables to Numeric labels

          1 --> Malignant 
          0 --> Benign

Two Unnecessary columns (id and Unamed) were removed during preprocessing.

Malignant --> It means Tumor is cancerous. It can grow aggressively and spread to ther parts of the body.
Benign    --> It means Tumor is non-cancerous. It grows slowly and does not spread 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Baseline Model :-

The baseline model used Logistic Regression with feature scaling through a pipeline.

Model evaluation was performed using 5 -fold Cross Validation 

Baseline Performance was 0.935 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 IMPROVEMENT -1 (Feature Engineering[VIF])

The correlation heatmap showed a strong relationship between features such as radius, perimeter and area indicating multicollinearity.

To address this, Variance Inflation Factor (VIF) was used to detect and remove highly correlated features.
Features with VIF>10 were iteratively removed(One by One).

After removing multicolinear features , Logistic Regression was retrained.

PERFORMANCE AFTER VIF FILTERING --> 

METRIC       VALUE 
Accuracy     0.9737



IMPACT -->
Accuracy improved from 0.935 --> 0.9737 which is an improvement of approx 3.8 %.

This indicates that removing redundant correlated features helped the model learn more stable relationships.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

IMPROVEMENT - 2 (RANDOM FOREST MODEL)

A Random forest classifier was trained to capture non linear relationships between features.

Model configuration was :

. n_estimators= 300
. random_state= 42

METRIC       VALUE 
Accuracy     0.9737


IMPACT -->

Random Forest achieved the same accuracy as the improved Logistic Regression model , suggesting that the dataset is highly predictable and can be effectively modeled using either linear or Tree Based methods ...


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

IMPROVEMENT - 3  (HYPERPARAMETER TUNING)

Hyperparameter Tuning was applied to random forewst using GRID SEARCH CV  with 5-fold cross validation

Parameters Tuned :
. n_estimators
. max_depth
. min_sample_split

The tuned model achieved the same test accuracy as the untuned Random forest model


[METRIC]                    [VALUE] 
Tuned random Forest          0.9737

IMPACT --> 
HT did not further improve accurracy , indicating that the default Random Forest config already performed near the optimal for this dataset.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

MODEL COMPARISON  --> 

[MODEL]                                  [ACCURACY]

Logistic Regression (Baseline CV).         0.9350

Logistic Regression (After VIF)            0.9737

Random forest                              0.9737

Random Forest (TUNED)                      0.9737



---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



Feature Importance -> 

Random Forest feature importance analysis shows that features related to tumor size and boundary irregularity are the most influential predictors.


The most important features identified by the model are:
	1.	area_worst
	2.	concave_points_worst
	3.	radius_worst
	4.	perimeter_worst
	5.	concave_points_mean


    These features are primarily related to tumor size and boundary irregularity.
	•	Size-related features such as area_worst, radius_worst, and perimeter_worst measure how large the tumor is.
	•	Shape-related features such as concave_points_worst and concavity_mean capture how irregular the tumor boundary is.

The model assigns higher importance to these features because malignant tumors often exhibit larger sizes and more irregular boundaries compared to benign tumors.

This indicates that the Random Forest model relies mainly on tumor geometry and structural irregularity to classify tumors as malignant or benign.



---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Interactive Demo (Streamlit)

A simple Streamlit application was created to visualize the dataset and model results interactively.

The app loads the dataset, performs preprocessing, and trains a Random Forest model. It allows users to:
	•	Preview the dataset
	•	View the distribution of benign vs malignant tumors
	•	See the top 10 important features from the model
	•	Explore the distribution of individual features using an interactive selector 

interactive dashboard instead of only static analysis.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



Conclusion ->

The baseline Logistic Regression model achieved 93.5% accuracy using cross-validation.

After applying VIF-based feature engineering, the model accuracy improved to 97.37%, representing a 3.8% improvement 

Random Forest achieved similar performance  indicating that the dataset is highly predictable and that the key predictive signals are captured effectively by both linear and ensemble models 

Hyperparameter tuning did not further improve performance  suggesting that the dataset is already well modeled by the selected algorithms.