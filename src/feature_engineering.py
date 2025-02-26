def create_features(data):
    features = data[['Open', 'High', 'Low', 'Close', 'Volume']]
    target = data['Target']
    return features, target
