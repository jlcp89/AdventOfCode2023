import re

alto = 0
largo = 0
CARACTERES_COMUNES = ['.', ' ', '\n', '\r']
asteriscos = {'coor':(0,0) , 'val': (0,[0])}




def obtenerLineas(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = []
            for linea in archivo:
                lineas.append(linea)

            for j, linea in enumerate(lineas):
                for i, caracter in enumerate(linea):
                    if caracter == '*':
                        asteriscos[(i,j)] = (0, [])
            return lineas

    except FileNotFoundError:
        print(f'Error: El archivo {nombre_archivo} no fue encontrado.')

lineas = obtenerLineas('data.txt')
            # Obtner alto y largo de filas
alto = len(lineas)
largo = len(lineas[0])

def siAsterisco(char, x, y, numero):
    if char == '*':
        if (x, y) in asteriscos:
            ocurrencias, numeros = asteriscos[(x, y)]
            ocurrencias += 1
            numeros.append(numero)
            asteriscos[(x, y)] = (ocurrencias, numeros)
        else:
            asteriscos[(x, y)] = (1, [numero])





def coor_validas(x,y):
    if ((x >= 0) and (x < largo - 1)):
        if y >= 0 and y<alto:
            return True
        else:
            return False
    else:
        return False
    

def calcularGear():
    gear = 0
    for coordenadas, (ocurrencias, numeros) in asteriscos.items():
        if ocurrencias == 2:
            gear += (numeros[0]*numeros[1])
    return gear




def obtener_diccionario_con_coordenadas(cadena):
    matches = re.finditer(r'\d+', cadena)
    return [{"num": int(match.group()), "coor": match.span()} for match in matches]

def numeroValido(coordenada, y, numero):
    numero_valido = False
    xo = coordenada[0]
    xf = coordenada[1]
    caracter = ''
    
    # 1 chequer arriba, esquina superior izquieda
    if coor_validas(xo-1, y-1):
        caracter = lineas[y-1][xo-1]
        if ((caracter not in CARACTERES_COMUNES) and (not caracter.isdigit() )) :
            numero_valido = True
            siAsterisco(caracter, xo-1, y-1, numero)

    # 2 hequer arriba, esquina superior derecha
    if coor_validas(xf+1, y-1):
        caracter = lineas[y-1][xf+1]
        if ((caracter not in CARACTERES_COMUNES) and (not caracter.isdigit() )) :
                numero_valido = True
                siAsterisco(caracter, xf+1, y-1, numero)


    # 3 chequer abajo, esquina inferior izquieda
    if coor_validas(xo-1, y+1):
        caracter = lineas[y+1][xo-1]
        if ((caracter not in CARACTERES_COMUNES) and (not caracter.isdigit() )) :
            numero_valido = True
            siAsterisco(caracter, xo-1, y+1, numero)


    # 4 chequer abajo, esquina inferior derecha
    if coor_validas(xf+1, y+1):
        caracter = lineas[y+1][xf+1]
        if ((caracter not in CARACTERES_COMUNES) and (not caracter.isdigit() )) :
            numero_valido = True
            siAsterisco(caracter, xf+1, y+1, numero)


    # 5 chequer arriba del numero
    if coor_validas(xo, y-1) and coor_validas(xf, y-1):
        for i in range (xo,xf+1):
            caracter = lineas[y-1][i]
            if ((caracter not in CARACTERES_COMUNES) and (not caracter.isdigit() )) :
                numero_valido = True
                siAsterisco(caracter, i, y-1, numero)


    # 6 chequer abajo del numero
    if coor_validas(xo, y+1) and coor_validas(xf, y+1):
        for i in range (xo,xf+1):
            caracter = lineas[y+1][i]
            if ((caracter not in CARACTERES_COMUNES) and (not caracter.isdigit() )) :
                numero_valido = True
                siAsterisco(caracter, i, y+1, numero)


    # 7 chequer izquierda del numero
    if coor_validas(xo-1, y):
        caracter = lineas[y][xo-1]
        if ((caracter not in CARACTERES_COMUNES) and (not caracter.isdigit() )) :
            numero_valido = True
            siAsterisco(caracter, xo-1, y, numero)


    # 8 chequer derecha del numero
    if coor_validas(xf+1, y):
        caracter = lineas[y][xf+1]
        if ((caracter not in CARACTERES_COMUNES) and (not caracter.isdigit() )) :
            numero_valido = True
            siAsterisco(caracter, xf+1, y, numero)
    return numero_valido

def numerosValidos(linea, y):
    numerosConCoordenadas = obtener_diccionario_con_coordenadas(linea.strip())
    numeros_validos = []
    for numero in numerosConCoordenadas:
        coor = (numero["coor"][0], numero["coor"][1] - 1)
        if numeroValido(coor, y, numero['num']):
            numeros_validos.append(int(numero['num']))
    return numeros_validos




def procesar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            # inicializar varibles de estado
            suma_total = 0
            contador_lineas = 0
            #Otener lineas
            
            for linea in lineas:
                numeros_validos = numerosValidos(linea, contador_lineas)
                for numero in numeros_validos:
                    suma_total += int(numero)
                contador_lineas += 1
            #print(f'{asteriscos}')

            print(f'Suma total del Gear: {calcularGear()}')
    except FileNotFoundError:
        print(f'Error: El archivo {nombre_archivo} no fue encontrado.')

# Reemplaza 'nombre_del_archivo.txt' con el nombre de tu archivo
procesar_archivo('data.txt')