import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from src.data_preprocessing import load_data, preprocess_data
from src.feature_engineering import create_features
from src.model_training import train_model, predict_future_prices
from src.model_evaluation import evaluate_model

def main():
    st.title("Stock Price Prediction App")
    
    # Upload CSV file
    uploaded_file = st.file_uploader("Upload your stock data CSV", type=["csv"])
    
    if uploaded_file is not None:
        data = load_data(uploaded_file)
        st.write("Data Preview:", data.head())
        
        # Preprocess data
        processed_data = preprocess_data(data)
        
        # Create features
        features, target = create_features(processed_data)
        
        # Train the model
        model = train_model(features, target)
        
        # Make predictions
        predictions = model.predict(features)
        
        # Compare predicted vs actual prices
        st.subheader("Predicted vs Actual Prices")
        comparison_df = pd.DataFrame({'Actual': target, 'Predicted': predictions})
        st.line_chart(comparison_df)
        
        # Evaluate the model
        metrics = evaluate_model(model, features, target)
        st.write("Model Evaluation Metrics:", metrics)

        # Future Predictions
        st.subheader("Future Price Predictions")
        days = st.number_input("Enter number of days to predict:", min_value=1, max_value=30, value=5)
        
        if st.button("Predict Future Prices"):
            last_data = features.iloc[-1]  # Get the last row of features
            future_prices = predict_future_prices(model, last_data, days)
            future_dates = pd.date_range(start=processed_data.index[-1] + pd.Timedelta(days=1), periods=days)
            future_df = pd.DataFrame({'Date': future_dates, 'Predicted Price': future_prices})
            st.write(future_df)

if __name__ == "__main__":
    main()
