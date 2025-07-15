import requests

class CurrencyConverter:
    """
    A class to convert currencies using a real-time exchange rate API.
    """
    def __init__(self):
        """
        Initializes the CurrencyConverter.
        The API used is ExchangeRate-API (https://www.exchangerate-api.com/).
        """
        self.base_url = "https://open.er-api.com/v6/latest/USD"

    def get_exchange_rates(self):
        """
        Retrieves the latest exchange rates from the API.

        Returns:
            dict: A dictionary containing exchange rates if the request is successful,
                  otherwise, returns None.
        """
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            data = response.json()
            return data['rates']
        except requests.exceptions.RequestException as e:
            print(f"Error fetching exchange rates: {e}")
            return None

    def convert(self, amount, from_currency, to_currency):
        """
        Converts an amount from one currency to another.

        Args:
            amount (float): The amount to convert.
            from_currency (str): The source currency code (e.g., 'USD', 'EUR', 'BRL').
            to_currency (str): The target currency code (e.g., 'USD', 'EUR', 'BRL').

        Returns:
            float: The converted amount if successful, otherwise returns None.
        """
        rates = self.get_exchange_rates()
        if not rates:
            return None

        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in rates or to_currency not in rates:
            print("Currency not found. Please check the currency codes.")
            return None

        # Convert to USD first, then to the target currency
        amount_in_usd = amount / rates[from_currency]
        converted_amount = amount_in_usd * rates[to_currency]
        return converted_amount
