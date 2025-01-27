import streamlit as st
import pandas as pd


# Configuración de la página
st.set_page_config(page_title="Análisis del Titanic", page_icon="🚢")

# Manejo de errores al cargar datos
try:
    titanic = pd.read_csv("titanic.csv")
except FileNotFoundError:
    st.error("Error: No se encuentra el archivo titanic.csv")
    st.stop()
except Exception as e:
    st.error(f"Error al cargar los datos: {e}")
    st.stop()

st.title("Análisis de Supervivientes del Titanic")

# Convertir valores numéricos a texto descriptivo
titanic['Survived'] = titanic['Survived'].map({0: 'Fallecidos', 1: 'Supervivientes'})

# Selector de visualización
vista_seleccionada = st.selectbox(
    "Selecciona el tipo de visualización:",
    ["Por Clase", "Por Género", "Por Edad"]
)

if vista_seleccionada == "Por Clase":
    # Crear un gráfico de barras mostrando supervivientes por clase
    supervivientes_por_clase = titanic.groupby('Pclass')['Survived'].value_counts().unstack()
    supervivientes_por_clase.index = ['Primera Clase', 'Segunda Clase', 'Tercera Clase']
    
    # Mostrar el gráfico
    st.bar_chart(supervivientes_por_clase)
    
    # Mostrar estadísticas
    st.subheader("Tasa de supervivencia por clase:")
    tasa_supervivencia = (titanic.groupby('Pclass')['Survived']
                         .apply(lambda x: (x == 'Supervivientes').mean() * 100)
                         .round(2))
    st.write(tasa_supervivencia.to_frame('Tasa de Supervivencia (%)'))

elif vista_seleccionada == "Por Género":
    supervivientes_por_genero = titanic.groupby('Sex')['Survived'].value_counts().unstack()
    supervivientes_por_genero.index = ['Mujeres', 'Hombres']
    st.bar_chart(supervivientes_por_genero)

elif vista_seleccionada == "Por Edad":
    # Crear grupos de edad
    titanic['Grupo_Edad'] = pd.cut(titanic['Age'], 
                                  bins=[0, 12, 18, 35, 50, 100],
                                  labels=['Niños', 'Adolescentes', 'Jóvenes', 'Adultos', 'Mayores'])
    supervivientes_por_edad = titanic.groupby('Grupo_Edad')['Survived'].value_counts().unstack()
    st.bar_chart(supervivientes_por_edad)

# Añadir explicación
st.markdown("""
### Distribución de Supervivientes
El gráfico muestra la distribución de pasajeros que sobrevivieron y fallecieron según la categoría seleccionada.

#### Datos adicionales:
- Total de pasajeros: {}
- Total de supervivientes: {}
- Porcentaje de supervivencia: {:.2f}%
""".format(
    len(titanic),
    (titanic['Survived'] == 'Supervivientes').sum(),
    (titanic['Survived'] == 'Supervivientes').mean() * 100
))



