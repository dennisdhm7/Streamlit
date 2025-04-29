# archivo: app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título
st.title("Sales Dashboard")

# Datos de ejemplo
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [1500, 1800, 2400, 3000, 2800]
}
df = pd.DataFrame(data)

# Mostrar tabla
st.subheader("Sales Data")
st.dataframe(df)

# Gráfico
st.subheader("Sales Line Chart")
plt.plot(df["Month"], df["Sales"], marker='o')
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
st.pyplot(plt)
