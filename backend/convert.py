import xgboost as xgb
import pickle

# Load the old model
with open("models/hotel_price_model.pkl", "rb") as f:
    model = pickle.load(f)

# Save it in JSON format
model.save_model("models/hotel_price_model.json")

print("Model successfully converted to JSON format.")
