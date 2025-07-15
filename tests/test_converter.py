import pytest
from unittest.mock import patch
import requests
from src.converter import CurrencyConverter

@pytest.fixture
def converter():
    return CurrencyConverter()

@patch("requests.get")
def test_get_exchange_rates_success(mock, converter):
    mock.return_value.raise_for_status.return_value = None
    mock.return_value.json.return_value = {"rates": {"USD": 1.0, "EUR": 0.85, "BRL": 5.0}}

    rates = converter.get_exchange_rates()
    assert rates == {"USD": 1.0, "EUR": 0.85, "BRL": 5.0}
    mock.assert_called_once_with("https://open.er-api.com/v6/latest/USD")

@patch("requests.get")
def test_get_exchange_rates_failure(mock, converter):
    mock.return_value.raise_for_status.side_effect = requests.exceptions.RequestException("Erro de conexão")

    rates = converter.get_exchange_rates()
    assert rates is None

@patch("src.converter.CurrencyConverter.get_exchange_rates")
def test_convert_success(mock, converter):
    mock.return_value = {"USD": 1.0, "EUR": 0.85, "BRL": 5.0}

    converted_amount = converter.convert(10, "USD", "BRL")
    assert converted_amount == 50.0

    converted_amount = converter.convert(10, "BRL", "USD")
    assert converted_amount == 2.0

    converted_amount = converter.convert(10, "EUR", "BRL")
    assert converted_amount == pytest.approx(58.82, rel=1e-2)

@patch("src.converter.CurrencyConverter.get_exchange_rates")
def test_convert_invalid_currency(mock, converter):
    mock.return_value = {"USD": 1.0, "EUR": 0.85, "BRL": 5.0}

    converted_amount = converter.convert(10, "XYZ", "BRL")
    assert converted_amount is None

@patch("src.converter.CurrencyConverter.get_exchange_rates")
def test_convert_api_failure(mock, converter):
    mock.return_value = None

    converted_amount = converter.convert(10, "USD", "BRL")
    assert converted_amount is None


