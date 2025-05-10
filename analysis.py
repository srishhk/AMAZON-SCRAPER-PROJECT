import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np

# Load cleaned data
df = pd.read_csv("cleaned_amazon_soft_toys.csv")

# --- Brand Performance Analysis ---

# Top 5 brands by frequency
brand_counts = df["Brand"].value_counts().head(5)
brand_counts.plot(kind="bar", title="Top 5 Brands by Frequency", color='skyblue')
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("top_brands_frequency.png")
plt.clf()

# Average rating by brand (top 5)
avg_ratings = df.groupby("Brand")["Rating"].mean().sort_values(ascending=False).head(5)
avg_ratings.plot(kind="pie", autopct="%1.1f%%", title="Top Brands by Avg Rating")
plt.ylabel("")
plt.tight_layout()
plt.savefig("top_brands_rating_pie.png")
plt.clf()

# --- Price vs Rating Analysis ---

# Scatter plot: Price vs Rating with Linear Regression trendline
sns.scatterplot(data=df, x="Rating", y="Selling Price")
plt.title("Price vs Rating")

# Fit a linear regression model
X = df[["Rating"]].dropna()  # Drop missing values in Rating
y = df["Selling Price"].iloc[X.index]  # Corresponding Selling Price
model = LinearRegression()
model.fit(X, y)
predicted = model.predict(X)

# Plotting the trendline
plt.plot(X, predicted, color='red', linestyle='--', label="Trendline")
plt.legend()

plt.tight_layout()
plt.savefig("scatter_price_rating_with_trendline.png")
plt.clf()

# Average price by rating range
df["Rating Range"] = pd.cut(df["Rating"], bins=[0, 2, 3, 4, 5], labels=["0-2", "2-3", "3-4", "4-5"])
avg_price_by_rating = df.groupby("Rating Range")["Selling Price"].mean()
avg_price_by_rating.plot(kind="bar", title="Avg Price by Rating Range", color='salmon')
plt.ylabel("Price (INR)")
plt.tight_layout()
plt.savefig("avg_price_by_rating.png")
plt.clf()

# --- Review & Rating Distribution ---

# Top 5 by reviews, sorted in descending order
top_reviewed = df.sort_values("Reviews", ascending=False).head(5)
top_reviewed.plot(x="Title", y="Reviews", kind="bar", title="Top 5 Products by Reviews", color='lightgreen')
plt.ylabel("Reviews")
# Add labels to bars
for i, v in enumerate(top_reviewed["Reviews"]):
    plt.text(i, v + 100, str(v), ha='center', color='black')
plt.tight_layout()
plt.savefig("top_reviews.png")
plt.clf()

# Top 5 by rating, sorted in descending order
top_rated = df.sort_values("Rating", ascending=False).head(5)
top_rated.plot(x="Title", y="Rating", kind="bar", title="Top 5 Products by Rating", color='orange')
plt.ylabel("Rating")
# Add labels to bars
for i, v in enumerate(top_rated["Rating"]):
    plt.text(i, v + 0.1, str(round(v, 2)), ha='center', color='black')
plt.tight_layout()
plt.savefig("top_rated.png")
plt.clf()

# --- Highly Rated but Less Reviewed Products ---
# Filter products with high ratings but less than a certain threshold of reviews
threshold_reviews = 1000  # Define threshold based on your analysis
high_rated_low_reviewed = df[(df["Rating"] >= 4.5) & (df["Reviews"] <= threshold_reviews)]
high_rated_low_reviewed = high_rated_low_reviewed.sort_values("Rating", ascending=False).head(5)

# Plot the top 5 high-rated but less-reviewed products
high_rated_low_reviewed.plot(x="Title", y="Rating", kind="bar", title="Top 5 High-Rated but Less-Reviewed Products", color='lightcoral')
plt.ylabel("Rating")
# Add labels to bars
for i, v in enumerate(high_rated_low_reviewed["Rating"]):
    plt.text(i, v + 0.1, str(round(v, 2)), ha='center', color='black')
plt.tight_layout()
plt.savefig("high_rated_low_reviewed.png")
plt.clf()

print("✅ All charts generated and saved successfully.")
