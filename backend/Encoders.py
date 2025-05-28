import pickle
from sklearn.preprocessing import LabelEncoder

# Define categorical columns
categorical_columns = ["City", "Place", "Season"]

# Load dataset to fit label encoders
import pandas as pd
df = pd.read_excel("mercydata.xlsx")  # Use the correct dataset path

# Create and save encoders
label_encoders = {}
for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

with open("models/label_encoders.pkl", "wb") as f:
    pickle.dump(label_encoders, f)

print("Label encoders saved successfully!")
