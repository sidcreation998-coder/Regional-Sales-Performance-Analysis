import import pandas as pd
import import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("dataset.csv")

print("===== DATASET PREVIEW =====")
print(data.head())

# Region-wise total sales
region_sales = data.groupby("Region")["Sales"].sum().sort_values(ascending=False)

print("\n===== REGION WISE TOTAL SALES =====")
print(region_sales)

# Category-wise total sales
category_sales = data.groupby("Category")["Sales"].sum().sort_values(ascending=False)

print("\n===== CATEGORY WISE TOTAL SALES =====")
print(category_sales)

# Save region summary
region_sales.to_csv("region_summary.csv")

# Save category summary
category_sales.to_csv("category_summary.csv")

# Plot Region-wise Sales
plt.figure()
region_sales.plot(kind="bar")
plt.title("Region Wise Total Sales")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("region_sales.png")
plt.close()

# Plot Category-wise Sales
plt.figure()
category_sales.plot(kind="bar")
plt.title("Category Wise Total Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("category_sales.png")
plt.close()

print("\nAnalysis Completed Successfully.")
