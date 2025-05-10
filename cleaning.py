import pandas as pd

# Load your existing CSV file with 100 values
df = pd.read_csv("amazon_soft_toys.csv")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Drop rows with missing or broken data
df.dropna(subset=["Rating", "Reviews", "Selling Price"], inplace=True)

# Convert columns to correct numeric types
df["Reviews"] = pd.to_numeric(df["Reviews"])
df["Rating"] = pd.to_numeric(df["Rating"])
df["Selling Price"] = pd.to_numeric(df["Selling Price"])

# Save cleaned data
df.to_csv("cleaned_amazon_soft_toys.csv", index=False)
print("✅ Cleaned data saved to cleaned_amazon_soft_toys.csv")
print(f"✅ Total Products After Cleaning: {len(df)}")
print("✅ Data cleaning completed successfully.")
