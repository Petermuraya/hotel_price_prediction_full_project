import pandas as pd
import numpy as np

def clean_hotel_data(raw_data_path, processed_data_path):
    df = pd.read_csv(raw_data_path)

    # Remove rows with missing prices
    df = df.dropna(subset=['price'])

    # Convert price to numeric (remove currency symbols)
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

    # Save cleaned data
    df.to_csv(processed_data_path, index=False)
    print(f"Cleaned data saved to {processed_data_path}")

# Example usage
clean_hotel_data('data/raw_data/hotels_Nairobi_2024-01-01_2024-01-05.csv', 'data/processed_data/cleaned_hotels_Nairobi_2024-01-01_2024-01-05.csv')