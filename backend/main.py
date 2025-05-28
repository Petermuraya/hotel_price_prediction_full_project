from fastapi import FastAPI, HTTPException
import pickle
import numpy as np
from pydantic import BaseModel
import ssl
import os

# Fix for missing SSL module in some environments
ssl._create_default_https_context = ssl._create_unverified_context

# Define the model path
MODEL_PATH = "hotel_price_predictor.pkl"

# Check if the model file exists and handle the error gracefully
if not os.path.exists(MODEL_PATH):
    print(f"Warning: Model file '{MODEL_PATH}' not found. Ensure the model is uploaded.")
    model = None
    scaler = None
    encoders = None
else:
    # Load the trained model and preprocessing tools
    with open(MODEL_PATH, "rb") as file:
        data = pickle.load(file)
        model = data.get("model")
        scaler = data.get("scaler")
        encoders = data.get("encoders")

        if not model or not scaler or not encoders:
            raise ValueError("Model file is missing required components.")

# Initialize FastAPI app
app = FastAPI()

# Define request model
class HotelInput(BaseModel):
    country: str
    reviews_count: int
    rating: float
    single_room: int
    double_room: int
    season: str
    tourist_demand_level: str
    major_event: str
    hotel_category: str
    room_occupancy_rate: float
    economic_impact: str
    local_event_impact: str

# Preprocessing function
def preprocess_input(data: HotelInput):
    if model is None or scaler is None or encoders is None:
        raise HTTPException(status_code=500, detail="Model not available. Please upload the model file.")
    
    try:
        features = [
            encoders["country"].transform([data.country])[0],
            data.reviews_count,
            data.rating,
            data.single_room,
            data.double_room,
            encoders["Season"].transform([data.season])[0],
            encoders["Tourist Demand Level"].transform([data.tourist_demand_level])[0],
            encoders["Major Event"].transform([data.major_event])[0],
            encoders["Hotel Category"].transform([data.hotel_category])[0],
            data.room_occupancy_rate,
            encoders["Economic Impact"].transform([data.economic_impact])[0],
            encoders["Local Event Impact"].transform([data.local_event_impact])[0]
        ]
        return scaler.transform([features])
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Invalid category value: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Preprocessing error: {str(e)}")

# Prediction endpoint
@app.post("/predict")
def predict_price(input_data: HotelInput):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not available. Please upload the model file.")
    
    processed_input = preprocess_input(input_data)
    prediction = model.predict(processed_input)[0]
    return {"predicted_price_usd": round(prediction, 2)}
