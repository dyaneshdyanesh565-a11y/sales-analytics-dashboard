import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("=" * 70)
print("SALES ANALYTICS DASHBOARD - DATA VISUALIZATION")
print("=" * 70)

# Load cleaned dataset
file_path = "cleaned_sales_data.csv"

print("\nLoading cleaned dataset...")

sales = pd.read_csv(file_path)

print("Dataset loaded successfully.")
print("Total records:", len(sales))

# Create folder for charts
output_folder = "visualizations"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

print("\nVisualization folder ready.")

# ----------------------------------------------------------
# 1. SALES BY PRODUCT
# ----------------------------------------------------------

print("\nCreating Product Sales Chart...")

product_sales = (
    sales.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    os.path.join(output_folder, "sales_by_product.png"),
    dpi=300
)

plt.close()

print("Saved: sales_by_product.png")


# ----------------------------------------------------------
# 2. SALES BY COUNTRY
# ----------------------------------------------------------

print("\nCreating Country Sales Chart...")

country_sales = (
    sales.groupby("Country")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

country_sales.plot(kind="bar")

plt.title("Sales by Country")
plt.xlabel("Country")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    os.path.join(output_folder, "sales_by_country.png"),
    dpi=300
)

plt.close()

print("Saved: sales_by_country.png")


# ----------------------------------------------------------
# 3. SALES BY SEGMENT
# ----------------------------------------------------------

print("\nCreating Segment Sales Chart...")

segment_sales = (
    sales.groupby("Segment")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

segment_sales.plot(kind="bar")

plt.title("Sales by Customer Segment")
plt.xlabel("Segment")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    os.path.join(output_folder, "sales_by_segment.png"),
    dpi=300
)

plt.close()

print("Saved: sales_by_segment.png")


# ----------------------------------------------------------
# 4. SALES BY YEAR
# ----------------------------------------------------------

print("\nCreating Yearly Sales Chart...")

year_sales = (
    sales.groupby("Year")["Sales"]
    .sum()
    .sort_index()
)

plt.figure(figsize=(8, 5))

year_sales.plot(kind="line", marker="o")

plt.title("Sales Trend by Year")
plt.xlabel("Year")
plt.ylabel("Sales ($)")
plt.grid(True)

plt.tight_layout()

plt.savefig(
    os.path.join(output_folder, "sales_by_year.png"),
    dpi=300
)

plt.close()

print("Saved: sales_by_year.png")


# ----------------------------------------------------------
# 5. PROFIT BY PRODUCT
# ----------------------------------------------------------

print("\nCreating Product Profit Chart...")

product_profit = (
    sales.groupby("Product")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

product_profit.plot(kind="bar")

plt.title("Profit by Product")
plt.xlabel("Product")
plt.ylabel("Profit ($)")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    os.path.join(output_folder, "profit_by_product.png"),
    dpi=300
)

plt.close()

print("Saved: profit_by_product.png")


# ----------------------------------------------------------
# 6. MONTHLY SALES TREND
# ----------------------------------------------------------

print("\nCreating Monthly Sales Trend...")

sales["Date"] = pd.to_datetime(sales["Date"])

monthly_sales = (
    sales.groupby("Date")["Sales"]
    .sum()
    .sort_index()
)

plt.figure(figsize=(12, 6))

monthly_sales.plot(kind="line")

plt.title("Monthly Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales ($)")
plt.grid(True)

plt.tight_layout()

plt.savefig(
    os.path.join(output_folder, "monthly_sales_trend.png"),
    dpi=300
)

plt.close()

print("Saved: monthly_sales_trend.png")


# ----------------------------------------------------------
# COMPLETED
# ----------------------------------------------------------

print("\n" + "=" * 70)
print("VISUALIZATION COMPLETED")
print("=" * 70)

print("\nCharts saved inside:")
print("visualizations\\")

print("\nCreated charts:")

print("- sales_by_product.png")
print("- sales_by_country.png")
print("- sales_by_segment.png")
print("- sales_by_year.png")
print("- profit_by_product.png")
print("- monthly_sales_trend.png")

print("\n" + "=" * 70)