#!/usr/bin/env python
# coding: utf-8

# In[21]:


import Funciones #Importamos las librerías a utilizar
import math as m
import scipy.special as sp


# In[15]:


Funciones.Factorial(10)==m.factorial(10) #Verificamos la función Binomial con math


# In[20]:


sp.binom(9,5)==Funciones.Binomial(9,5) #Verificamos la función Binomial con scipy.special


# In[ ]:




