import pandas as pd

print("=" * 70)
print("SALES ANALYTICS DASHBOARD - DATASET INSPECTION")
print("=" * 70)

file_path = "Financial Sample.xlsx"

print("\nLoading Excel file...")

excel_file = pd.ExcelFile(file_path)

print("\nAvailable sheets:")
print(excel_file.sheet_names)

for sheet in excel_file.sheet_names:
    print("\n" + "=" * 70)
    print(f"SHEET: {sheet}")
    print("=" * 70)

    data = pd.read_excel(file_path, sheet_name=sheet)

    print("\nNumber of rows:", len(data))
    print("Number of columns:", len(data.columns))

    print("\nColumn names:")
    print(list(data.columns))

    print("\nFirst 5 rows:")
    print(data.head())

    print("\nData types:")
    print(data.dtypes)

    print("\nMissing values:")
    print(data.isnull().sum())

print("\n" + "=" * 70)
print("DATASET INSPECTION COMPLETED")
print("=" * 70)