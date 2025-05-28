import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import xgboost as xgb
import joblib

def train_xgboost_model(data_path, model_save_path):
    # Load cleaned data
    df = pd.read_csv(data_path)

    # Feature engineering (example: add month and day as features)
    df['checkin_date'] = pd.to_datetime(df['checkin_date'])
    df['month'] = df['checkin_date'].dt.month
    df['day'] = df['checkin_date'].dt.day

    # Define features (X) and target (y)
    X = df[['month', 'day', 'rating']]  # Add more features as needed
    y = df['price']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train XGBoost model
    model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1, max_depth=5)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    print("Model Evaluation:")
    print(f"Mean Absolute Error (MAE): {mean_absolute_error(y_test, y_pred)}")
    print(f"Mean Squared Error (MSE): {mean_squared_error(y_test, y_pred)}")
    print(f"R² Score: {r2_score(y_test, y_pred)}")

    # Save the trained model
    joblib.dump(model, model_save_path)
    print(f"Model saved to {model_save_path}")

# Example usage
train_xgboost_model('data/processed_data/cleaned_hotels_Nairobi_2024-01-01_2024-01-05.csv', 'ml_models/saved_models/xgboost_model.pkl')