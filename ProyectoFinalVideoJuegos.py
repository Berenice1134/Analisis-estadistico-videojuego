#Librerias
import pandas as pd #estadistica
import numpy as np #numeros
import matplotlib.pyplot as plt #graficos

#llamamos al archivo
ds = pd.read_csv('Videojuegos.csv')
pd.set_option('display.max_columns', None)
ds = ds.round(3) # Dejar solo dos decimales
#print(ds)
print(ds.head(1000))

#Columna 1 se le asigna ID
id = ds.iloc[:,1]
#Columna 2 se le asigna nombre
nombre = ds.iloc[:,2]
#Columna 3 se le asigna fecha de lanzamiento
fecha_lan = ds.iloc[:,3]
#Columna 4 se le asigna numero de veces que se marcò como favorito
favoritoN = ds.iloc[:,4]
#Columna 5 se le asigna el tiempo de juego promedio
tiempo_juego = ds.iloc[:,5]
#Columna 5 se le asigna el numero de reseñas 
reseñasN = ds.iloc[:,6]
#Columna 5 se le asigna el numero de calificaciones asignadas
califN = ds.iloc[:,7]
#Columna 5 se le asigna la calificacion final 
calif = ds.iloc[:,8]

#Coeficiente de correlacion (fuerza y direccion entre dos variables)
coef1 = np.corrcoef(tiempo_juego, calif)
coef2 = np.corrcoef(favoritoN, reseñasN)
coef3 = np.corrcoef(califN, calif)

#Medias
mediaF = favoritoN.mean() #Media Numero de Favoritos
mediaT = tiempo_juego.mean() #Media del Tiempo de Juego
mediaRN = reseñasN.mean() #Media Numero de reseñas
mediaCN = califN.mean() #Media Numero de calificaciones
mediaC = calif.mean() #Media Calificacion Final del juego

#Varianza
varF = favoritoN.var()
varT = tiempo_juego.var()
varRN = reseñasN.var()
varCN = califN.var()
varC = calif.var()

#Desviacion Estándar
desvestF = np.sqrt(varF) #
desvestT = np.sqrt(varT) #
desvestRN = np.sqrt(varRN) #
desvestCN = np.sqrt(varCN) #
desvestC = np.sqrt(varC) #

#Covarianza TIEMPO-CALIFICACION
covarianzaTC = np.cov(tiempo_juego,calif)
covarianzaTC[0,1]
#Covarianza NUMERO DE FAVORITOS-NUMERO DE RESEÑAS
covarianzaFR = np.cov(favoritoN,reseñasN)
covarianzaFR[0,1]
#Covarianza NUMERO DE CALIFICACIONES-CALIFICACION
covarianzaFC = np.cov(favoritoN,calif)
covarianzaFC[0,1]

#Pendiente
pendienteTC = covarianzaTC[0,1] / np.var(tiempo_juego)
pendienteFRN = covarianzaFR[0,1] / np.var(favoritoN)
pendienteFCN = covarianzaFC[0,1] / np.var(favoritoN)

#b
b1 = mediaC - (pendienteTC * mediaT)
b2 = mediaRN - (pendienteFRN * mediaF)
b3 = mediaC - (pendienteFCN * mediaF)

#Coeficiente de Correlacion
print("\n\nCoeficiente de Correlacion (Tiempo de Juego - Calificación): ",coef1)
print("Coeficiente de Correlacion (Número de Favoritos - Número de Reseñas): ",coef2)
print("Coeficiente de Correlacion (Numero de Favoritos - Calificacionn): ",coef3)

#Media
print("\nMedia del Numero de Favoritos: ",mediaF)
print("Media deL Tiempo de Juego: ",mediaT)
print("Media del Numero de Reseñas: ",mediaRN)
print("Media del Numero de Calificaciones: ",mediaCN)
print("Media de la Calificaciòn: ",mediaC)

#Varianza
print("\nVarianza del Numero de Favoritos: ",varF)
print("Varianza deL Tiempo de Juego: ",varT)
print("Varianza del Numero de Reseñas: ",varRN)
print("Varianza del Numero de Calificaciones: ",varCN)
print("Varianza de la Calificaciòn: ",varC)

#Desviación estándar
print("\nDesviacion Estandar del Numero de Favoritos: ",desvestF)
print("Desviacion Estandar deL Tiempo de Juego: ",desvestT)
print("Desviacion Estandar del Numero de Reseñas: ",desvestRN)
print("Desviacion Estandar del Numero de Calificaciones: ",desvestCN)
print("Desviacion Estandar de la Calificaciòn: ",desvestC)

#Covarianza
print("\nCovarianza (Tiempo - Calificacion): ",covarianzaTC)
print("Covarianza (Favoritos - Reseñas): ",covarianzaFR)
print("Covarianza (Favoritos - Calificacion): ",covarianzaFC)

#Pendiente
print("\nPendiente (Tiempo - Calificación): ",pendienteTC)
print("Pendiente (Favoritos - Reseñas): ",pendienteFRN)
print("Pendiente (Favoritos - Calificación): ",pendienteFCN)

#b
print("\nb (Tiempo - Calificacion): ",b1)
print("b (Favorito - Reseñas): ",b2)
print("b (Favorito - Calificacion): ",b3)
