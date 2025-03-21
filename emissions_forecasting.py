import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import joblib

# Load emissions data
data = pd.read_csv("data/emissions_data.csv")

# Features and target
X = data[['melt_volume', 'temp_rise']]
y = data['emissions_tons']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost Model
model = XGBRegressor(n_estimators=100, learning_rate=0.1)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'models/emission_model.pkl')

print("✅ Emission Forecasting Model Trained and Saved.")
