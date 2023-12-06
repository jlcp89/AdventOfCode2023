import re

def obtenerId(texto):
    patron = r'Card\s*(\d+):'
    match = re.search(patron, texto)
    if match:
        numero = match.group(1)
        return int(numero)
    else:
        return None


def contarTotal(lineas):
    num_dict = {}

    for linea in lineas:
        id = obtenerId(linea)
        num_dict[id] = 1

    for linea in lineas:
        id = obtenerId(linea)
        linea_div = linea.split(':')
        lineas_numeros = linea_div[1].split('|')

        lineas_numeros[0] = lineas_numeros[0].strip()
        lineas_numeros[1] = lineas_numeros[1].strip()

        numeros_ganadores = [int(numero) for numero in lineas_numeros[0].split() if numero]
        numeros_actuales = [int(numero) for numero in lineas_numeros[1].split() if numero]

        matching_numbers = sum(1 for num in numeros_actuales if num in numeros_ganadores)

        if id is not None and id in num_dict:
            for i in range(id + 1, id + 1 + matching_numbers):
                if i in num_dict:
                    num_dict[i] += num_dict[id]
        print(f'{num_dict[id]}')

    total_scratchcards = sum(num_dict.values())

    return total_scratchcards

def procesar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()

            print(f'Total de lineas: {contarTotal(lineas)}')
    except FileNotFoundError:
        print(f'Error: El archivo {nombre_archivo} no fue encontrado.')

procesar_archivo('datosCartas.txt')
