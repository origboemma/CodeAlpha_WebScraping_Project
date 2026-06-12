import pandas as pd


def save_to_csv(data, output_file):
    df = pd.DataFrame(data)

    df.to_csv(
        output_file,
        index=False,
        encoding="utf-8"
    )

    print(f"Data saved to {output_file}")