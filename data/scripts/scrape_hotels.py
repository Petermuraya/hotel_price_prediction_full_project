import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define Wikipedia URL for Uganda hotels
url = "https://en.wikipedia.org/wiki/List_of_hotels_in_Uganda"

def scrape_wikipedia_hotels(url, country):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    hotels = []
    tables = soup.find_all("table", {"class": "wikitable"})
    
    for table in tables:
        rows = table.find_all("tr")[1:]  # Skip header
        for row in rows:
            columns = row.find_all("td")
            if len(columns) > 0:
                hotel_name = columns[0].text.strip()
                location = columns[1].text.strip() if len(columns) > 1 else "Unknown"
                hotels.append({"Hotel Name": hotel_name, "Location": location, "Country": country})
    
    return hotels

# Scrape Uganda hotels from Wikipedia
uganda_hotels = scrape_wikipedia_hotels(url, "Uganda")

# Convert to DataFrame
df_uganda_hotels = pd.DataFrame(uganda_hotels)

# Save to Excel
df_uganda_hotels.to_excel("uganda_hotels.xlsx", index=False)

print("Scraping complete! Data saved to uganda_hotels.xlsx")
     