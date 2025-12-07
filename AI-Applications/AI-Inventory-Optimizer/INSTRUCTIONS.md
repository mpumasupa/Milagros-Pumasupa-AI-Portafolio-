AI Inventory Optimizer - Instructions for Running the Prototype
Overview

This document provides instructions to set up and run the AI Inventory Optimizer integrated prototype. The system predicts weekly product demand, recommends trending products, and provides actionable insights for inventory management.

Project Structure
AI-Inventory-Optimizer/
├── notebooks/
│   ├── Model_training_baseline_AI_Inventory_Optimizer.ipynb
│   └── Model_optimization_and_evaluation_AI_Inventory_Optimizer.ipynb
├── data/
│   ├── train.csv
│   ├── features.csv
│   └── stores.csv
├── mvp/
│   └── inventory_mvp
├── reports/
│   ├── AI_Inventory_Optimizer_Evaluation_Report.pdf
│   └── AI_Inventory_Optimizer_Project_Report.pdf
├── src/
│   └── helper_functions.py
└── README.md

Setup Instructions

Clone the Repository

git clone <your-repository-url>
cd AI-Inventory-Optimizer


Set Up Python Environment
Create a virtual environment and install required packages:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install --upgrade pip
pip install -r requirements.txt


Data Preparation
Ensure all CSV files are located in the data/ folder. No additional preprocessing is required, as the integrated prototype uses preprocessed data.

Running the Prototype
Navigate to the mvp/ folder and run the main prototype:

cd mvp
python inventory_mvp


The system will load preprocessed data, run the predictive models, and output forecasts and recommendations.

Optional: Explore Notebooks
The notebooks/ folder contains Jupyter notebooks for:

Model training and baseline evaluation: Model_training_baseline_AI_Inventory_Optimizer.ipynb

Model optimization and evaluation: Model_optimization_and_evaluation_AI_Inventory_Optimizer.ipynb

Open the notebooks in Jupyter or Google Colab to explore data preprocessing, feature engineering, model experiments, and evaluation results.

Reports
Project and evaluation reports are located in the reports/ folder for reference:

AI_Inventory_Optimizer_Project_Report.pdf

AI_Inventory_Optimizer_Evaluation_Report.pdf