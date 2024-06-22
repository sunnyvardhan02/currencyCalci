from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'dc28b79b9fff0e0c7011af93'  # Replace with your actual API key

# List of common currencies
CURRENCIES = [
    'USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD',
    'MXN', 'SGD', 'HKD', 'NOK', 'KRW', 'TRY', 'RUB', 'INR', 'BRL', 'ZAR'
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            exchange_rate = data['conversion_rates'][to_currency]
            result = amount * exchange_rate
            return render_template('index.html', currencies=CURRENCIES, result=f"{amount} {from_currency} = {result:.2f} {to_currency}")
    
    return render_template('index.html', currencies=CURRENCIES)

if __name__ == '__main__':
    app.run(debug=True)