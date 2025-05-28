from fastapi import FastAPI
import pickle
import pandas as pd
from pydantic import BaseModel

# Load the trained model
model_path = "best_hotel_price_model.pkl"  # Ensure the model file is in the same directory
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Initialize FastAPI
app = FastAPI(title="Hotel Price Prediction API", version="1.0")

# Define input schema using Pydantic
class HotelInput(BaseModel):
    location: str
    star_rating: int
    season: str
    reviews_count: int
    amenities_score: float

@app.get("/")
def home():
    """Root endpoint to confirm the API is running."""
    return {"message": "Welcome to the Hotel Price Prediction API"}

@app.post("/predict/")
def predict_price(data: HotelInput):
    """Predict hotel price based on input features."""
    try:
        # Convert input to DataFrame
        input_data = pd.DataFrame([data.dict()])

        # Make prediction
        predicted_price = model.predict(input_data)[0]

        return {"predicted_price": round(predicted_price, 2)}
    except Exception as e:
        return {"error": str(e)}

# Run using: uvicorn app:app --host 0.0.0.0 --port 8000 --reload
