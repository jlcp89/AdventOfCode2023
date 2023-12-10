lineas_t = open("d9_real.txt").read().split('\n')
lineas = [list(map(int, line.strip().split(' '))) for line in lineas_t if line.strip()]
total = 0

for linea in lineas:
    noTodosCeros = True
    sub_total = 0
    nuevas_lineas = [linea]

    while noTodosCeros:
        nueva_linea_t = []
        #print (nuevas_lineas)
        
        for i in range (0, len(nuevas_lineas[-1])-1):
            nueva_linea_t.append(nuevas_lineas[-1][i+1]-nuevas_lineas[-1][i] )
            
            

        nuevas_lineas.append(nueva_linea_t)

        if all (numero == 0 for numero  in nuevas_lineas[-1]):
             noTodosCeros = False
    
    for linea in nuevas_lineas:
        total += (linea[-1])
        

print(total)