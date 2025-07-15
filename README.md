# 🌐 Real-Time Currency Converter

![GitHub repo size](https://img.shields.io/github/repo-size/alexandrekatsuura/python-currency-converter?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/alexandrekatsuura/python-currency-converter?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/alexandrekatsuura/python-currency-converter?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/alexandrekatsuura/python-currency-converter?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/alexandrekatsuura/python-currency-converter?style=for-the-badge)

## 📚 Academic Use Disclaimer

> ⚠️ This is an academic project created solely for educational purposes.  
> It is not intended for production use or real-world financial applications.

## ℹ️ About
This project is a simple yet robust currency converter that uses an external API to fetch real-time exchange rates. Developed in Python, it provides a command-line interface (CLI) for quick and accurate conversions. The main goal of this project is to demonstrate skills in Python development, API consumption, unit testing, and documentation best practices.

## 🚀 Features

- **Real-Time Currency Conversion**: Fetches the latest exchange rates from the [ExchangeRate-API](https://www.exchangerate-api.com/).
- **Command-Line Interface (CLI)**: Allows the user to input the amount, source currency, and target currency directly via the terminal.
- **Error Handling**: Includes handling for API failures and invalid user inputs.
- **Unit Testing**: Test coverage using `pytest` to ensure reliability of the request and conversion functions.
- **Clean Project Structure**: Code organized into modules and directories to support maintainability and scalability.

## 🛠️ Technologies Used

- **Python 3.x**
- **`requests`**: To perform HTTP requests to the exchange rate API.
- **`pytest`**: Framework for writing and running unit tests.

## ⚙️ How to Run the Project

### Prerequisites

Make sure you have Python 3.x installed on your machine.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/alexandrekatsuura/python-currency-converter
   cd currency-converter-project
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv .venv
   source venv/bin/activate  # On Linux/macOS
   # venv\Scripts\activate    # On Windows
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

   To start the currency converter, run the following command in the terminal:

   ```bash
   python src/main.py
   ```

   Follow the on-screen instructions to enter the amount and the source/target currencies.

## ✅ Running the Tests

To run the unit tests, make sure you are in the project root directory (`currency-converter-project`) and execute:

```bash
pytest -v
```

This will run all tests defined in the `tests/` directory and show the results.

## 📁 Project Structure
```bash
currency-converter-project/
├── src/
│   └── main.py             # Main logic for execution
│   └── converter.py        # logic for currency conversion
├── tests/
│   └── test_converter.py   # Unit tests for the converter
├── .gitignore              # Git ignore rules
├── README.md               # Project documentation
└── requirements.txt        # Project dependencies
```

## 📄 License

This project is licensed under the [MIT License](LICENSE).
