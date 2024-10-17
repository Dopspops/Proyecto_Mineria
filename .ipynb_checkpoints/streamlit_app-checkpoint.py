# =================================================================
# == INSTITUTO TECNOLOGICO Y DE ESTUDIOS SUPERIORES DE OCCIDENTE ==
# ==         ITESO, UNIVERSIDAD JESUITA DE GUADALAJARA           ==
# ==                                                             ==
# ==            MAESTRÍA EN SISTEMAS COMPUTACIONALES             ==
# ==             PROGRAMACIÓN PARA ANÁLISIS DE DATOS             ==
# ==                 IMPLEMENTACIÓN EN STREAMLIT                 ==
# =================================================================

#----- Importación de Librerías -----------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import random
from skimage import io


#------------------------------------------------------------------
#----- Configuración Inicial del Panel Central --------------------
#------------------------------------------------------------------

#----- Lectura de la Imagen ---------------------------------------
Logo = io.imread(r"./Imagenes/ITESO_Logo.png")
GraficaEstaciones = io.imread(r"./Imagenes/Agrupacion_por_estaciones_Numeros_de_viajes.png")
GraficaNumViajesEstaciones = io.imread(r"./Imagenes/num_viajes_por_mesyanio.png")
GraficaPromedioDeViaje = io.imread(r"./Imagenes/promedio_tiempo_viaje_poranio.png")
GraficaComparacionTiempoRutaGenero = io.imread(r"./Imagenes/tiempo_ruta_entre_genero.png")
GraficaUsoDiasSemana = io.imread(r"./Imagenes/uso_dias_semana.png")
GraficaDineroGastado = io.imread(r"./Imagenes/apox_dinero_gastado.png")
GraficaUsoDeEstaciones = io.imread(r"./Imagenes/uso_de_estaciones.png")
GraficaCorrelacionEdadTiempo = io.imread(r"./Imagenes/corr_edad_tiempo_viaje.png")

GraficaCorrelacionDiaSemanaTiempo = io.imread(r"./Imagenes/corr_dia_semana_tiempo_viaje.png")


#----- Renderizado de la Imagen -----------------------------------
st.image(Logo, width = 500)

#----- Renderizado del Texto --------------------------------------
st.title("Proyecto de Programación para Mineria de Datos")
st.subheader(":blue[Ferdinand Josef Bierbaum Agular - Exp. 739162]")
st.markdown("Este proyecto se estaría basando sobre los datos proporcionados de MiBici. Se tienen registros desde 2015 al 2024.")
st.markdown("El procedimiento para la lectura de los datos fue separar todos los archivos por su respectivo año. Es decir, todos los archivos de un respectivo año estan en una misma carpeta.")
st.markdown("Después, se crea un nuevo CSV con todos los datos del respectivo año."
"Con este nuevo archivo, se realizó la limpia de datos, se removieron los años de 1910 hasta 1960 y 2018 a 2024. A su vez, se reemplazaron algunos años, como 200 a 2000.")
st.markdown("Terminando este proceso, se tienen archivos nuevos limpios. Estos son los que se usaron para las siguientes gráficas.")

st.divider()


# ------- Grafico Agrupacion por Estaciones --------------------
st.subheader("Gráfico Agrupación por Estaciones")
st.image(GraficaEstaciones)
plt.show()
st.divider()


# ------ Grafico Numeros de Viajes (mes y año)
st.subheader("Gráfico Numeros de Viajes (mes y año )")
st.image(GracicaNumViajesEstaciones)
plt.show()
st.divider()

# ------ Promedios de Viaje 
st.subheader("Gráfico Promedio de Viaje")
st.image(GraficaPromedioDeViaje)
plt.show()
st.divider()

# ------ Comparacion Tiempo y Ruta entre Genero
st.subheader("Gráfico por Uso por Dias de le Semana")
st.image(GraficaComparacionTiempoRutaGenero)
plt.show()
st.divider()

# ------ Grafico Uso por Dias de Semana
st.subheader("Gráfico sobre el Uso por Dias de Semana")
st.image(GraficaUsoDiasSemana)
plt.show()
st.divider()

# ------ Dinero Gastado
st.subheader("Gráfico Sobre el Dinero Gastado")
st.image(GraficaDineroGastado)
plt.show()
st.divider()

# ------ Uso de Estaciones 
st.subheader("Gráfico de Uso de Estaciones")
st.image(GraficaUsoDeEstaciones)
plt.show()
st.divider()

# ------ Correlación entre edad y tiempo de viaje
st.subheader("Gráfico de Correlacion entre Edad y Tiempo de Viaje")
st.image(GraficaCorrelacionEdadTiempo)
plt.show()
st.divider()

# ------ Correlacion dia de la semana y tiempo de viaje
st.subheader("Gráfico de Correlacion sobre Dia de la Semana y Tiempo de Viaje")
st.image(GraficaCorrelacionDiaSemanaTiempo)
plt.show()
st.divider()





