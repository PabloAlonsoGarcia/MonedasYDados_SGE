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

    for x in 1_000_000:
        contCara = 0
        conCruz = 0
        for y in 10:
            nRandom = random.randint(0, 1)
            if nRandom == 0:
                contCara += 1
            else:
                conCruz += 1
        diccionario['moneda']['cara'][contCara] += 1
        diccionario['moneda']['cruz'][conCruz] += 1

        for z in 3:
            zRandom







