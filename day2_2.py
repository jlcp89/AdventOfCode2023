import re

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def obtener_id(linea):
    match = re.search(r'Game (\d+):', linea)
    if match:
        return int(match.group(1))
    return '0'

def extraer_muestras(muestras):
    return muestras.split(";")

def dividir_muestra(muestra):

    return muestra.split(',')




def obtenerPotencia(linea):
    partes_linea  = linea.strip().split( ":")
    muestras = extraer_muestras(partes_linea[1])
    linea_invalida = False
    max_red = 0
    max_blue = 0
    max_green = 0
    for muestra in muestras:
        pares_texto = muestra.split(',')
        

        for par in pares_texto:
            par_separado = par.strip().split(" ")
            # print(f"{int(par_separado[0])}")
            num = int(par_separado[0])
            text = par_separado[1]
            if text == 'red':
                if num > max_red:
                    max_red = num
                if num > MAX_RED:
                    linea_invalida = True
                
            if text == 'blue':
                if num > max_blue:
                    max_blue = num
                if num > MAX_BLUE:
                    linea_invalida = True
                
            if text == 'green':
                if num > max_green:
                    max_green = num
                if num > MAX_GREEN:
                    linea_invalida = True

    return int(max_red*max_blue*max_green)                
                

def procesar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            suma_total = 0
            for linea in archivo:
                id = obtener_id(linea)
                potencia = obtenerPotencia(linea)
                print(f'Game: {id}, Potencia: {potencia}')
                suma_total += potencia
            print(f'Suma total de calibraciones: {suma_total}')
    except FileNotFoundError:
        print(f'Error: El archivo {nombre_archivo} no fue encontrado.')

# Reemplaza 'nombre_del_archivo.txt' con el nombre de tu archivo
procesar_archivo('datos.txt')