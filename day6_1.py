def convert_to_tuples(time_values, distance_values):
    if len(time_values) != len(distance_values):
        raise ValueError("La cantidad de valores de tiempo y distancia debe ser la misma.")
    result = list(zip(time_values, distance_values))
    return result

def calculate_ways_to_win(time_distance_tuples):
    total_ways_to_win = 1
    for time, distance in time_distance_tuples:
        ways_to_win = 0
        aceleracion = 1 # m/s
        for i in range(0,time):
            velocidad = i * aceleracion
            distancia = velocidad * (time - i)
            if distancia > distance:
                ways_to_win += 1
        total_ways_to_win *= ways_to_win
        print(f'Carrera: {time},{distance}  Maneras: {ways_to_win}')
    return total_ways_to_win


def read_values_from_file(file_path):
    with open(file_path, 'r') as file:
        time_line = file.readline().strip()
        distance_line = file.readline().strip()

    if not time_line.startswith("Time:") or not distance_line.startswith("Distance:"):
        raise ValueError("El formato del archivo no es válido.")

    time_values = list(map(int, time_line[len("Time:"):].split()))
    distance_values = list(map(int, distance_line[len("Distance:"):].split()))

    return convert_to_tuples(time_values, distance_values)

# Ejemplo de uso con el archivo botes1.txt
file_path = 'botes3.txt'
tuples_result = read_values_from_file(file_path)
result = calculate_ways_to_win(tuples_result)

print(result)
