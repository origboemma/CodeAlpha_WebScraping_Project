import pandas as pd


def analyze_data():
    # Load cleaned data
    df = pd.read_csv(
        "data/processed/books/books_clean.csv"
    )

    # Basic information
    print("ROWS:", len(df))
    print()

    # Average price
    print("AVERAGE PRICE:")
    print(df["price"].mean())
    print()

    # Highest price
    print("HIGHEST PRICE:")
    print(df["price"].max())
    print()

    # Lowest price
    print("LOWEST PRICE:")
    print(df["price"].min())
    print()

    # Most expensive book
    highest_book = df.loc[
        df["price"].idxmax()
    ]

    print("MOST EXPENSIVE BOOK")
    print(highest_book)
    print()

    # Cheapest book
    lowest_book = df.loc[
        df["price"].idxmin()
    ]

    print("CHEAPEST BOOK")
    print(lowest_book)
    print()

    # Rating distribution
    print("RATING DISTRIBUTION")
    print(
        df["rating"].value_counts()
    )
    print()

    # Summary report
    print("SUMMARY REPORT")
    print(
        df.describe()
    )
    print()

    # Top 5 most expensive books
    print("TOP 5 MOST EXPENSIVE BOOKS")

    top_5_expensive = df.sort_values(
        by="price",
        ascending=False
    )

    print(
        top_5_expensive[
            ["title", "price", "rating"]
        ].head(5)
    )
    print()

    # Top 5 cheapest books
    print("TOP 5 CHEAPEST BOOKS")

    top_5_cheapest = df.sort_values(
        by="price",
        ascending=True
    )

    print(
        top_5_cheapest[
            ["title", "price", "rating"]
        ].head(5)
    )
    print()
    
    print("AVERAGE PRICE BY RATING")

    average_price_by_rating = (
        df.groupby("rating")["price"]
        .mean()
    )

    print(
        average_price_by_rating
    )
    print()
    
    
    print("NUMBER OF BOOKS BY RATING")

    books_per_rating = (
        df.groupby("rating")
        .size()
    )

    print(
        books_per_rating
    )
    print()


if __name__ == "__main__":
    analyze_data()  