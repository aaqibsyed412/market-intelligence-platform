import pytest

from collectors.yahoo import download_stock
from database.connection import get_connection
from database.loader import load_stock_data

@pytest.mark.integration
def test_yahoo_to_database():
    
    symbol = "NVDA"

    # Get real data from Yahoo Finance
    data = download_stock(symbol)

    # Make sure Yahoo actually returned data
    assert not data.empty

    # Load the real data into PostgreSQL
    load_stock_data(data, symbol)

    # Connect to PostgreSQL and verify the latest record
    conn = get_connection()
    cursor = conn.cursor()

    latest_date = data.index[-1].date()
    expected_close = float(data["Close"].iloc[-1])

    cursor.execute(
        """
        SELECT close
        FROM stock_prices
        WHERE date = %s AND symbol = %s
        """,
        (latest_date, symbol),
    )

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    # Make sure PostgreSQL found the record
    assert result is not None

    # Make sure the database value matches Yahoo's value
    assert float(result[0]) == pytest.approx(expected_close)