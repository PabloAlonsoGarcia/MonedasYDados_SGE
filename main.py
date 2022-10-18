from pprint import pprint
import matplotlib.pyplot as plt
import random

diccionario = {
    'moneda': {
        'cara': {},
        'cruz': {}
    },
    'dado': {}
}
if __name__ == '__main__':

    for y in range(11):
        diccionario['moneda']['cara'][y] = 0
        diccionario['moneda']['cruz'][y] = 0
    for y in range(3, 19):
        diccionario['dado'][y] = 0



    for x in range(1_000_000):
        contCara = 0
        conCruz = 0
        valorDados=0
        for y in range(10):
            nRandom = random.randint(0, 1)
            if nRandom == 0:
                contCara += 1
            else:
                conCruz += 1
        diccionario['moneda']['cara'][contCara] += 1
        diccionario['moneda']['cruz'][conCruz] += 1

        for z in range(3):
            zRandom = 0
            valorDados += random.randint(1, 6)
        diccionario['dado'][valorDados] += 1

    pprint(diccionario)

    plt.figure()
    clavesCara = diccionario['moneda']['cara'].keys()
    valoresCara = diccionario['moneda']['cara'].values()
    plt.plot(clavesCara, valoresCara)
    plt.xlabel("Ocurrencias cara")
    plt.show()


    plt.figure()
    clavesCruz = diccionario['moneda']['cruz'].keys()
    valoresCruz = diccionario['moneda']['cruz'].values()
    plt.plot(clavesCruz, valoresCruz)
    plt.xlabel("Ocurrencias cruz")
    plt.show()

    plt.figure()
    clavesDados = diccionario['dado'].keys()
    valoresDados = diccionario['dado'].values()
    plt.plot(clavesDados, valoresDados)
    plt.xlabel("Ocurrencias dado")
    plt.show()








