#!/usr/bin/env python3
# 2023 Day 10: Pipe Maze

#from ast import literal_eval

def process_input(filename):
    """Acquire input data"""
    with open(filename) as file:
        input = file.read().splitlines()

    maze = {}
    x_len = len(input[0])
    y_len = len(input)

    for y, line in enumerate(input):
        for x, ch in enumerate(line):
            maze[(x,y)] = ch
            if ch == 'S': start = (x,y)

    return maze, x_len, y_len, start


def find_loop():
    """Find all tiles that are on the loop"""
    global start_tile
    steps = 0
    loop = set()
    current = start
    move = 'S'
    start_tile = determine_start_tile()

    while True:
        loop.add(current)
        current, move = next_tile(current, move)
        steps += 1
        if current == start: break
    return loop, steps, start_tile

def next_tile(current, move_dir):
    global start_tile
    cx, cy = current
    from_dir = reverse_dir[move_dir]
    current_tile = maze[current]
    if current == start: current_tile = start_tile
    directions = moves[current_tile]
    for move in directions:
        if move != from_dir:
            new_tile, new_pos = tile_at(current, move)
            return new_pos, move
    return ''

def determine_start_tile():
    directions = ''
    for move in ('N', 'E', 'W', 'S'):
        from_dir = reverse_dir[move]
        next_ch, next_pos = tile_at(start, move)
        if from_dir in moves[next_ch]:
            directions += move
    if directions in ('NS', 'SN'): start_tile = '|'
    elif directions in ('EW', 'WE'): start_tile = '-'
    elif directions in ('NE', 'EN'): start_tile = 'L'
    elif directions in ('NW', 'NW'): start_tile = 'J'
    elif directions in ('SW', 'WS'): start_tile = '7'
    elif directions in ('SE', 'ES'): start_tile = 'F'
    return start_tile


def tile_at(pos, move):
    x, y = pos
    a, b = tile_adjust[move]
    new_pos = (x + a, y + b)
    if new_pos in maze:
        ch = maze[new_pos]
    else:
        ch = '.'
    return ch, new_pos


def count_enclosed():
    enclosed = 0
    for y in range(y_len):
        for x in range(x_len):
            if (x,y) in loop: continue
            if (loop_tiles_to_edge(x,y) % 2) != 0:
                enclosed += 1
    return enclosed

def loop_tiles_to_edge(x, y):
    """Count how many tiles are between the x,y position and the edge of the maze"""
    loop_tiles = 0
    for a in range(0,x):
        if (a,y) in loop:
            weight = 0
            tile = maze[(a,y)]
            if tile == 'S': tile = start_tile
            if tile == '|':
                weight += 1
            elif tile in ('L', '7'):
                weight += .5
            elif tile in ('J', 'F'):
                weight -= .5
            loop_tiles += weight
    return int(loop_tiles)

#-----------------------------------------------------------------------------------------

filename = 'd10_real.txt'
#filename = 'sample5.txt'

maze, x_len, y_len, start = process_input(filename)

moves = {'|':'NS', '-':'EW', 'L':'NE', 'J':'NW', '7':'SW', 'F':'SE', '.':''}
reverse_dir = {'N': 'S', 'S': 'N', 'E':'W', 'W':'E'}
tile_adjust = {'N': (0,-1), 'S': (0,1), 'E':(1,0), 'W':(-1,0)}

loop, loop_len, start_tile = find_loop()


enclosed = count_enclosed()

print('Enclosed:', enclosed)
print()
