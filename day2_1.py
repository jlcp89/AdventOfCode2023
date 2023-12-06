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




def juego_valido(linea):
    partes_linea  = linea.strip().split( ":")
    muestras = extraer_muestras(partes_linea[1])
    linea_invalida = False
    for muestra in muestras:
        pares_texto = muestra.split(',')
        for par in pares_texto:
            par_separado = par.strip().split(" ")
            # print(f"{int(par_separado[0])}")
            if par_separado[1] == 'red':
                if int(par_separado[0]) > MAX_RED:
                    linea_invalida = True
                
            if par_separado[1] == 'blue':
                if int(par_separado[0]) > MAX_BLUE:
                    linea_invalida = True
                
            if par_separado[1] == 'green':
                if int(par_separado[0]) > MAX_GREEN:
                    linea_invalida = True
    if linea_invalida:
        return False
    else:
        return True                
                

def procesar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            suma_total = 0
            for linea in archivo:
                id = obtener_id(linea)
                esValido = juego_valido(linea)
                print(f'Game: {id}, Valido: {esValido}')
                if esValido:
                    suma_total += id
            print(f'Suma total de calibraciones: {suma_total}')
    except FileNotFoundError:
        print(f'Error: El archivo {nombre_archivo} no fue encontrado.')

# Reemplaza 'nombre_del_archivo.txt' con el nombre de tu archivo
procesar_archivo('datos.txt')