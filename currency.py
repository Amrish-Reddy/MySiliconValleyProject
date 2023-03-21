import requests

url = "https://api.exchangerate-api.com/v4/latest/USD"

try:
    response = requests.get(url)
    data = response.json()
except requests.exceptions.RequestException as e:
    print("Error occurred: ", e)
    exit(1)

print("Available currencies:")
print(", ".join(data["rates"].keys()))

source_currency = input("Enter the source currency: ").upper()
target_currency = input("Enter the target currency: ").upper()
amount = float(input("Enter the amount: "))

if source_currency not in data["rates"]:
    print(f"Invalid currency: {source_currency}")
    exit(1)

if target_currency not in data["rates"]:
    print(f"Invalid currency: {target_currency}")
    exit(1)

exchange_rate = data["rates"][target_currency] / data["rates"][source_currency]
converted_amount = amount * exchange_rate

print(f"{amount:.2f} {source_currency} is equal to {converted_amount:.2f} {target_currency}")
