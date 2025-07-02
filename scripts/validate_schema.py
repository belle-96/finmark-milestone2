import pandas as pd
import pandera as pa
from pandera import Column, DataFrameSchema

# Define the expected schema
schema = DataFrameSchema({
    "user_id": Column(str, nullable=False),
    "transaction_amount": Column(float, nullable=False),
    "created_at": Column(pa.DateTime, nullable=False),
})

# Load the cleaned dataset
df = pd.read_csv("data/processed/transactions_clean.csv")

# Convert created_at column to datetime in case it's still string
df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")

# Validate against schema
try:
    schema.validate(df)
    print("✅ Schema validation passed.")
except pa.errors.SchemaError as e:
    print("❌ Schema validation failed:")
    print(e)