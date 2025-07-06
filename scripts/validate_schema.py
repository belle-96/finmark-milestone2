import pandas as pd
import pandera.pandas as pa
from pandera.pandas import Column, DataFrameSchema
import yaml
import os

# Load config
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Define the expected schema
schema = DataFrameSchema({
    "user_id": Column(str, nullable=False),
    "transaction_amount": Column(float, nullable=True),
    "created_at": Column(pa.DateTime, nullable=False),
})

# Load the cleaned dataset
df = pd.read_csv(config["validation"]["processed_data_path"])

# Convert created_at column to datetime in case it's still string
df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")

# Validate against schema
try:
    schema.validate(df)
    print("✅ Schema validation passed.")
except pa.errors.SchemaError as e:
    print("❌ Schema validation failed:")
    print(e)
