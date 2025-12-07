# inventory_mvp.py
"""
AI Inventory Optimizer, possible Command-line Prototype for phase 4.

What this prototype does:
- Loads the preprocessed Walmart dataset (walmart_preprocessed.csv)
- Trains a "RandomForestRegressor" on historical Weekly_Sales
- Asks the person (user)for a scenario (Store, Dept, Month, Week, etc.)
- Prints a predicted Weekly_Sales value


"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from math import sqrt
import os

DATA_PATH = "walmart_preprocessed.csv"

def load_data(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} not found. Make sure it is in the same folder as this script.")
    df = pd.read_csv(path)

    # Required columns
    base_cols = [
        "Store","Dept","Size","Temperature","Fuel_Price","CPI","Unemployment",
        "Total_MarkDown","Month","Week","DayOfWeek","IsWeekend"
    ]
    for c in base_cols:
        if c not in df.columns:
            raise ValueError(f"Required column '{c}' is missing from dataset.")

    # Optional one-hot flags
    optional_cols = ["Type_B","Type_C","IsHoliday_True"]
    for c in optional_cols:
        if c not in df.columns:
            df[c] = 0

    if "Weekly_Sales" not in df.columns:
        raise ValueError("Target column 'Weekly_Sales' is missing from dataset.")

    return df

def train_model(df: pd.DataFrame):
    feature_cols = [
        "Store","Dept","Size","Temperature","Fuel_Price","CPI","Unemployment",
        "Total_MarkDown","Month","Week","DayOfWeek","IsWeekend",
        "Type_B","Type_C","IsHoliday_True"
    ]

    X = df[feature_cols]
    y = df["Weekly_Sales"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    model = RandomForestRegressor(
        n_estimators=150,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    rmse = sqrt(mean_squared_error(y_test, preds))
    r2 = r2_score(y_test, preds)

    print("\n=== Model Trained ===")
    print(f"MAE : {mae:,.2f}")
    print(f"RMSE: {rmse:,.2f}")
    print(f"R^2 : {r2:.4f}")
    print("=====================\n")

    return model, feature_cols, df

def get_float(prompt: str, default: float) -> float:
    while True:
        raw = input(f"{prompt} (press Enter to use {default:.2f}): ").strip()
        if raw == "":
            return default
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number.")

def get_int(prompt: str, default: int) -> int:
    while True:
        raw = input(f"{prompt} (press Enter to use {default}): ").strip()
        if raw == "":
            return default
        try:
            return int(raw)
        except ValueError:
            print("Please enter a valid integer.")

def main():
    print("=== AI Inventory Optimizer – Command-line Prototype ===")
    print("This prototype trains a demand forecasting model")
    print("and lets you get a predicted Weekly_Sales value.\n")

    df = load_data(DATA_PATH)
    model, feature_cols, df_full = train_model(df)

    # Default values from medians
    defaults = {
        "Store": int(df_full["Store"].median()),
        "Dept": int(df_full["Dept"].median()),
        "Size": float(df_full["Size"].median()),
        "Temperature": float(df_full["Temperature"].median()),
        "Fuel_Price": float(df_full["Fuel_Price"].median()),
        "CPI": float(df_full["CPI"].median()),
        "Unemployment": float(df_full["Unemployment"].median()),
        "Total_MarkDown": float(df_full["Total_MarkDown"].median()),
        "Month": int(df_full["Month"].median()),
        "Week": int(df_full["Week"].median()),
        "DayOfWeek": int(df_full["DayOfWeek"].median()),
        "IsWeekend": 0,
        "Type_B": 0,
        "Type_C": 0,
        "IsHoliday_True": 0,
    }

    while True:
        print("\nEnter scenario details to get a prediction:\n")

        store = get_int("Store ID", defaults["Store"])
        dept = get_int("Department ID", defaults["Dept"])
        size = get_float("Store Size (sqft)", defaults["Size"])
        temp = get_float("Temperature (F)", defaults["Temperature"])
        fuel = get_float("Fuel Price", defaults["Fuel_Price"])
        cpi = get_float("CPI", defaults["CPI"])
        unemp = get_float("Unemployment rate", defaults["Unemployment"])
        markdown = get_float("Total Markdown amount", defaults["Total_MarkDown"])
        month = get_int("Month (1–12)", defaults["Month"])
        week = get_int("Week number (1–52)", defaults["Week"])
        dow = get_int("Day of week (1=Mon ... 7=Sun)", defaults["DayOfWeek"])

        is_weekend = 1 if dow in (6, 7) else 0
        is_holiday = 0
        type_b = 0
        type_c = 0

        row = {
            "Store": store,
            "Dept": dept,
            "Size": size,
            "Temperature": temp,
            "Fuel_Price": fuel,
            "CPI": cpi,
            "Unemployment": unemp,
            "Total_MarkDown": markdown,
            "Month": month,
            "Week": week,
            "DayOfWeek": dow,
            "IsWeekend": is_weekend,
            "Type_B": type_b,
            "Type_C": type_c,
            "IsHoliday_True": is_holiday,
        }

        X_new = pd.DataFrame([row])[feature_cols]
        pred = model.predict(X_new)[0]

        print(f"\n>>> Predicted Weekly_Sales for this scenario: ${pred:,.2f}\n")

        again = input("Do you want to try another scenario? (y/n): ").strip().lower()
        if again != "y":
            print("\nExiting prototype. Goodbye!")
            break

if __name__ == "__main__":
    main()
