#!/usr/bin/env python
# coding: utf-8

# In[104]:


def Factorial(n): #Definimos la función factorial
    if n==0: #Condicionamos para no tener errores en 0 y 1, dado que los valores factoriales son los mismos
            return 1
    if int(n**2)!=n**2:
        import sys 
        print("No es un número entero positivo")
        sys.exit()
    if n<0: #Condicionamos para no tener factoriales de números positivos
        import sys 
        print("No es un número entero positivo")
        sys.exit()
    else:
        resultado = 1
        for i in range(2,n+1):#Factorial de n, para n distinto de 0 y 1
            resultado = resultado*i
        
    return resultado #Retornamos el resultado de la función evaluada 


# In[105]:


def Binomial(n,k): # Definimos la función binomial
    return Factorial(n)/(Factorial(k)*Factorial(n-k)) # Restornamos el resultado de la función evaluada
    


# In[106]:


def Pascal(n): #Definimos la función
    import os #Importamos la libreria a utilizar
    file = open("Pascal-"+str(n)+".txt.","w")#Creamos el archivos txt en el que vamos a escribir
    for j in range(0,n+1): #For para correr n- veces el programa y tener los distintos resultados
        c=[] #Lista vacia donde iremos almacenando los datos
        
        for i in range(0,j+1): # For para correr k-veces)
            c.append(int(Binomial(j,i))) #Llenamos la lista vacia con la función binomial
            
        
        file.write('n=%s  '%i) # Escribimos en el archivo la linea correspondiente al triángulo,
                                #es decir n=1, n=2, etc
        c = str(c) #Convertimos la lista en un string
        c = c.replace("[","").replace("]","").replace(",","    ")
        file.write(((2*(n+9-j)-j -4*int(j/10)))*" " +c+ os.linesep) #Escribimos las lineas de cada parte del triángulo 
                                            #correspondiente a cada n
        
    file.close()
    return







