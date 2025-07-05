import pandas as pd
import yaml
import sys

# Load config
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Load raw data
try:
    df = pd.read_csv(config["raw_data_path"])
except Exception as e:
    print("Failed to load raw data:", e)
    sys.exit(1)

# Convert transaction_amount to numeric, coercing errors to NaN
df["transaction_amount"] = pd.to_numeric(df["transaction_amount"], errors="coerce")

# Check for required columns before proceeding
required_columns = ["user_id", "transaction_amount", "created_at"]
missing = [col for col in required_columns if col not in df.columns]

if missing:
    print(f"Missing required column(s): {missing}")
    sys.exit(1)

# Drop irrelevant columns
df.drop(columns=config["drop_columns"], inplace=True, errors="ignore")

# Remove rows with missing values in key columns
df.dropna(subset=["user_id", "transaction_amount"], inplace=True)

# Convert dates safely
for col in config["date_columns"]:
    df[col] = pd.to_datetime(df[col], errors="coerce")

# Drop rows with invalid date values
df.dropna(subset=config["date_columns"], inplace=True)

# Save cleaned data
try:
    df.to_csv(config["cleaned_data_path"], index=False)
    print("Data cleaned and saved successfully.")
except Exception as e:
    print("Failed to save cleaned data:", e)
