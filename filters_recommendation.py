import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# ✅ Load the corrected CSV
data = pd.read_csv('data/filter_data.csv')

# ✅ Error handling for missing columns
required_columns = {'emission_type', 'emission_volume', 'recommended_filter', 'efficiency'}
if not required_columns.issubset(data.columns):
    missing = required_columns - set(data.columns)
    raise ValueError(f"Missing columns in CSV: {missing}")

# ✅ Model input features (X) and target variable (y)
X = data[['emission_type', 'emission_volume', 'efficiency']]
y = data['recommended_filter']

# ✅ One-hot encoding for categorical features
X = pd.get_dummies(X, columns=['emission_type'], drop_first=True)

# ✅ Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Initialize and train the RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ✅ Make predictions
y_pred = model.predict(X_test)

# ✅ Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2%}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ✅ Save the model in the models directory
joblib.dump(model, 'models/filter_classifier.pkl')

print("\n✅ Filter Recommendation Model Saved Successfully in 'models/filter_classifier.pkl'")
