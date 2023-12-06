import re

alto = 0
largo = 0
CARACTERES_COMUNES = ['.', ' ', '\n', '\r']



def obtenerLineas(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = []
            for linea in archivo:
                lineas.append(linea)
            return lineas

    except FileNotFoundError:
        print(f'Error: El archivo {nombre_archivo} no fue encontrado.')

lineas = obtenerLineas('data.txt')
            # Obtner alto y largo de filas
alto = len(lineas)
largo = len(lineas[0])



def coor_validas(x,y):
    if ((x >= 0) and (x < largo - 1)):
        if y >= 0 and y<alto:
            return True
        else:
            return False
    else:
        return False



def obtener_diccionario_con_coordenadas(cadena):
    matches = re.finditer(r'\d+', cadena)
    return [{"num": int(match.group()), "coor": match.span()} for match in matches]

def numeroValido(coordenada, y):
    numero_valido = False
    xo = coordenada[0]
    xf = coordenada[1]
    caracter = ''
    
    # 1 chequer arriba, esquina superior izquieda
    if coor_validas(xo-1, y-1):
        caracter = lineas[y-1][xo-1]
        if ((caracter not in CARACTERES_COMUNES) and (not caracter.isdigit() )) :
            numero_valido = True
            print(f' arriba izquieda: {lineas[y][xo]}')

    # 2 hequer arriba, esquina superior derecha
    if coor_validas(xf+1, y-1):
        caracter = lineas[y-1][xf+1]
        if ((caracter not in CARACTERES_COMUNES) and (not caracter.isdigit() )) :
                numero_valido = True
                print(f' arriba derecha : : {xf+1} , {y-1}')

    # 3 chequer abajo, esquina inferior izquieda
    if coor_validas(xo-1, y+1):
        caracter = lineas[y+1][xo-1]
        if ((caracter not in CARACTERES_COMUNES) and (not caracter.isdigit() )) :
            numero_valido = True
            print(f' abajo izquieda: {lineas[y][xo]} ')

    # 4 chequer abajo, esquina inferior derecha
    if coor_validas(xf+1, y+1):
        caracter = lineas[y+1][xf+1]
        if ((caracter not in CARACTERES_COMUNES) and (not caracter.isdigit() )) :
            numero_valido = True
            print(f' abajo derecha : caracter -{caracter}- numero {lineas[y][xf]}')

    # 5 chequer arriba del numero
    if coor_validas(xo, y-1) and coor_validas(xf, y-1):
        for i in range (xo,xf+1):
            caracter = lineas[y-1][i]
            if ((caracter not in CARACTERES_COMUNES) and (not caracter.isdigit() )) :
                numero_valido = True
                print(f'arriba  : {lineas[y][i]}')

    # 6 chequer abajo del numero
    if coor_validas(xo, y+1) and coor_validas(xf, y+1):
        for i in range (xo,xf+1):
            caracter = lineas[y+1][i]
            if ((caracter not in CARACTERES_COMUNES) and (not caracter.isdigit() )) :
                numero_valido = True
                print(f' abajo : {lineas[y][i]}')

    # 7 chequer izquierda del numero
    if coor_validas(xo-1, y):
        caracter = lineas[y][xo-1]
        if ((caracter not in CARACTERES_COMUNES) and (not caracter.isdigit() )) :
            numero_valido = True
            print(f'  izquierda : {lineas[y][xo]}')

    # 8 chequer derecha del numero
    if coor_validas(xf+1, y):
        print(f' derecha : {alto} {xf+1} {y}')
        caracter = lineas[y][xf+1]
        if ((caracter not in CARACTERES_COMUNES) and (not caracter.isdigit() )) :
            numero_valido = True
            print(f' derecha : {lineas[y][xf]}')
                
    return numero_valido

def numerosValidos(linea, y):
    numerosConCoordenadas = obtener_diccionario_con_coordenadas(linea.strip())
    numeros_validos = []
    for numero in numerosConCoordenadas:
        coor = (numero["coor"][0], numero["coor"][1] - 1)
        if numeroValido(coor, y):
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
                
                print(f' {linea} ')

                numeros_validos = numerosValidos(linea, contador_lineas)
                for numero in numeros_validos:
                    suma_total += int(numero)
                    print(f' {numero} ')
                contador_lineas += 1

            print(f'Suma total de numero validos: {suma_total}')
    except FileNotFoundError:
        print(f'Error: El archivo {nombre_archivo} no fue encontrado.')

# Reemplaza 'nombre_del_archivo.txt' con el nombre de tu archivo
procesar_archivo('data.txt')