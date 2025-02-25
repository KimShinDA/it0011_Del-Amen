exchange_rates = {}  # Dictionary to store rates
currency_names = {}  # Dictionary to store currency names

with open("currency.csv", "r", encoding="ISO-8859-1") as file:
    next(file)  
    for line in file:
        parts = line.strip().split(",")  # Split CSV line by comma
        currency_code = parts[0].strip()
        currency_name = parts[1].strip()
        exchange_rate = float(parts[2].strip())

        exchange_rates[currency_code] = exchange_rate
        currency_names[currency_code] = currency_name  

# User input
usd_amount = float(input("How much dollar do you have? "))
target_currency = input("What currency you want to have? ").strip().upper()

# Convert and display result
if target_currency in exchange_rates:
    converted_amount = usd_amount * exchange_rates[target_currency]
    print(f"\nDollar: {usd_amount} USD")
    print(f"{currency_names[target_currency]}: {converted_amount:.6f}") 
else:
    print("Currency not found.")
