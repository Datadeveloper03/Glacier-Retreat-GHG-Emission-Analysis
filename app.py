import streamlit as st
import pandas as pd
import joblib
import random

# Load models
glacier_model = joblib.load('models/glacier_model.pkl')
emission_model = joblib.load('models/emission_model.pkl')
filter_model = joblib.load('models/filter_classifier.pkl')

# Set Streamlit page config
st.set_page_config(page_title="Glacier Retreat & Emission Analysis", layout="wide")

# Header
st.title("❄️ Glacier Retreat & GHG Emission Analysis with Filter Recommendation")
st.write("### 🌍 Predict glacier retreat, forecast GHG emissions, and recommend filters.")

# Sidebar Inputs
st.sidebar.header("🔹 User Input Parameters")

# Select emission type
emission_type = st.sidebar.selectbox("Select Emission Type:", ['CO2', 'CH4', 'N2O'])

# Get user input
glacier_area = st.sidebar.slider("Initial Glacier Area (sq. km):", min_value=50.0, max_value=1000.0, value=500.0, step=10.0)
temp_rise = st.sidebar.slider("Temperature Rise (°C):", min_value=0.0, max_value=10.0, value=2.5, step=0.1)
precipitation = st.sidebar.slider("Precipitation (mm/year):", min_value=100.0, max_value=2000.0, value=1200.0, step=50.0)

# Encoding emission type
emission_map = {'CO2': [1, 0, 0], 'CH4': [0, 1, 0], 'N2O': [0, 0, 1]}
encoded_emission = emission_map[emission_type]

# Glacier Retreat Prediction
glacier_pred = glacier_model.predict([[glacier_area, temp_rise, precipitation]])

# GHG Emission Prediction
emission_pred = emission_model.predict([[glacier_pred[0], temp_rise]])

# 🌟 **Dynamic Filter Recommendation Logic**
# Add slight random variations to simulate real-world diversity
random_variation = random.uniform(0.85, 1.15)  # 15% variation
dynamic_volume = emission_pred[0] * random_variation

# Randomize efficiency (only for display purposes, not for model input)
dynamic_efficiency = random.randint(80, 95)

# ✅ Correct filter prediction with 4 features (no efficiency passed)
filter_pred = filter_model.predict([[*encoded_emission, dynamic_volume]])

# 🌟 **Display Results**
col1, col2, col3 = st.columns(3)

# Column 1: Glacier Retreat Prediction
with col1:
    st.write("### 🧊 Glacier Retreat Prediction")
    st.write(f"🌡️ Predicted Glacier Area After Melt: {glacier_pred[0]:.2f} sq. km")

# Column 2: GHG Emissions Prediction
with col2:
    st.write("### 🌿 Predicted GHG Emissions")
    st.write(f"🔥 {emission_pred[0]:.2f} tons/year")

# Column 3: Filter Recommendation
with col3:
    st.write("### 🛠️ Recommended Filter")
    st.write(f"🛡️ {filter_pred[0]}")
    st.write(f"🔥 Emission Volume Used for Filter: {dynamic_volume:.2f} tons/year")
    st.write(f"⚙️ Filter Efficiency: {dynamic_efficiency}%")  # For display only

# 🌟 **Data Visualization**
st.write("### 📊 Visualizations")

# Load updated datasets for visualization
glacier_data = pd.read_csv("data/glacier_data.csv")
emission_data = pd.read_csv("data/emissions_data.csv")
filter_data = pd.read_csv("data/filter_data.csv")

# Check if 'year' column exists before setting the index
if 'year' in glacier_data.columns:
    st.write("#### 🧊 Glacier Retreat Over Time")
    st.line_chart(glacier_data.set_index('year'))
else:
    st.error("⚠️ 'year' column missing in glacier_data.csv")

if 'year' in emission_data.columns:
    st.write("#### 🌿 GHG Emission Forecast")
    st.line_chart(emission_data.set_index('year'))
else:
    st.error("⚠️ 'year' column missing in emission_data.csv")

# Filter Efficiency Visualization
# Check if required columns are present
if 'filter' in filter_data.columns and 'efficiency' in filter_data.columns:
    st.write("#### 🛠️ Filter Efficiency by Emission Type")
    
    # Use 'filter' and 'efficiency' for visualization
    st.bar_chart(filter_data.set_index('filter')['efficiency'])

else:
    st.error("⚠️ Missing required columns in filter_data.csv")

