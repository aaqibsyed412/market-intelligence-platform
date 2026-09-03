from collectors.yahoo import download_stock
from database.loader import load_stock_data
from config.logging_config import configure_logging


def main():
    configure_logging()

    symbols = ["AAPL", "NVDA", "MSFT", "AMZN"]

    for symbol in symbols:
        try:
            data = download_stock(symbol)
            load_stock_data(data, symbol)

            print(f"Successfully loaded {len(data)} records for {symbol}.")

        except ValueError as error:
            print(f"Error loading {symbol}: {error}")


if __name__ == "__main__":
    main()