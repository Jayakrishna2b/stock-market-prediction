from sklearn.metrics import mean_absolute_error, mean_squared_error

def evaluate_model(model, features, target):
    predictions = model.predict(features)
    mae = mean_absolute_error(target, predictions)
    mse = mean_squared_error(target, predictions)
    return {'MAE': mae, 'MSE': mse}
