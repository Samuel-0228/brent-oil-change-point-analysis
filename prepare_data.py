# prepare_data.py
import pandas as pd
import numpy as np
import os
import sys

# Where the file should be
INPUT_FILE = "data/raw/brent_prices.csv"
OUTPUT_FILE = "data/processed/brent_2012_2022.csv"
OUTPUT_FILE_T = "data/processed/brent_model_ready.csv"

print("Checking for input file...")
if not os.path.isfile(INPUT_FILE):
    print(f"\nERROR: File not found: {INPUT_FILE}")
    print("Current directory:", os.getcwd())
    print("Please put 'brent_prices.csv' inside the 'data/raw/' folder.")
    sys.exit(1)

print(f"Found: {INPUT_FILE}")
print("Reading file...")

try:
    df = pd.read_csv(INPUT_FILE)
except Exception as e:
    print("Error reading file:", e)
    sys.exit(1)

print("Columns:", df.columns.tolist())
print("First rows:\n", df.head(3))

# Guess columns (very simple version)
date_col = None
price_col = None

for col in df.columns:
    cl = col.lower()
    if "date" in cl or "day" in cl:
        date_col = col
    if "price" in cl or "close" in cl or "brent" in cl:
        price_col = col

if not date_col or not price_col:
    print("Could not automatically find date and/or price column.")
    print("Please edit the file and rename columns to 'Date' and 'Price'.")
    sys.exit(1)

print(f"Using date column: {date_col}")
print(f"Using price column: {price_col}")

# Convert dates
df[date_col] = pd.to_datetime(df[date_col], errors='coerce', dayfirst=True)
df = df.dropna(subset=[date_col]).sort_values(date_col).set_index(date_col)

# Keep only price
df = df[[price_col]].rename(columns={price_col: "price"})

# Features
df["log_price"] = np.log(df["price"])
df["log_return"] = df["log_price"].diff()

# Subset
df_model = df["2012":"2022-09-30"].copy()

print("\nFinal shape:", df_model.shape)
print(df_model.head())
print(df_model.tail())

# Save
os.makedirs("data/processed", exist_ok=True)
df_model.to_csv(OUTPUT_FILE)
print(f"\nSaved: {OUTPUT_FILE}")

# With time index 0,1,2,...
df_reset = df_model.reset_index()
df_reset["t"] = np.arange(len(df_reset))
df_reset.to_csv(OUTPUT_FILE_T, index=False)
print(f"Saved with t column: {OUTPUT_FILE_T}")

print("\nDone.")
