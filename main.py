from pprint import pprint
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






