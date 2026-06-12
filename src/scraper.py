import requests
from bs4 import BeautifulSoup

from config import BASE_URL, OUTPUT_FILE
from exporter import save_to_csv


def get_page():
    response = requests.get(BASE_URL)

    print("Status Code:", response.status_code)

    return response.text



def parse_page(html):
    soup = BeautifulSoup(html, "html.parser")

    books = soup.find_all(
        "article",
        class_="product_pod"
    )

    print("Number of books found:", len(books))

    books_data = []

    for book in books:
        title = book.h3.a["title"]

        price = book.find(
            "p",
            class_="price_color"
        ).text

        rating = book.find(
            "p",
            class_="star-rating"
        )["class"][1]

        books_data.append({
            "title": title,
            "price": price,
            "rating": rating
        })

    return books_data


if __name__ == "__main__":
    html = get_page()

    books = parse_page(html)

    save_to_csv(
        books,
        OUTPUT_FILE
    )
    
    
    
    