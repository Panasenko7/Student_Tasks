import requests


URL = 'https://open.er-api.com/v6/latest/UAH'

response = requests.get(URL)
response_dict = response.json()
exchange_rates = response_dict['rates']

input_amount_of_money = int(input('Input amount of UAH:'))
currency_list = []

while True:
    input_currency = input(f'Enter the currency you need:')
    if input_currency == '':
        break
    currency_list.append(input_currency.upper())

for currency_name, currency_ratio in exchange_rates.items():
    if currency_name in currency_list:
        total_amount = currency_ratio * input_amount_of_money
        print(f"Currency: {currency_name} - {currency_ratio} - {total_amount}")
    else:
        print('Dont need')




