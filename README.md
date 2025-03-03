# Stock Market Prediction App

## 📌 Project Overview  
Stock market price prediction is a challenging problem due to the volatile nature of financial markets. Traditional statistical methods often fail to capture hidden patterns in stock price movements. This project aims to build a **machine learning-based stock price prediction system** that takes historical stock market data, processes it, and forecasts future prices using a **Random Forest Regressor**.

## 🚀 Problem Statement  
**How can we predict future stock prices based on historical data?**  
Many investors and traders struggle with making informed decisions due to market volatility. This project helps users analyze stock trends and make data-driven predictions using machine learning.

## 🎯 Solution  
This project provides:  
✅ **Data Preprocessing** – Cleans raw stock market data (Date, Open, High, Low, Close, Volume).  
✅ **Feature Engineering** – Extracts meaningful features for model training.  
✅ **Model Training & Prediction** – Uses **Random Forest Regressor** to train and predict stock prices.  
✅ **Visualization** – Displays actual vs. predicted prices using interactive graphs.  
✅ **Future Price Forecasting** – Allows users to input a time range (days) to forecast future prices.

---

## 🏗️ Tech Stack  
- **Python**
- **Streamlit** (for UI)
- **pandas, numpy** (for data handling)
- **scikit-learn** (for machine learning)
- **matplotlib** (for visualization)
- **yfinance** (for fetching stock data)

---

## 🤖 Machine Learning Model  
The project utilizes a **Random Forest Regressor**, which is an ensemble learning method that builds multiple decision trees and merges their outputs to improve accuracy and reduce overfitting.  

- **Algorithm**: Random Forest Regression  
- **Advantages**:
  - Works well with nonlinear data  
  - Reduces overfitting compared to a single decision tree
  - Handles missing and unstructured data efficiently  


# 🔧 Installation & Setup  
 
# 1️⃣ Clone the Repository

```sh
git clone https://github.com/Jayakrishna2b/stock-market-prediction.git
```

📂 Navigate into the Project Directory  
After cloning, move into the project folder:  
```sh
cd stock-market-prediction
```

# 2️⃣ Create a Virtual Environment (Recommended)
```sh
python -m venv venv
```
```sh
source venv/bin/activate 
```

 On Windows use:
 ```sh
venv\Scripts\activate
```

# 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

# 4️⃣ Run the Application
```sh
streamlit run app.py
```

# 📊 Expected CSV Format
The CSV file should contain at least the following columns : Date, Open, High, Low, Close, Volume
Date: Must be in YYYY-MM-DD format.
Close: The target column for prediction.

# 📈 Model Evaluation Metrics
To measure model performance, the following evaluation metrics are used:

Mean Absolute Error (MAE) – Measures the average absolute difference between predicted and actual prices.
Mean Squared Error (MSE) – Penalizes larger errors more heavily than MAE.

# 🛠️ Debugging Issues
If dependencies are missing, run:
```sh
pip install -r requirements.txt
```
 If streamlit is not found, activate the virtual environment and retry.


