# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Quantitative Methods and Simulation                             #
# Miguel Marines                                                  #
# Activity: Gambling Simulation                    		          #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

import matplotlib.pyplot as plt # Biblioteca para hacer gráficas.
import random # Biblioteca para generar numeros aleatorios.

total = 0 # Cantidad total de dinero ganada o perdida.
N = 10000 # Numero de veces que se avienta el dado.

freqs = {} # Diccionario para guardar la frecuencia de cada numero del 1 al 6 (Se usan como las llaves del diccionario).
money = []
trials = []

for i in range(N): # Ciclo para aventar el dado el número de veces indicado por N.
    dice = random.randint(1,6) # Genera un número aleatorio del 1 al 6.
    
    # Agrega 1 al número de frecuencia del número correspondiente en el diccionario.
    if dice in freqs:
        freqs[dice] += 1
    else:
        freqs[dice] = 1
        
    if dice in (1, 2, 3): # Si cae en el número 1 o 2 o 3 se gana 2.
        total += 2 # Se suma 2 a la cantidad total de dinero.
    elif dice in (4, 5): # Si cae en el número 4 o 4 se gana 4.
        total += 4 # Se suma 4 a la cantidad total de dinero.
    else: # Si cae 6 se pierde 6.
        total -= 6 # Se resta 6 a la cantidad total de dinero.
    
    money.append(total)
    trials.append(i)

faces = list(freqs.keys()) # Lista las llaves del diccionario (Numeros del 1 al 6).
freq = list(freqs.values()) # Lista los valores del diccionario (Cuantas veces caen cada uno de los numeros del 1 al 6).

# Grafica la informacion
plt.figure(1)
plt.bar(faces, freq) # Grafica la frecuencia con la que aparecen cada uno de los números del 1 al 6.
plt.figure(2)
plt.plot(trials, money) # Grafica el número de veces que se avento el dado y el dinero que se ganó y perdió.
plt.show()

print(f'Total: ${total}') # Imprime el total de dinero ganado o perdido.