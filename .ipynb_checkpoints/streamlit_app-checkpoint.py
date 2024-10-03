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

#----- Renderizado de la Imagen -----------------------------------
st.image(Logo, width = 500)

#----- Renderizado del Texto --------------------------------------
st.title("Proyecto de Programación para Mineria de Datos")
st.subheader(":blue[Ferdinand Josef Bierbaum Agular - Exp. 739162]")
st.markdown("Este proyecto se estaría basando sobre los datos proporcionados de MiBici. Se tienen registros desde 2015 al 2024.")


#------------------------------------------------------------------
#----- Configuración de los Elementos del DashBoard ---------------
#------------------------------------------------------------------

#----- Renderizado de la Imagen y el Título en el Dashboard -------
st.sidebar.image(Logo, width = 200)
st.sidebar.markdown("## MENÚ DE CONFIGURACIÓN")
st.sidebar.divider()

