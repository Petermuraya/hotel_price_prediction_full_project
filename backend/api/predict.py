# backend/api/predict.py
from flask import Blueprint, request, jsonify
from models.model_loader import load_model, predict_price

predict_bp = Blueprint("predict", __name__)
model = load_model()

@predict_bp.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        required_features = ["City", "Place", "ReviewsCount", "Rating", "Single_room", "Double_room", "Season"]
        if not all(feature in data for feature in required_features):
            return jsonify({"error": "Missing required features"}), 400
        
        prediction = predict_price(model, data)
        return jsonify({"predicted_price": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 500