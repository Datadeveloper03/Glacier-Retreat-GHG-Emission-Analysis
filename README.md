

# 🌍 **Glacier Retreat Prediction, GHG Emission Forecasting, and Filter Recommendation with Interactive Visualization**

### 🚀 **Project Description**
This project uses **Machine Learning (ML)** models to predict glacier retreat, forecast greenhouse gas (GHG) emissions due to melting glaciers, and recommend suitable filters to reduce emissions. The solution includes **interactive visualizations** using Streamlit, allowing users to explore predictions, filters, and trends with dynamic charts.

---

## 📊 **Features**
✅ **Glacier Retreat Prediction:**  
- Forecasts future glacier area reduction using time-series ML models.  
- Visualizes retreat trends with line charts.  

✅ **GHG Emission Forecasting:**  
- Uses ML models to estimate **CO₂, CH₄, and N₂O emissions** from melting glaciers.  
- Displays predicted emissions with interactive charts.  

✅ **Filter Recommendation:**  
- Suggests industrial-grade filters based on emission type and volume.  
- Displays **filter efficiency and compatibility** dynamically.  

✅ **Dynamic Visualizations:**  
- Line and bar charts for emissions, filters, and efficiencies.  
- Year-over-year trend visualization.  

✅ **Data Visualization with Streamlit:**  
- Interactive and user-friendly UI.  
- Real-time updates with random variations for realistic projections.  

---

## 📁 **Project Structure**
```
📦 Glacier_Project  
 ┣ 📂 models                      # Trained models for predictions  
 ┃ ┣ 📄 glacier_model.pkl         # Glacier retreat model  
 ┃ ┣ 📄 emissions_model.pkl       # Emission forecasting model  
 ┃ ┣ 📄 filter_classifier.pkl     # Filter recommendation model  
 ┣ 📂 data                        # CSV data files  
 ┃ ┣ 📄 glacier_data.csv          # Glacier retreat data  
 ┃ ┣ 📄 emission_data.csv         # Emission data with year and GHG types  
 ┃ ┣ 📄 filter_data_corrected.csv # Filter data with efficiency and year  
 ┣ 📂 glacier_env                 # Python virtual environment  
 ┣ 📄 app.py                      # Streamlit web app  
 ┣ 📄 glacier_retreat.py          # Glacier prediction script  
 ┣ 📄 emissions_forecasting.py    # Emission forecasting script  
 ┣ 📄 filters_recommendation.py   # Filter recommendation script  
 ┣ 📄 requirements.txt            # Project dependencies  
 ┣ 📄 README.md                   # Project documentation  
```

---

## ⚙️ **Setup and Installation**

### ✅ **1. Clone the Repository**
```bash
git clone <repository_url>
cd Glacier_Project
```

### ✅ **2. Create and Activate the Virtual Environment**
```bash
# Create virtual environment
python -m venv glacier_env

# Activate (Windows)
glacier_env\Scripts\activate

# Activate (Linux/Mac)
source glacier_env/bin/activate
```

### ✅ **3. Install Required Dependencies**
```bash
pip install -r requirements.txt
```

---

## 🚀 **How to Run the Project**

### ✅ **1. Launch the Streamlit App**
Run the following command:
```bash
streamlit run app.py
```

### ✅ **2. View the Web App**
After running the Streamlit app, you can view it in your browser:
```
http://localhost:8501
```

---

## 📊 **Data Files**

### 1. **glacier_data.csv**
- Contains glacier area, temperature rise, and precipitation data over years.
- Used for predicting **glacier retreat**.

### 2. **emission_data.csv**
- Includes **GHG emission volume** by year.
- Used for forecasting emissions.

### 3. **filter_data_corrected.csv**
- Contains **filter efficiency** for different emission types and years.
- Used for filter recommendation visualization.

---

## 🔥 **Technologies Used**
- **Python:** Programming language  
- **Streamlit:** Interactive web interface  
- **pandas, numpy:** Data processing and manipulation  
- **scikit-learn, XGBoost:** ML models  
- **matplotlib, seaborn, plotly:** Data visualization  
- **joblib:** Model persistence  
- **CSV:** Data storage format  

---

## 📊 **Model Details**

### 1. **Glacier Retreat Prediction**
- **Input Features:** Year, temperature rise, precipitation  
- **Model:** RandomForestRegressor  
- **Output:** Predicted glacier area over time  

### 2. **Emission Forecasting**
- **Input Features:** Glacier melt volume, temperature rise  
- **Model:** XGBoost Regressor  
- **Output:** Predicted GHG emissions in tons/year  

### 3. **Filter Recommendation**
- **Input Features:** Emission type, volume, efficiency  
- **Model:** RandomForestClassifier  
- **Output:** Recommended filter type  

---

## 📈 **Visualization Components**

### ✅ **1. Glacier Retreat Visualization**
- **Line Chart:**  
    - Glacier area over years  
    - Trends of retreat over time  

### ✅ **2. Emission Forecasting**
- **Line Chart:**  
    - Emission trends by year  
    - CO₂, CH₄, and N₂O emissions  

### ✅ **3. Filter Recommendation**
- **Bar Chart:**  
    - Filter efficiency by type  
    - Random variations in efficiency and volume for realism  

---

## 🔥 **Future Enhancements**
- **More Visualizations:**  
    - Correlation between GHG emissions and temperature rise.  
    - Additional filters with detailed descriptions.  
- **Model Optimization:**  
    - Use **LSTM or Prophet** for better time-series predictions.  
- **Real-Time Data:**  
    - Integration with real-time APIs for **live climate data**.

---

## 🚀 **Usage Instructions**
1. Select the **emission type** in the dropdown.  
2. View the **predicted GHG emissions** dynamically.  
3. See the **recommended filter** with efficiency and volume.  
4. Explore the **glacier retreat and emission trends** over time.  
5. Interact with the **visualizations** to analyze the impact.  

---

## 🔥 **Contributing**
Contributions are welcome!  
To contribute:  
1. Fork the repository  
2. Create a new branch  
3. Make your changes  
4. Create a pull request  
