from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'dc28b79b9fff0e0c7011af93'  # Replace with your actual API key

# List of common currencies with their codes
CURRENCIES = [
    ('USD', 'United States Dollar'),
    ('EUR', 'Euro (Eurozone)'),
    ('JPY', 'Japanese Yen'),
    ('GBP', 'British Pound Sterling'),
    ('AUD', 'Australian Dollar'),
    ('CAD', 'Canadian Dollar'),
    ('CHF', 'Swiss Franc'),
    ('CNY', 'Chinese Yuan'),
    ('SEK', 'Swedish Krona'),
    ('NZD', 'New Zealand Dollar'),
    ('MXN', 'Mexican Peso'),
    ('SGD', 'Singapore Dollar'),
    ('HKD', 'Hong Kong Dollar'),
    ('NOK', 'Norwegian Krone'),
    ('KRW', 'South Korean Won'),
    ('TRY', 'Turkish Lira'),
    ('RUB', 'Russian Ruble'),
    ('INR', 'Indian Rupee'),
    ('BRL', 'Brazilian Real'),
    ('ZAR', 'South African Rand'),
    ('AED', 'United Arab Emirates Dirham'),
    ('ARS', 'Argentine Peso'),
    ('CLP', 'Chilean Peso'),
    ('EGP', 'Egyptian Pound'),
    ('ILS', 'Israeli New Shekel'),
    ('IDR', 'Indonesian Rupiah'),
    ('MYR', 'Malaysian Ringgit'),
    ('PHP', 'Philippine Peso'),
    ('THB', 'Thai Baht'),
    ('VND', 'Vietnamese Dong')
]


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error_message = None
    if request.method == 'POST':
        amount = float(request.form['amount'])
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            exchange_rate = data['conversion_rates'].get(to_currency)
            if exchange_rate:
                result = f"{amount} {from_currency} = {amount * exchange_rate:.2f} {to_currency}"
            else:
                error_message = f"Conversion rate for {to_currency} not found."
        else:
            error_message = "Error fetching exchange rate data."
    
    return render_template('index.html', currencies=CURRENCIES, result=result, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
