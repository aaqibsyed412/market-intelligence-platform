import pytest

from collectors.yahoo import download_stock
def test_empty_symbol_raises_value_error():
    with pytest.raises(ValueError):
        download_stock("")
def test_valid_symbol_returns_dataframe():
    data = download_stock("AAPL")

    assert not data.empty
def test_invalid_symbol_raises_value_error():
    with pytest.raises(ValueError):
        download_stock("NOTAREALSTOCK")