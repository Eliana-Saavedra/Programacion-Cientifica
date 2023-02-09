


#Punto 1) Escriba una función que multiplique todos los números de un arreglo
def multiplica_numeros_arreglo(arreglo):
    multiplicacion = 1

    for i in arreglo: # Se recorre el arreglo para multiplicar los elementos
        multiplicacion *= i

    print("La multiplicación de todos los numeros del arreglo es:", multiplicacion)
    return multiplicacion

arr = input("Ingrese una lista de números de la forma (a,b,c,...,z): ").split(",") #Se solicita una lista de números
arr = map(float,arr)
multiplica_numeros_arreglo(arr)
"""
"""
#Punto 2) Escriba una función que calcule el factorial de un número entero positivo. Luego pruebela con ejemplo.

def factorial(numero):
    rta = numero
    if numero == 1:
        rta = 1
    while numero > 1:  
        rta = rta* (numero -1)  
        numero -= 1 
    return rta

print(factorial(5))
"""    
"""      
#Punto 3) Escriba una función que indique si un número entero positivo pertenece a la serie de Fibonacci. Luego pruebela con ejemplo.    
def esFibonacci(n):
    antes= 0
    despues = 1
    rta = False
    while (antes<=n):
        if (antes==n):
            rta=True
        suma=antes+despues
        despues=suma
        antes=despues
    return rta
n=int(input("Escriba el numero que quiere comprobar: "))
if esFibonacci(n):
    print("Si pertenece a la serie de fibonacci")
else:
    print("No pertenece a la serie fibonacci")


#Punto 4)  Usando las funciones de las librerías numpy y matplotlib para Python
#           obtenga 1000 valores aleatorios con distribución uniforme y 1000 valores con una distribución normal.
import numpy as np
import matplotlib.pyplot as plt


distribucion_uniforme = np.random.uniform(0, 1, 1000) # Generamos 1000 valores aleatorios con distribución uniforme
distribucion_normal = np.random.normal(0, 1, 1000) # Generamos 1000 valores aleatorios con distribución normal
sum_values = distribucion_uniforme + distribucion_normal # Sumamos ambos conjuntos de valores

fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Graficamos los histogramas con 10, 20, 30 y 50 particiones
axs[0, 0].hist(sum_values, bins=10, color='red')
axs[0, 1].hist(sum_values, bins=20, color='blue')
axs[1, 0].hist(sum_values, bins=30, color='green')
axs[1, 1].hist(sum_values, bins=50, color='purple')

plt.show()
 

#Punto 5) Grafique el desplazamiento, velocidad y aceleración bajo los parámetros: 


#𝑥 = 𝐴  𝑐𝑜𝑠(ω𝑡 + ϕ)
# Se inicializa el periodo, la amplitud, la velocidad angular, y el tiempo
#T = 4s (periodo) 
#t = 8s (duración) 
#A = 5m (amplitud) 
T = 4
A = 5
w = (2*(np.pi))/T
t = np.linspace(0, 8 ,10000) #  Cree un vector de tiempo que vaya desde 0 hasta el tiempo final(t).*

#Grafique el desplazamiento, velocidad y aceleración:
#DESPLAZAMIENTO:
plt.subplot(1,3,1)
x = A*np.cos((w*t)) # (Se usa la ecuacion  x = Acos(wt))
plt.plot(t, x, color = 'blue') # Se genera la gráfica de desplazamiento
plt.xlabel("t(s)")
plt.ylabel("Amplitud ($m$)")
plt.title("Desplazamiento")
plt.grid(1)

#VELOCIDAD
plt.subplot(1,3,2)
v = -A*w*np.sin((w*t)) # (Se usa la ecuación de v = -Awsen(wt))
plt.plot(t, v) # Se genera la gráfica de la velocidad
plt.xlabel("t(s)")
plt.ylabel("Velocidad (m/s)")
plt.title("Velocidad")
plt.grid(1)

#ACELERACIÓN 
plt.subplot(1,3,3)
a = -A*(w**2)*np.cos((w*t)) #(Se usa la ecuación de a = -A(w^2)cos(wt))
plt.plot(t,a, color = 'red') # Se genera la gráfica de aceleración
plt.xlabel("t(s)")
plt.ylabel("Aceleración (m/s^2)")
plt.title("Aceleración")
plt.grid(1)


plt.tight_layout()
plt.show()
  

# Punto 6) Operaciones entre matrices
A=[[0.1,2],[2,0.1]]
B=[[1,2,3],[4,5,6]]
C=[[5/3, 2/3],[2/3, 5/3]]

# A∗B.
#Usando Numpy 
import numpy as np

def multiplicacion_matriz_A_y_B(A, B):
    return np.dot(A, B)

result = multiplicacion_matriz_A_y_B(A, B)
print(result)

#A^2*B
def multiplicacion_matriz_AA_y_B(A, B):
    rta=np.dot(np.dot(A,A),B)
    return rta 

result = multiplicacion_matriz_AA_y_B(A, B)
print(result)

#C^3*   
def multiplicacion_matriz_CCC_y_B(C,B):
    rta=np.dot(np.dot(np.dot(C,C),C),B)
    return rta
result= multiplicacion_matriz_CCC_y_B(C, B)
print(result)