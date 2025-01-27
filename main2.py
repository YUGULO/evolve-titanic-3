import streamlit as st
import pandas as pd
import colorama


titanic = pd.read_csv("titanic.csv")

st.title("Análisis de Supervivientes del Titanic")

# Crear un gráfico de barras mostrando supervivientes por clase
supervivientes_por_clase = titanic.groupby('Pclass')['Survived'].value_counts().unstack()
supervivientes_por_clase.columns = ['Fallecidos', 'Supervivientes']
supervivientes_por_clase.index = ['Primera Clase', 'Segunda Clase', 'Tercera Clase']

# Mostrar el gráfico
st.bar_chart(supervivientes_por_clase)

# Añadir una explicación
st.markdown("""
### Distribución de Supervivientes por Clase
El gráfico muestra la cantidad de pasajeros que sobrevivieron y fallecieron en cada clase del Titanic.
""")

# Mostrar estadísticas adicionales
st.subheader("Tasa de supervivencia por clase:")
tasa_supervivencia = (titanic.groupby('Pclass')['Survived'].mean() * 100).round(2)
st.write(tasa_supervivencia.to_frame('Tasa de Supervivencia (%)'))

"""
 Objetivo: Usando https://docs.streamlit.io/develop/api-reference crear 3 elementos para mostrar datos de Titanic.
 Los datos están en Pandas ->  
    Ejemplos - ayuda: 
        https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html
        https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html

""" 