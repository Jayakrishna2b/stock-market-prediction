import pandas as pd

def load_data(file):
    return pd.read_csv(file)

def preprocess_data(data):
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    data['Target'] = data['Close'].shift(-1)  # Predict next day's close
    data.dropna(inplace=True)
    return data
