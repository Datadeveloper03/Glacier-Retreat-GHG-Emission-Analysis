import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt

# 3D Visualization for Glacier Retreat
def glacier_3d_plot():
    data = pd.read_csv("data/glacier_data.csv")

    fig = go.Figure(data=[go.Surface(z=data['glacier_area'].values.reshape(10, 10),
                                     x=data['year'], y=data['avg_temp'])])
    fig.update_layout(title='Glacier Retreat 3D Plot',
                      scene=dict(xaxis_title='Year', yaxis_title='Temperature Rise (°C)', zaxis_title='Glacier Area'))
    fig.show()

# Filter Efficiency Over Time
def filter_efficiency_plot():
    years = list(range(1, 11))
    efficiency = [90 - (i * 5) for i in years]

    plt.plot(years, efficiency, label='Filter Efficiency', color='green')
    plt.xlabel('Years')
    plt.ylabel('Efficiency (%)')
    plt.title('Filter Efficiency Over Time')
    plt.legend()
    plt.show()
