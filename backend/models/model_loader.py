import pickle
import numpy as np
import pandas as pd

# Load label encoders
with open("models/label_encoders.pkl", "rb") as f:
    label_encoders = pickle.load(f)

def load_model():
    with open("models/hotel_price_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

def preprocess_input(input_data):
    """Convert categorical values to numerical using label encoders."""
    input_df = pd.DataFrame([input_data])

    # Encode categorical columns
    for col in ["City", "Place", "Season"]:
        if col in input_df.columns:
            input_df[col] = label_encoders[col].transform([input_df[col][0]])

    return input_df

def predict_price(model, input_data):
    df = preprocess_input(input_data)
    return model.predict(df)[0]
