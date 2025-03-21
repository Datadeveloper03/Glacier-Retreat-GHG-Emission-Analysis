import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
data = pd.read_csv("data/glacier_data.csv")

# Features and target
X = data[['year', 'avg_temp', 'precipitation']]
y = data['glacier_area']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'models/glacier_model.pkl')

print("✅ Glacier Prediction Model Trained and Saved.")
