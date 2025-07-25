import requests
import sys

url = 'https://rest.coincap.io/v3/assets/bitcoin?apiKey='
api_key = '5254489015d1095045c36262af746dc27b548c1537f3579292b5ebd9a8d52630'

api_call = url + api_key
response = requests.get(api_call)
req = response.json().get('data')

try:
    bitcoin_price = float(req['priceUsd']) * float(sys.argv[1])
except IndexError:
    sys.exit('Missing command-line argument')
except ValueError:
    sys.exit('Command-line argument is not a number')
except requests.RequestException:
    pass
else:
    print(f'${round(bitcoin_price, 4):,}')


