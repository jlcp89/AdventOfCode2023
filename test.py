linea = "41 48 83 86 17 | 83 86  6 31 17  9 48 53"

lineas_numeros = linea.split('|')
lineas_numeros[0] = lineas_numeros[0].strip()
lineas_numeros[1] = lineas_numeros[1].strip()

numeros_ganadores = lineas_numeros[0].split(" ")
numeros_actuales = lineas_numeros[1].split(" ")

print (f'{numeros_actuales}')