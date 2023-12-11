#!/usr/bin/env python3
# 2023 Day 10: Pipe Maze

# Importación comentada y no utilizada
# from ast import literal_eval

def process_input(filename):
    """Adquiere los datos de entrada"""
    with open(filename) as file:
        # Lee el contenido del archivo, divide las líneas y lo almacena en la variable 'input'
        input = file.read().splitlines()

    maze = {}  # Inicializa un diccionario para representar el laberinto
    x_len = len(input[0])  # Calcula la longitud del laberinto en la dirección x
    y_len = len(input)  # Calcula la longitud del laberinto en la dirección y

    for y, line in enumerate(input):
        for x, ch in enumerate(line):
            # Llena el diccionario 'maze' con las posiciones y caracteres del laberinto
            maze[(x, y)] = ch
            # Encuentra la posición inicial (x, y) cuando el carácter es 'S'
            if ch == 'S':
                start = (x, y)

    return maze, x_len, y_len, start  # Devuelve el laberinto, longitudes y posición inicial como una tupla


def find_loop():
    """Encuentra todas las casillas que forman el bucle"""
    global start_tile  # Declara una variable global 'start_tile'
    steps = 0  # Inicializa el contador de pasos
    loop = set()  # Inicializa un conjunto para almacenar las casillas del bucle
    current = start  # Inicializa la posición actual con la posición inicial
    move = 'S'  # Inicializa la dirección de movimiento con 'S'
    start_tile = determine_start_tile()  # Llama a la función para determinar el tipo de casilla en la posición inicial

    while True:
        loop.add(current)  # Agrega la posición actual al conjunto 'loop'
        current, move = next_tile(current, move)  # Calcula la siguiente casilla y dirección de movimiento
        steps += 1  # Incrementa el contador de pasos
        if current == start:
            break  # Sale del bucle cuando se regresa a la posición inicial

    return loop, steps, start_tile  # Devuelve el conjunto del bucle, número de pasos y tipo de casilla en la posición inicial


def next_tile(current, move_dir):
    global start_tile  # Accede a la variable global 'start_tile'
    cx, cy = current  # Desempaqueta la posición actual en coordenadas x e y
    from_dir = reverse_dir[move_dir]  # Obtiene la dirección opuesta a la dirección de movimiento
    current_tile = maze[current]  # Obtiene el tipo de casilla en la posición actual

    if current == start:
        current_tile = start_tile  # Si la posición actual es la posición inicial, utiliza el tipo de casilla en la posición inicial

    directions = moves[current_tile]  # Obtiene las direcciones permitidas desde la casilla actual

    for move in directions:
        if move != from_dir:
            new_tile, new_pos = tile_at(current, move)  # Calcula la casilla y posición después del movimiento
            return new_pos, move  # Devuelve la nueva posición y dirección de movimiento

    return ''  # Devuelve una cadena vacía si no hay una nueva posición válida


def determine_start_tile():
    directions = ''  # Inicializa una cadena para almacenar las direcciones permitidas
    for move in ('N', 'E', 'W', 'S'):
        from_dir = reverse_dir[move]  # Obtiene la dirección opuesta a la dirección de movimiento actual
        next_ch, next_pos = tile_at(start, move)  # Calcula la casilla y posición después del movimiento
        if from_dir in moves[next_ch]:
            directions += move  # Agrega la dirección actual si es válida

    # Determina el tipo de casilla en la posición inicial según las direcciones permitidas
    if directions in ('NS', 'SN'):
        start_tile = '|'
    elif directions in ('EW', 'WE'):
        start_tile = '-'
    elif directions in ('NE', 'EN'):
        start_tile = 'L'
    elif directions in ('NW', 'NW'):
        start_tile = 'J'
    elif directions in ('SW', 'WS'):
        start_tile = '7'
    elif directions in ('SE', 'ES'):
        start_tile = 'F'

    return start_tile  # Devuelve el tipo de casilla en la posición inicial


def tile_at(pos, move):
    x, y = pos  # Desempaqueta la posición en coordenadas x e y
    a, b = tile_adjust[move]  # Obtiene los ajustes correspondientes a la dirección de movimiento
    new_pos = (x + a, y + b)  # Calcula la nueva posición después del movimiento

    if new_pos in maze:
        ch = maze[new_pos]  # Obtiene el carácter en la nueva posición si está en el laberinto
    else:
        ch = '.'  # Utiliza un punto si la nueva posición está fuera del laberinto

    return ch, new_pos  # Devuelve el carácter y la nueva posición


def count_enclosed():
    enclosed = 0  # Inicializa el contador de casillas cerradas

    for y in range(y_len):
        for x in range(x_len):
            # Ignora las casillas que forman parte del bucle
            if (x, y) in loop:
                continue

            # Verifica si el número de casillas hasta el borde es impar
            if (loop_tiles_to_edge(x, y) % 2) != 0:
                enclosed += 1  # Incrementa el contador si el número es impar

    return enclosed  # Devuelve el número de casillas cerradas


def loop_tiles_to_edge(x, y):
    """Cuenta cuántas casillas hay entre la posición (x, y) y el borde del laberinto"""
    loop_tiles = 0  # Inicializa el contador de casillas hasta el borde

    for a in range(0, x):
        if (a, y) in loop:
            weight = 0  # Inicializa el peso de la casilla
            tile = maze[(a, y)]  # Obtiene el tipo de casilla en la posición actual

            if tile == 'S':
                tile = start_tile  # Utiliza el tipo de casilla en la posición inicial si la posición actual es la posición inicial

            # Asigna un peso según el tipo de casilla
            if tile == '|':
                weight += 1
            elif tile in ('L', '7'):
                weight += 0.5
            elif tile in ('J', 'F'):
                weight -= 0.5

            loop_tiles += weight  # Incrementa el contador de casillas hasta el borde

    return int(loop_tiles)  # Devuelve el número de casillas hasta el borde como un entero


#-----------------------------------------------------------------------------------------

# Especifica el nombre del archivo de entrada
filename = 'd10_real.txt'
#filename = 'sample5.txt'

# Procesa la entrada y obtiene el laberinto, longitudes y posición inicial
maze, x_len, y_len, start = process_input(filename)

# Diccionarios utilizados en el recorrido del laberinto
moves = {'|': 'NS', '-': 'EW', 'L': 'NE', 'J': 'NW', '7': 'SW', 'F': 'SE', '.': ''}
reverse_dir = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
tile_adjust = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}

# Encuentra el bucle en el laberinto
loop, loop_len, start_tile = find_loop()

# Cuenta el número de casillas cerradas
enclosed = count_enclosed()

# Imprime el resultado
print('Enclosed:', enclosed)
print()
