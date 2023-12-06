import re

def obtenerId(linea):
    match = re.search(r'Card (\d+):', linea)
    if match:
        return int(match.group(1))
    

def obtenerPuntos (linea):

    linea_div = linea.split(':')
    lineas_numeros = linea_div[1].split('|')

    lineas_numeros[0] = lineas_numeros[0].strip()
    lineas_numeros[1] = lineas_numeros[1].strip()

    numeros_ganadores = lineas_numeros[0].split(" ")
    numeros_actuales = lineas_numeros[1].split(" ")

    for numero in numeros_ganadores:
        if numero == ' ' or numero == '':
            numeros_ganadores.remove(numero)

    for numero in numeros_actuales:
        if numero == ' ' or numero == '':
            numeros_actuales.remove(numero)
        
    
    num_ganadores = []
    for numero in numeros_ganadores:
        num_ganadores.append(int(numero))

    num_actuales = []
    for numero in numeros_actuales:
        num_actuales.append(int(numero))


    coincidencias = 0
    puntos = 0
    


    for num_ganador in num_ganadores:
        for num_actual in num_actuales:
            if num_ganador == num_actual:
                coincidencias += 1
                if coincidencias == 1:
                    puntos = 1
                else:
                    puntos = puntos * 2

    return puntos




def procesar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            suma_total = 0
            for linea in archivo:
                id = obtenerId(linea)
                puntos = obtenerPuntos(linea)
                print(f'Game: {id} Puntos: {puntos}')
                suma_total += puntos
            print(f'Suma total de puntos: {suma_total}')
    except FileNotFoundError:
        print(f'Error: El archivo {nombre_archivo} no fue encontrado.')

# Reemplaza 'nombre_del_archivo.txt' con el nombre de tu archivo
procesar_archivo('datosCartas.txt')