from pprint import pprint
import matplotlib.pyplot as plt
import random

#Creación diccionario y subdiccionarios

diccionario = {
    'moneda': {
        'cara': {},
        'cruz': {}
    },
    'dado': {}
}

if __name__ == '__main__':

#Creacion claves e inicializacion de valores
    for y in range(11):
        diccionario['moneda']['cara'][y] = 0
        diccionario['moneda']['cruz'][y] = 0
    for y in range(3, 19):
        diccionario['dado'][y] = 0


#Realizamos el millón de experimentos
    for x in range(1_000_000):
        contCara = 0
        conCruz = 0
        valorDados=0
#Tiramos 10 veces la moneda
        for y in range(10):
            nRandom = random.randint(0, 1)
            if nRandom == 0:
                contCara += 1
            else:
                conCruz += 1
        diccionario['moneda']['cara'][contCara] += 1
        diccionario['moneda']['cruz'][conCruz] += 1
#Tiramos 3 veces el dado
        for z in range(3):
            zRandom = 0
            valorDados += random.randint(1, 6)
        diccionario['dado'][valorDados] += 1
#Mostramos el diccionario
    pprint(diccionario)

#Mostramos las gráficas con los resultados
    plt.figure()
    clavesCara = diccionario['moneda']['cara'].keys()
    valoresCara = diccionario['moneda']['cara'].values()
    plt.plot(clavesCara, valoresCara)
    plt.xlabel("Resultados cara")
    plt.show()


    plt.figure()
    clavesCruz = diccionario['moneda']['cruz'].keys()
    valoresCruz = diccionario['moneda']['cruz'].values()
    plt.plot(clavesCruz, valoresCruz)
    plt.xlabel("Resultados cruz")
    plt.show()

    plt.figure()
    clavesDados = diccionario['dado'].keys()
    valoresDados = diccionario['dado'].values()
    plt.plot(clavesDados, valoresDados)
    plt.xlabel("Resultados dado")
    plt.show()








