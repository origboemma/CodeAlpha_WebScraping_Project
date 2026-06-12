import pandas as pd


RAW_FILE = "data/raw/books/books_raw.csv"
import pandas as pd

RAW_FILE = "data/raw/books/books_raw.csv"

CLEAN_FILE = "data/processed/books/books_clean.csv" 


def load_data():
    df = pd.read_csv(RAW_FILE)

    print("Rows:", len(df))
    print("Columns:", len(df.columns))

    return df


def clean_price(df):

    df["price"] = (
        df["price"]
        .str.replace("Â£", "", regex=False)
        .astype(float)
    )

    return df



def clean_rating(df):

    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    df["rating"] = df["rating"].map(rating_map)

    return df

def save_data(df):

    df.to_csv(
        CLEAN_FILE,
        index=False
    )

    print("Clean data saved to", CLEAN_FILE) 



if __name__ == "__main__":

    df = load_data()

    df = clean_price(df)

    df = clean_rating(df)

    save_data(df)

    print(df.head()) 