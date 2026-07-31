import logging
import yfinance as yf

logger = logging.getLogger(__name__)

def download_stock(symbol: str):
    """
    Download one month of historical stock data.

    Args:
        symbol: Stock ticker (e.g. AAPL)

    Returns:
        Pandas DataFrame containing historical prices.
    """

    symbol = symbol.strip().upper()
    logger.info(f"Downloading stock data for ticker: {symbol}")

    if not symbol:
        raise ValueError("Stock symbol cannot be empty.")

    try :
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1mo")
    except Exception as error:
        logger.exception(
            f"Failed to retrieve stock data for ticker: {symbol}"
        )
        raise RuntimeError(
            "Unable to retrieve stock data from Yahoo Finance"
        ) from error

    if data.empty:
        raise ValueError(f"No historical data found for ticker '{symbol}'.")
    logger.info(
            f"Successfully retrieved {len(data)} records for ticker: {symbol}")
    return data