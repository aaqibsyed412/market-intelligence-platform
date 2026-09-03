from database.connection import get_connection


def load_stock_data(data, symbol):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        for index, row in data.iterrows():
            stock_date = index.date()
            stock_open = row["Open"]
            stock_high = row["High"]
            stock_low = row["Low"]
            stock_close = row["Close"]
            stock_volume = row["Volume"]

            cursor.execute(
                """
                INSERT INTO stock_prices
                (date, symbol, open, high, low, close, volume)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (date, symbol) DO NOTHING
                """,
                (
                    stock_date,
                    symbol,
                    stock_open,
                    stock_high,
                    stock_low,
                    stock_close,
                    stock_volume,
                ),
            )

        conn.commit()

    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()