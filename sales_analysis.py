import pandas as pd

print("=" * 70)
print("SALES ANALYTICS DASHBOARD - BUSINESS KPI ANALYSIS")
print("=" * 70)

# Load cleaned dataset
file_path = "cleaned_sales_data.csv"

print("\nLoading cleaned dataset...")

sales = pd.read_csv(file_path)

print("Dataset loaded successfully.")
print("Total records:", len(sales))

# ---------------------------------------------------------
# Calculate Business KPIs
# ---------------------------------------------------------

total_sales = sales["Sales"].sum()
total_profit = sales["Profit"].sum()
total_units = sales["Units Sold"].sum()
total_records = len(sales)

average_sales = sales["Sales"].mean()

profit_margin = (total_profit / total_sales) * 100

# ---------------------------------------------------------
# Display KPIs
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("KEY PERFORMANCE INDICATORS")
print("=" * 70)

print(f"\nTotal Sales      : ${total_sales:,.2f}")
print(f"Total Profit     : ${total_profit:,.2f}")
print(f"Total Units Sold : {total_units:,.0f}")
print(f"Total Records    : {total_records:,}")
print(f"Average Sales    : ${average_sales:,.2f}")
print(f"Profit Margin    : {profit_margin:.2f}%")

# ---------------------------------------------------------
# Product Analysis
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("SALES BY PRODUCT")
print("=" * 70)

product_sales = (
    sales.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(product_sales)

# ---------------------------------------------------------
# Country Analysis
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("SALES BY COUNTRY")
print("=" * 70)

country_sales = (
    sales.groupby("Country")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(country_sales)

# ---------------------------------------------------------
# Segment Analysis
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("SALES BY SEGMENT")
print("=" * 70)

segment_sales = (
    sales.groupby("Segment")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(segment_sales)

# ---------------------------------------------------------
# Year Analysis
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("SALES BY YEAR")
print("=" * 70)

year_sales = (
    sales.groupby("Year")["Sales"]
    .sum()
    .sort_index()
)

print(year_sales)

print("\n" + "=" * 70)
print("KPI ANALYSIS COMPLETED")
print("=" * 70)