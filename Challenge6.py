#Utilizando documentación de pandas:

#Handle data
#https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html

#Graphs
#https://matplotlib.org/stable/tutorials/introductory/pyplot.html

#1) Realizar la regresión lineal de los tests (datasets) del archivo file-load.csv (por separado). *Regresión lineal del script
#2) Generar las respectivas graficas una por una.
#3) Generar la regresión multiple para que puedan verse los historicos de examenes y la calif final.*Regresión multiple
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

datos = pd.read_csv('file-load-V2.csv')
#print(datos)
""" 
Last_name=datos['Last_name'].values
Test1=datos['Test1'].values
Test2=datos['Test2'].values
Test3=datos['Test3'].values
Test4=datos['Test4'].values
Final=datos['Final'].values
Grade=datos['Grade'].values
"""
lm= LinearRegression()
x=datos[['Test1','Test2','Test3','Test4']]
print(x)
y=datos['Final']

print('*'*100)
print(y)
print('*'*100)

lm.fit(x,y)

prediccion = lm.predict(x)
a= lm.intercept_
b= lm.coef_

print('*'*100)
print('---prediccion----')
print(prediccion)
print(y)
print(lm.score(x,y))

resultado = {'Real ':datos['Final'],'predicion':prediccion}
R = pd.DataFrame(data=resultado)
print(R.head())

from sklearn import metrics
ECM = metrics.mean_squared_error(datos['Final'],prediccion)
print(ECM)

r_cuadrado= metrics.r2_score(datos['Final'],prediccion)
print(r_cuadrado)

#graficamos
plt.plot(datos['Test4'], prediccion, 'r', label='Prediccion')
plt.scatter(datos['Test4'],y, label='Datos')
plt.title('Regresion')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()



""" 
#modelo
reg=LinearRegression()
reg=reg.fit(X,Y)
Y_pred=reg.predict(X)
error=np.sqrt(mean_squared_error(Y,Y_pred))
r2=reg.score(X,Y)
print('el error es : ',error)
print('el error r cuad : ',r2)
print('los coeficientes son: \n', reg.coef_)
"""

