import requests
from bs4 import BeautifulSoup
import csv

# Yahoo Finance URL for McDonald's (MCD) stock
stock_symbol = "MCD"
url = f"https://finance.yahoo.com/quote/{stock_symbol}/"

# Headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# Send request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract stock price
    price_element = soup.find("fin-streamer", {"data-field": "regularMarketPrice"})
    price = price_element.text if price_element else "N/A"

    # Extract price change
    change_element = soup.find("fin-streamer", {"data-field": "regularMarketChange"})
    change = change_element.text if change_element else "N/A"

    # Extract percentage change
    percent_change_element = soup.find("fin-streamer", {"data-field": "regularMarketChangePercent"})
    percent_change = percent_change_element.text if percent_change_element else "N/A"

    # Print results
    print(f"🔹 Stock: {stock_symbol}")
    print(f"💰 Price: ${price}")
    print(f"📉 Change: {change} ({percent_change}%)")

    # Save data to CSV
    filename = "mcd_stock_data.csv"
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock Symbol", "Price", "Change", "Percentage Change"])
        writer.writerow([stock_symbol, price, change, percent_change])

    print(f"✅ Data saved to {filename}")

else:
    print(f"❌ Failed to fetch data. Status Code: {response.status_code}")
    
import csv

filename = "mcd_stock_data.csv"

# Read and display data from the CSV file
with open(filename, mode="r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)