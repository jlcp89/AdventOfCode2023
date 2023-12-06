
def obtener_calibracion(linea):
    calibracion = [0, '']

    palabras_a_reemplazar = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    for palabra, valor in palabras_a_reemplazar.items():
        linea = linea.replace(palabra, palabra[0]+ str(valor) +palabra[-1])
        
    calibracion[1] = linea

    # Filtrar dígitos de la línea
    digitos = [caracter for caracter in linea if caracter.isdigit()]
    
    # Combinar el primer y último dígito para formar un número de dos dígitos
    if len(digitos) >= 2:
        calibracion[0] = int(digitos[0] + digitos[-1])
        return calibracion
    elif len(digitos) == 1:
        calibracion[0] = int(digitos[0] + digitos[0])
        return calibracion
    return calibracion

def procesar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            suma_total = 0
            for linea in archivo:
                calibracion = obtener_calibracion(linea)
                print(f'Línea: {linea.strip()}, Calibración: {calibracion[0]}, Final: {calibracion[1]}')
                suma_total += calibracion[0]
            print(f'Suma total de calibraciones: {suma_total}')
    except FileNotFoundError:
        print(f'Error: El archivo {nombre_archivo} no fue encontrado.')

# Reemplaza 'nombre_del_archivo.txt' con el nombre de tu archivo
procesar_archivo('datitos.txt')
