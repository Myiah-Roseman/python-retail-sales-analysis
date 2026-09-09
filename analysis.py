"""
Retail Sales Analysis
Author: Myiah Roseman

Portfolio project using a synthetic retail dataset.
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_PATH = Path("retail_sales.csv")
CHARTS_DIR = Path("charts")
CHARTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

# -----------------------------
# 1. Data cleaning
# -----------------------------
df["order_date"] = pd.to_datetime(df["order_date"])
df["region"] = df["region"].fillna("Unknown")
df["customer_id"] = df["customer_id"].fillna("Guest")

# Recalculate key metrics to validate the source columns
df["calculated_revenue"] = (
    df["quantity"] * df["unit_price"] * (1 - df["discount_pct"])
).round(2)

df["calculated_profit"] = (
    df["calculated_revenue"] - (df["quantity"] * df["unit_cost"])
).round(2)

# -----------------------------
# 2. KPI summary
# -----------------------------
total_revenue = df["revenue"].sum()
total_profit = df["profit"].sum()
average_order_value = df.groupby("order_id")["revenue"].sum().mean()
profit_margin = total_profit / total_revenue

print("KPI SUMMARY")
print(f"Total revenue: ${total_revenue:,.2f}")
print(f"Total profit: ${total_profit:,.2f}")
print(f"Average order value: ${average_order_value:,.2f}")
print(f"Overall profit margin: {profit_margin:.1%}")

# -----------------------------
# 3. Monthly performance
# -----------------------------
df["month"] = df["order_date"].dt.to_period("M").astype(str)

monthly_revenue = (
    df.groupby("month", as_index=False)["revenue"]
      .sum()
      .sort_values("month")
)

print("\nMONTHLY REVENUE")
print(monthly_revenue)

plt.figure(figsize=(9, 5))
plt.plot(monthly_revenue["month"], monthly_revenue["revenue"], marker="o")
plt.xticks(rotation=45, ha="right")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig(CHARTS_DIR / "monthly_revenue.png", dpi=160)
plt.close()

# -----------------------------
# 4. Category performance
# -----------------------------
category_performance = (
    df.groupby("category", as_index=False)
      .agg(
          revenue=("revenue", "sum"),
          profit=("profit", "sum"),
          units_sold=("quantity", "sum")
      )
)

category_performance["profit_margin"] = (
    category_performance["profit"] / category_performance["revenue"]
)

category_performance = category_performance.sort_values(
    "revenue", ascending=False
)

print("\nCATEGORY PERFORMANCE")
print(category_performance)

plt.figure(figsize=(7, 5))
plt.bar(category_performance["category"], category_performance["revenue"])
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig(CHARTS_DIR / "category_revenue.png", dpi=160)
plt.close()

# -----------------------------
# 5. Regional sales
# -----------------------------
regional_sales = (
    df.groupby("region", as_index=False)["revenue"]
      .sum()
      .sort_values("revenue", ascending=False)
)

print("\nREGIONAL SALES")
print(regional_sales)

plt.figure(figsize=(7, 5))
plt.bar(regional_sales["region"], regional_sales["revenue"])
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig(CHARTS_DIR / "regional_revenue.png", dpi=160)
plt.close()

# -----------------------------
# 6. Product performance
# -----------------------------
product_performance = (
    df.groupby("product", as_index=False)
      .agg(
          units_sold=("quantity", "sum"),
          revenue=("revenue", "sum"),
          profit=("profit", "sum")
      )
      .sort_values("revenue", ascending=False)
)

print("\nTOP PRODUCTS")
print(product_performance.head(10))

# -----------------------------
# 7. Customer behavior
# -----------------------------
customer_summary = (
    df.groupby("customer_id", as_index=False)
      .agg(
          orders=("order_id", "nunique"),
          revenue=("revenue", "sum")
      )
)

known_customers = customer_summary[customer_summary["customer_id"] != "Guest"]
repeat_customers = known_customers[known_customers["orders"] > 1]
repeat_customer_rate = len(repeat_customers) / len(known_customers)

print(f"\nRepeat customer rate: {repeat_customer_rate:.1%}")
print("\nTop customers by revenue:")
print(
    known_customers.sort_values("revenue", ascending=False).head(10)
)

# -----------------------------
# 8. Business takeaways
# -----------------------------
best_month = monthly_revenue.loc[monthly_revenue["revenue"].idxmax()]
best_category = category_performance.iloc[0]
best_region = regional_sales.iloc[0]
best_product = product_performance.iloc[0]

print("\nBUSINESS TAKEAWAYS")
print(f"Highest-revenue month: {best_month['month']} (${best_month['revenue']:,.2f})")
print(f"Top category: {best_category['category']} (${best_category['revenue']:,.2f})")
print(f"Top region: {best_region['region']} (${best_region['revenue']:,.2f})")
print(f"Top product: {best_product['product']} (${best_product['revenue']:,.2f})")
