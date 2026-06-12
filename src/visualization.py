import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv(
    "data/processed/books/books_clean.csv"
)

# Sort by price
top_books = df.sort_values(
    by="price",
    ascending=False
).head(10)

# Create figure
plt.figure(figsize=(10, 6))

# Bar chart
plt.bar(
    top_books["title"],
    top_books["price"]
)

# Title and labels
plt.title(
    "Top 10 Most Expensive Books"
)

plt.xlabel(
    "Book Title"
)

plt.ylabel(
    "Price (£)"
)

# Rotate titles
plt.xticks(
    rotation=90
)

plt.tight_layout()

# Save chart
plt.savefig(
    "screenshots/top_10_book_prices.png"
)

print(
    "Top 10 prices chart saved successfully!"
) 