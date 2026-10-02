import pandas as pd

print("=" * 70)
print("SALES ANALYTICS DASHBOARD - DATA CLEANING")
print("=" * 70)

# Load Excel dataset
file_path = "Financial Sample.xlsx"

print("\nLoading dataset...")

sales = pd.read_excel(file_path)

print(f"Original rows: {len(sales)}")
print(f"Original columns: {len(sales.columns)}")

# ---------------------------------------------------------
# 1. Clean column names
# ---------------------------------------------------------

print("\nCleaning column names...")

sales.columns = sales.columns.str.strip()

print("Updated column names:")
print(list(sales.columns))

# ---------------------------------------------------------
# 2. Check duplicate records
# ---------------------------------------------------------

print("\nChecking duplicate records...")

duplicates = sales.duplicated().sum()

print("Duplicate rows:", duplicates)

if duplicates > 0:
    sales = sales.drop_duplicates()
    print("Duplicate rows removed.")
else:
    print("No duplicate rows found.")

# ---------------------------------------------------------
# 3. Handle missing values
# ---------------------------------------------------------

print("\nChecking missing values...")

print(sales.isnull().sum())

# Discount Band is a categorical column.
# Replace missing values with "Unknown".

sales["Discount Band"] = sales["Discount Band"].fillna("Unknown")

print("\nMissing values after cleaning:")
print(sales.isnull().sum())

# ---------------------------------------------------------
# 4. Convert date column
# ---------------------------------------------------------

print("\nChecking date column...")

sales["Date"] = pd.to_datetime(sales["Date"])

print("Date column converted successfully.")

# ---------------------------------------------------------
# 5. Create useful analysis columns
# ---------------------------------------------------------

print("\nCreating additional analysis columns...")

sales["Month"] = sales["Date"].dt.month
sales["Quarter"] = sales["Date"].dt.quarter

print("Created:")
print("- Month")
print("- Quarter")

# ---------------------------------------------------------
# 6. Save cleaned dataset
# ---------------------------------------------------------

output_file = "cleaned_sales_data.csv"

sales.to_csv(output_file, index=False)

print("\n" + "=" * 70)
print("DATA CLEANING COMPLETED")
print("=" * 70)

print("\nFinal rows:", len(sales))
print("Final columns:", len(sales.columns))

print("\nCleaned dataset saved as:")
print(output_file)

print("\nFinal dataset preview:")
print(sales.head())

print("\nFinal missing-value check:")
print(sales.isnull().sum())

print("\n" + "=" * 70)