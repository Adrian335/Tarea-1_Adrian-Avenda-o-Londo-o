#!/usr/bin/env python
# coding: utf-8

# In[1]:


import Funciones #Importamos la librería


# In[2]:


def probabilidad(n,k): #Definimos la función de probabilidad
    return Funciones.Binomial(n,k)/2**n #Retornamos el valor


# In[5]:


P = probabilidad(100,10) #Vemos el resultado de la probabilidad
print("La probabilidad de que de 100 intentos 10 sean cara es de:%.20f"%P) #Imprimimos el resultado


# In[4]:


suma = 0 #Definimos la suma dado que queremos 30 veces cara o más
for i in range(30,101): #Hacemos el for para realizar las operaciones. EL 101 es por la naturaleza del range
    suma += probabilidad(100,i) #Probabilidad sumada desde 30 hasta 100
print("la probabilidad de que caiga cara más de 30 veces es de:%.10f"%suma) #Imprimimos el resultado


# In[6]:


# En mi PC no sé cómo pero 120/1024 da 0, devuelve SIEMPRE la parte entera
#Todo por ponerme a instalar ROOT algo se cambió
#Si alguno sabe cómo solucionar esto de maravillar. Saludos.


# In[ ]:




