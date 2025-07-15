from converter import CurrencyConverter

class Main:
    def __init__(self):
        self._converter = CurrencyConverter()
        
    def run(self):
        print("\n--- Currency Converter ---")
        try:
            amount = float(input("Enter the amount to convert: "))
            from_currency = input("From currency (e.g., USD, EUR, BRL): ").upper()
            to_currency = input("To currency (e.g., USD, EUR, BRL): ").upper()

            converted_value = self._converter.convert(amount, from_currency, to_currency)

            if converted_value is not None:
                print(f"{amount} {from_currency} is equal to {converted_value:.2f} {to_currency}")

        except ValueError:
            print("Invalid amount. Please enter a number.")

if __name__ == "__main__":
    main = Main()
    main.run()