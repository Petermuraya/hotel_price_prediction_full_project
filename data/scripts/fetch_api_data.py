import requests
import hashlib
import time
import pymongo
import json  # For debugging API responses

# MongoDB Setup
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "hotel_data"
COLLECTION_NAME = "hotels"

# Hotelbeds API Credentials
API_KEY = "21c7bbef603a341ab6e481f748187805"  # Your actual API key
API_SECRET = "3f4b0501e0"  # Your actual API secret

# Generate X-Signature
def generate_signature():
    timestamp = str(int(time.time()))
    raw_signature = API_KEY + API_SECRET + timestamp
    return hashlib.sha256(raw_signature.encode()).hexdigest(), timestamp

# Function to Fetch Hotel Data
def fetch_hotels(destination, checkin, checkout):
    url = "https://api.test.hotelbeds.com/hotel-api/1.0/hotels"

    # Generate correct authentication signature
    signature, _ = generate_signature()

    headers = {
        "Api-Key": API_KEY,
        "X-Signature": signature,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # Properly structured API request body
    payload = {
        "stay": {
            "checkIn": checkin,
            "checkOut": checkout,
            "shiftDays": 1
        },
        "destination": {
            "code": destination
        },
        "occupancies": [{"rooms": 1, "adults": 2, "children": 0}]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()

        # Debugging: Print API response to check structure
        print(json.dumps(data, indent=4))

        # Ensure "hotels" exists in response
        if "hotels" in data and isinstance(data["hotels"], list):
            return data["hotels"]
        else:
            print("Unexpected API response structure. No 'hotels' key found.")
            return []
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return []

# Function to Store Data in MongoDB
def store_in_mongo(data):
    client = pymongo.MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    if data:
        collection.insert_many(data)
        print(f"Stored {len(data)} hotels in MongoDB.")
    else:
        print("No data to store.")

# Example Usage
if __name__ == "__main__":
    destination = "NBO"  # Nairobi
    checkin = "2025-03-01"
    checkout = "2025-03-05"

    hotels_data = fetch_hotels(destination, checkin, checkout)

    if hotels_data:
        formatted_data = []
        for hotel in hotels_data:
            if isinstance(hotel, dict):  # Ensure hotel is a dictionary before accessing keys
                formatted_data.append({
                    "name": hotel.get("name", "N/A"),
                    "location": hotel.get("destinationName", "Nairobi"),
                    "rating": hotel.get("categoryCode", "N/A"),
                    "price": hotel.get("minRate", 0),
                    "amenities": hotel.get("facilities", []),
                    "booking_policy": hotel.get("ratePlans", [])
                })
            else:
                print(f"Unexpected hotel entry format: {hotel}")

        # Store in MongoDB
        store_in_mongo(formatted_data)
    else:
        print("No hotel data retrieved.")
