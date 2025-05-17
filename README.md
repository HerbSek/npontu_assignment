# npontu_assignment

#  E-Commerce Customer Behavior Analysis

##  Objective

This project analyzes synthetic customer activity data on an e-commerce platform. The aim is to generate actionable insights to improve **sales**, enhance **customer engagement**, and personalize the **shopping experience**.


##  Features of the Project

### 1.  Data Analysis & Cleaning
- Performed **exploratory data analysis (EDA)** to understand structure and patterns.
- Cleaned missing values, removed duplicates, and encoded categorical variables.
- Identified the most influential features using **correlation** with the `purchased` column.

### 2.  Feature Engineering
- Used **LabelEncoding** for categorical data.

### 3.  Predictive Modeling
- Built a **classification model** using Random Forest.
- Achieved **100% accuracy** (due to synthetic nature of data).
- Validated using **cross-validation (CV)**:
  - Mean CV Accuracy: `1.0`
  - Std. Deviation: `0.0`

### 4.  Business Insights
- Top 3 features influencing purchase behavior:
  - `price`, `product_category`, and `session_time`
- Recommendation: Focus on **price optimization**, **targeted marketing**, and **UX improvements** for longer session time.

##  Visualizations
All visual insights were generated using:
- **Seaborn** and **Matplotlib** in Python

## Final Thoughts

This project provides a complete pipeline:
- From data generation, cleaning, analysis
- To modeling and big data simulation
- Plus actionable insights for improving e-commerce strategy

