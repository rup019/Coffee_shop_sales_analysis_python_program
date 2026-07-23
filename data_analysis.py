import numpy as np
import pandas as pd

coffee = np.array(["Espresso", "Latte", "Cappuccino", "Mocha", "Cold Coffee"])
cups_sold = np.array([120, 95, 150, 80, 110])
price = np.array([120, 180, 160, 200, 150])

# Create the DataFrame
df = pd.DataFrame({
    "Coffee": coffee,
    "Cups Sold": cups_sold,
    "Price": price
})

# Calculate Revenue
df["Revenue"] = df["Cups Sold"] * df["Price"]

# Generate Sales Report
print("\n========== COFFEE SHOP SALES REPORT ==========")
print(df.to_string(index=False))  # Hides the 0,1,2,3 row indices for a cleaner look

# Calculate Metrics safely using pandas
highest_price_val = df["Price"].max()
highest_price_df = df[df["Price"] == highest_price_val]

best_seller_val = df["Cups Sold"].max()
best_seller_df = df[df["Cups Sold"] == best_seller_val]

# Print Summaries
print("\n[Most Sold Coffee]")
for _, row in best_seller_df.iterrows():
    print(f"- {row['Coffee']} ({row['Cups Sold']} cups)")

print("\n[Most Expensive Coffee]")
for _, row in highest_price_df.iterrows():
    print(f"- {row['Coffee']} (₹{row['Price']})")

print(f"\nAverage Coffee Price: ₹{df['Price'].mean():.2f}")
print(f"Total Revenue:        ₹{df['Revenue'].sum():,}")
print("==============================================")
