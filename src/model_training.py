from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import numpy as np

def train_model(features, target):
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    return model

def predict_future_prices(model, last_data, days):
    future_prices = []
    current_data = last_data.copy()

    for _ in range(days):
        next_price = model.predict(current_data.values.reshape(1, -1))[0]
        future_prices.append(next_price)

        # Update current_data for the next prediction
        current_data = current_data.shift(-1)
        current_data.iloc[-1] = next_price  # Set the predicted price as the last value

    return future_prices
