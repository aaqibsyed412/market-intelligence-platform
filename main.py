from collectors.yahoo import download_stock
from config.logging_config import configure_logging 

def main():
    configure_logging()
    try:
        data = download_stock("AAPL")
        print(data)

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()