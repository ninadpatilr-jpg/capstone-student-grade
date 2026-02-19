### Data-Driven Insights into Student Academic Performance

**Ninad Patil**

####  Executive summary
This project analyzes the factors that influence student academic performance and builds predictive models to estimate future academic outcomes based on current student characteristics.

The goal is not only to predict grades but to translate findings into actionable recommendations for schools, educators, and policymakers.

#### Rationale
Student performance is influenced by multiple interconnected factors --- academic habits, socio-demographic background, and access to resources. However, decisions about interventions are often made based on assumptions rather than evidence.

This project aims to:
 - Identify the most influential factors affecting student grades
 - Distinguish strong predictors from weak or commonly assumed factors
 - Provide early indicators of academic risk
 - Deliver data-driven recommendations for performance improvement
 

#### Research Question
Student academic performance is often discussed, but the drivers behind it are not always clearly understood. This capstone project will provide an actionable insights backed by data:
 - How schools can design targeted support programs for at-risk students
 - Improve student outcomes
 - Reduce academic underperformance early
 - Make informed decisions grounded in data rather than assumptions

#### Data Sources

The dataset will be sourced from Kaggle, using publicly available student performance data containing academic results and student background attributes. 
- Local file: `data/StudentPerformanceFactors.csv`
- Original dataset: https://www.kaggle.com/datasets/ayeshaseherr/student-performance

The dataset includes:
 - Demographic variables (Age, Gender)
 - Academic behavior variables (Study Time, Absences)
 - Family background (Parental Education)
 - Support indicators (Tutoring, Internet Access)
 - Academic outcome (Final Score)

#### Methodology
This project follows the CRISP-DM framework:

### 1️⃣ Business Understanding
Define the key drivers of student performance and determine how findings can inform early intervention strategies.

### 2️⃣ Data Understanding
 - Exploratory Data Analysis (EDA)
 - Distribution analysis
 - Correlation analysis
 - Identification of patterns and anomalies

### 3️⃣ Data Preparation
 - Handling missing values
 - Encoding categorical variables
 - Feature engineering (e.g., effort index, pass/fail classification)
 - Train-test split

### 4️⃣ Modeling
Baseline and comparative models including:
 - Linear Regression
 - Logistic Regression
 - Ridge
 - Lasso
 - KNN
 - RandomForest
 - GradientBoosting

### 5️⃣ Evaluation
 - RMSE and R² (for regression)
 - Accuracy, Precision, Recall, F1-score (for classification)
 - Cross-validation to reduce overfitting
 - Feature importance analysis

Exploratory data analysis, basic statistical analysis, feature engineering, linear and multiple regression, logistic regression, k-Nearest Neighbors, decision trees, PCA, and model evaluation with regularization to prevent overfitting.

#### Results
This initiative is expected to make teacher(s) understand, which factors most strongly affect academic performance:
 - A measurable framework for identifying academic risk
 - Evidence-based prioritization of interventions
 - Clear guidance on where educational institutions should focus resources

Otherwise
 - At-risk students may not be identified early
 - Resources may be allocated inefficiently
 - Interventions may target weak predictors rather than impactful ones
Below are cross-validated results for models evaluated (Train_Time, Train_Accuracy, Test_Accuracy, CV_MSE reported as mean squared error on validation folds; CV_R2 is mean R²):

| Model | Train_Time | Train_Accuracy | Test_Accuracy | Test_MSE | Test_R2CV_MSE |
|---|---:|---:|---:|---:|---:|
| Ridge | 0.009380 | 0.715675 | 0.768282 | 3.275349 | 0.768282 |
| LinearRegression | 0.010401 | 0.715675 | 0.768280 | 3.275385 | 0.768280 |
| GradientBoosting | 0.386067 | 0.743125 | 0.736137 | 3.729723 | 0.736137 |
| LogisticRegression | 0.507928 | 0.641816 | 0.589259 | 3.872163 | 0.726060 |
| RandomForest | 1.290086 | 0.948018 | 0.677094 | 4.564297 | 0.677094 |
| KNN | 0.012539 | 0.651684 | 0.515958 | 6.841967 | 0.515958 |
| Lasso | 0.009821 | 0.398994 | 0.437833 | 7.946270 | 0.437833 |


#### Next steps
 - Implement advanced models (Random Forest, Gradient Boosting)
 - Compare model performance against baseline
 - Perform hyperparameter tuning
 - Use k-fold cross-validation (with more folds) and report confidence intervals for metrics.
 - Translate technical findings into executive summary
 - Prepare presentation-ready visuals
 - provide an UI as a guideline where student can provide their information and it will update them with potential grades

#### Outline of project
- [Jupyter Notebook — Student Performnce Factors](student_performance_factors.ipynb)

##### Contact and Further Information
For questions or feedback please reach out to Ninad Patil, using github profile. See `student_performance_factors.ipynb` for code, visualizations, and detailed results.
