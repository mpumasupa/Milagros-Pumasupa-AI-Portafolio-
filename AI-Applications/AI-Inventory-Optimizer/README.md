# AI Inventory Optimizer

**Authors:** Milagros Pumasupa, Ahad Maredia, Larry Towett, Yasmin Bello  
**Course:** ITAI 2277: Artificial Intelligence Resource  
**Professor:** Anna Devarakonda  
**Date:** October 2025  

---

## Project Overview

The AI Inventory Optimizer is an AI-powered system designed to improve inventory management for retail stores by predicting weekly product demand, recommending trending products, and providing actionable insights through an interactive dashboard. The system aims to reduce overstock and stockouts, optimize product availability, and enhance business profitability.

The project was developed as part of the ITAI 2277:Artificial Intelligence Resource course and involved data preprocessing, model development, evaluation, and deployment of a working prototype (MVP).

---
## Project Structure

```
AI-Inventory-Optimizer/
├── notebooks/
│ ├── Model_training_baseline_AI_Inventory_Optimizer.ipynb
│ └── Model_optimization_and_evaluation_AI_Inventory_Optimizer.ipynb
├── data/
│ ├── train.csv
│ ├── features.csv
│ ├── stores.csv
│ └── walmart_preprocessed.zip # Preprocessed and cleaned dataset for modeling
├── mvp/
│ └── inventory_mvp # Final integrated prototype
├── reports/
│ ├── AI_Inventory_Optimizer_Evaluation_Report.pdf
│ └── AI_Inventory_Optimizer_Project_Report.pdf
├── src/ # Optional Python scripts
│ └── helper_functions.py
└── README.md
```
## Project Reports

### 1. Data Report
- Historical sales data exploration and cleaning  
- Feature engineering including lag features and trend indicators  
- Handling missing values and outliers  
- Summary statistics and initial insights  

### 2. Evaluation Report
- Baseline model performance (Linear Regression)  
- Advanced models: Random Forest, Gradient Boosting, XGBoost  
- Hyperparameter tuning and cross-validation  
- Model comparison and selection based on accuracy, RMSE, and business metrics  

---

## Team Members

| Name | Role / Contribution |
|------|-------------------|
| Milagros Pumasupa | Data preprocessing, feature engineering, report writing, and Model experimentation and tuning |
| Ahad Maredia | Model experimentation and tuning |
| Larry Towett | MVP prototype development and integration |
| Yasmin Bello | Data visualization and dashboard creation, and MVP prototype development and integration |

---

## Tools Used

- Python  
- Google Colab  
- Pandas, NumPy, scikit-learn  
- XGBoost  
- Git and GitHub  

---


## Data Sources

- **Kaggle:** Walmart Recruiting: Store Sales Forecasting  
- **Files used:**
  - `train.csv` – historical weekly sales data by store and department
  - `features.csv` – external variables (fuel prices, CPI, unemployment, markdowns)
  - `stores.csv` – metadata for each store (type, size)
  - `walmart_preprocessed.zip` – preprocessed and cleaned dataset used for model training

All data is anonymized and aggregated at the store level to protect privacy.

---

## Workflow

1. **Data Preprocessing**  
   - Merging datasets and cleaning missing values  
   - Feature engineering: date-based features, promotional activity aggregation, categorical encoding, normalization  
   - Final preprocessed dataset: `walmart_preprocessed.csv`  

2. **Model Development**  
   - Baseline models: Linear Regression, Random Forest, Gradient Boosting  
   - Advanced models: XGBoost with hyperparameter tuning  
   - Feature engineering for temporal patterns: lag, rolling, differenced, and store × department interactions  

3. **Evaluation**  
   - Metrics: MAE, RMSE, R²  
   - Comparison of baseline vs advanced models  
   - Visualization of predicted vs actual sales  

4. **MVP Prototype**  
   - Integrated system using the final XGBoost model  
   - Prepared for deployment and demonstration  
   - Stored in `mvp/inventory_mvp`  

---

## Key Insights

- Random Forest and XGBoost significantly outperformed Linear Regression in capturing non-linear relationships.  
- Feature engineering improved the model’s ability to account for temporal and store-department interactions.  
- The final tuned XGBoost model achieved **R² = 0.9547** and **RMSE = 4,858.7**, providing highly accurate weekly sales predictions.  

---

## Usage

To run the notebooks and reproduce results:

1. Clone the repository:  
```
git clone <your-repo-link>
cd AI-Inventory-Optimizer
Install required libraries:

pip install -r requirements.txt
Open Jupyter or Colab and execute the notebooks in order:

Model_training_baseline_AI_Inventory_Optimizer.ipynb

Model_optimization_and_evaluation_AI_Inventory_Optimizer.ipynb

Access the final integrated MVP in mvp/inventory_mvp.

License

This project is developed for educational purposes as part of ITAI 2277:Artificial Intelligence Resource course.
