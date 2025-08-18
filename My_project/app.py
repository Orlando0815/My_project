#Cargando librerias 
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


#Cargar datos
df = pd.read_csv('My_project/vehicles_us.csv')

st.header('Relación de automoviles', divider = 'gray')

hist_button = st.button('Construir histograma')

if hist_button: 
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    
    fig = px.histogram(df, x="odometer") 

    
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    
    fig = px.scatter(df, x="odometer", y="price", title="Relación entre Kilometraje y Precio")

    
    st.plotly_chart(fig, use_container_width=True)
