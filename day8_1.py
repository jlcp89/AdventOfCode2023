
lines = open("d8_real.txt").read().split('\n')

m, *lines = lines
map = {line.split('=')[0].strip(): tuple(line.split('=')[1].replace('(', '').replace(')', '').split(', ')) for line in lines[1:]}

a, c, i = 'AAA', 0, 0

while a != 'ZZZ':
    a, _ = map[a.strip()] if m[i] == 'L' else map[a.strip()][::-1]  # Eliminar espacios en blanco
    i = (i + 1) % len(m)
    c += 1

print(c)


################################################## primera solución
"""
lines = open("d8_real.txt").read().split('\n')

m = lines[0]
map = {}

for i in range (2, len(lines)):
    linea = lines[i].split('=')
    nodo = linea[0].strip()
    opciones = linea[1].replace('(', '').replace(')','').split(', ')
    iz = opciones[0].strip()
    der = opciones[1].strip()
    map[nodo] = (iz, der)

a = 'AAA'
c = 0
i = 0

while a != 'ZZZ':
    if m[i] == 'L':
        a, _ = map[a]
    elif m[i] == 'R':
        _, a = map[a]

    i += 1
    if i == len(m):
        i = 0

    c += 1
    
print(c)
"""

