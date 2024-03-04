import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
import streamlit as st


merged_data = pd.read_csv("../Data/merged_data.csv")

transaction_counts_per_city = merged_data['customer_city'].value_counts()

# You can also calculate the average transaction value per city for additional insights
average_transaction_values_per_city = merged_data.groupby('customer_city')['payment_value'].mean()


st.title("Project Akhir Analisis Data")

st.subheader("Question 1:")
# Top 20 cities by transaction counts
st.subheader("Top 20 cities by transaction counts")
plt.figure(figsize=(30, 20))  # Adjust the figure size
top_cities_transaction = transaction_counts_per_city.sort_values(ascending=False).head(20)

# Plotting average transaction values for the top 20 cities
ax = top_cities_transaction.plot(kind='bar', color='lightcoral')
plt.title('Top 20 Cities by Transaction Counts')
plt.xlabel('City')
plt.ylabel('Total Transaction Counts')
plt.ylim(0, 20000)  # Adjust the y-axis range based on your data
plt.xticks(rotation=45, ha='right')  # Rotate city labels for better visibility

# Annotate each bar with its value
for i, v in enumerate(top_cities_transaction):
    ax.text(i, v + 50, f'{v:.2f}', ha='center', va='bottom', fontsize=8, color='black')

# Display the plot using Streamlit
st.pyplot(plt)

st.subheader("Question 2:")
# Top 20 cities by transaction values
st.subheader("Top 20 cities by transaction values")
plt.figure(figsize=(30, 20))  # Adjust the figure size
top_cities_avg_transaction = average_transaction_values_per_city.sort_values(ascending=False).head(20)

# Plotting average transaction values for the top 20 cities
ax = top_cities_avg_transaction.plot(kind='bar', color='lightcoral')
plt.title('Top 20 Cities by Average Transaction Values')
plt.xlabel('City')
plt.ylabel('Average Transaction Value')
plt.ylim(0, 3000)  # Adjust the y-axis range based on your data
plt.xticks(rotation=45, ha='right')  # Rotate city labels for better visibility

# Annotate each bar with its value
for i, v in enumerate(top_cities_avg_transaction):
    ax.text(i, v + 50, f'{v:.2f}', ha='center', va='bottom', fontsize=8, color='black')

# Display the plot using Streamlit
st.pyplot(plt)