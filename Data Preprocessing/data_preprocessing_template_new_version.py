#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 12:11:34 2020

@author: juangabriel
"""


# Plantilla de Pre Procesado

# Cómo importar las librerias en Python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
#-------------------------------------------
# Importar el Data set
dataset = pd.read_csv("Data.csv")
X = dataset.iloc[:, :-1].values 
y = dataset.iloc[:, 3].values 

#------------------------------------------
# Tratamiento de los NAs
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean", verbose=0)
imputer = imputer.fit(X[:,1:3]) 
X[:, 1:3] = imputer.transform(X[:,1:3])

#------------------------------------------
# Codificar datos categoricos
# Pasar a numero
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])

# Pasar a Variables Dummy
ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto'), [0])],   
    remainder='passthrough'                        
)

X = np.array(ct.fit_transform(X), dtype=float)
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

#---------------------------------------------
# Dividir el data set en conjunto de entrenamiento y en conjunto de testing
# X_train = variables independientes de entrenamiento para entrenear al algoritmo
# X_test = variables independientes para testear que el algoritmo funciona correctamente
# y_train = valores de prediccion que se suministran al algoritmo para que aprende a predecir
# y_test = Para validar que las predicciones de testing son o no son correctas
# test_size = 0.2, 20% para test (hasta 30% para testing)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.2, random_state = 0)

# Escalado de variables
# Normalizar los datos para que ambas variables se encuentren de ntro de un mismo rango de valores
# Escalar entre -1 y 1
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)