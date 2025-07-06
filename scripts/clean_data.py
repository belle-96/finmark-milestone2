import pandas as pd
import yaml
import sys
import os

# Load config
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Load raw data
try:
    df = pd.read_csv(config["data"]["raw_data_path"])
except Exception as e:
    raw_data = f"Failed to load raw data: {e}"
    print(raw_data)
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
df.drop(columns=config["data"]["drop_columns"], inplace=True, errors="ignore")

# Remove rows with missing values in key columns
df.dropna(subset=["user_id", "transaction_amount"], inplace=True)

# Convert dates safely
for col in config["data"]["date_columns"]:
    df[col] = pd.to_datetime(df[col], errors="coerce")

# Drop rows with invalid date values
df.dropna(subset=config["data"]["date_columns"], inplace=True)

# Save cleaned data
output_folder = config["data"]['output_folder']
FIXED_BASE_FILENAME = "transactions_cleaned"

def get_next_filename(folder, base_name, extension=".csv"):
    i = 1
    while True:
        filename = f"{base_name}_{i}{extension}"
        full_path = os.path.join(folder, filename)
        if not os.path.exists(full_path):
            return full_path
        i += 1
try:
    # Get the full path for the next available file using the fixed base filename
    save_path = get_next_filename(output_folder, FIXED_BASE_FILENAME)

    df.to_csv(save_path, index=False)
    print(f"Data cleaned and saved successfully to: {save_path}")
except Exception as e:
    print(f"Failed to save cleaned data: {e}")
