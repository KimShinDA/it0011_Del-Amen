exchangeRates = {}  # Dictionary to store rates
currencyNames = {}  # Dictionary to store currency names

with open("currency.csv", "r") as file:
    next(file)  
    for line in file:
        parts = line.strip().split(",")  # Split CSV line by comma
        currencyCode = parts[0].strip()
        currencyName = parts[1].strip()
        exchangeRate = float(parts[2].strip())

        exchangeRates[currencyCode] = exchangeRate
        currencyNames[currencyCode] = currencyName  

# User input
usdAmount = float(input("How much dollar do you have? "))
currencyChoice = input("What currency you want to have? ").strip().upper() # Convert to upper case

# Convert and display result
if currencyChoice in exchangeRates:
    convertedAmount = usdAmount * exchangeRates[currencyChoice]
    print(f"\nDollar: {usdAmount} USD")
    print(f"{currencyNames[currencyChoice]}: {convertedAmount:.6f}") 
else:
    print("Currency not found.")
