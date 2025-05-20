import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the sales data
try:
	data = pd.read_csv('sales_data.csv')
	if data.empty:
		raise ValueError("The file 'sales_data.csv' is empty.")
except FileNotFoundError:
	print("Error: The file 'sales_data.csv' was not found.")
	exit()
except ValueError as e:
	print(f"Error: {e}")
	exit()

# Display the first few rows
print("First 5 rows:\n", data.head())

# Data Cleaning
# Drop any missing values
data.dropna(inplace=True)

# Convert 'Date' to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Extract month and year for analysis
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year

# Calculate Total Sales per Product
sales_per_product = data.groupby('Product')['Sales'].sum().reset_index()
print("Sales per Product:\n", sales_per_product)

# Calculate Monthly Sales
monthly_sales = data.groupby(['Year', 'Month'])['Sales'].sum().reset_index()
print("Monthly Sales:\n", monthly_sales)

# Identify Top-Selling Product
top_selling_product = sales_per_product.loc[sales_per_product['Sales'].idxmax()]
print("Top-Selling Product:\n", top_selling_product)

# Visualization
plt.figure(figsize=(10, 6))
plt.bar(sales_per_product['Product'], sales_per_product['Sales'], color='skyblue')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.title('Sales per Product')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot Monthly Sales
plt.figure(figsize=(10 , 6))
plt.plot(monthly_sales['Month'], monthly_sales['Sales'], marker='o', linestyle='-', color='blue')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Trend')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
