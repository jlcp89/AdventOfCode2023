def convert_number(number, conversion_map):
    for dest_start, source_start, length in conversion_map:
        if source_start <= number < source_start + length:
            return dest_start + (number - source_start)
    return number  # If no mapping found, return the original number

conversion_maps = []

def find_lowest_location(initial_seeds, conversion_maps):
    current_numbers = initial_seeds

    for conversion_map in conversion_maps:
        new_numbers = []

        for seed_number in current_numbers:
            new_number = convert_number(seed_number, conversion_map)
            new_numbers.append(new_number)

        current_numbers = new_numbers

    return min(current_numbers)

def read_seed_file(file_path):
    seed_data = {
        "seeds": [],
        "seed_to_soil_map": [],
        "soil_to_fertilizer_map": [],
        "fertilizer_to_water_map": [],
        "water_to_light_map": [],
        "light_to_temperature_map": [],
        "temperature_to_humidity_map": [],
        "humidity_to_location_map": [],
    }
    current_map_key = None

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if line.startswith("seeds:"):
                seed_data["seeds"] = list(map(int, line[len("seeds:"):].strip().split()))
            elif line.endswith(" map:"):
                current_map_key = line.split(':')[0].replace(" ", "_").lower()
                current_map_key = current_map_key.replace("-", "_")
            elif line:
                seed_data[current_map_key].append(tuple(map(int, line.split())))

    return seed_data

# Example usage:
file_path = 'seeds.txt'
seed_data = read_seed_file(file_path)
conversion_maps.append(seed_data.get("seed_to_soil_map", []))
conversion_maps.append(seed_data.get("soil_to_fertilizer_map", []))
conversion_maps.append(seed_data.get("fertilizer_to_water_map", []))
conversion_maps.append(seed_data.get("water_to_light_map", []))
conversion_maps.append(seed_data.get("light_to_temperature_map", []))
conversion_maps.append(seed_data.get("temperature_to_humidity_map", []))
conversion_maps.append(seed_data.get("humidity_to_location_map", []))

lowest_location = find_lowest_location(seed_data.get("seeds", []), conversion_maps)

print(f"Lowest Location: {lowest_location}")

# Access the parsed data
"""
print("Seeds:", seed_data.get("seeds", []))
print("Seed to Soil Map:", seed_data.get("seed_to_soil_map", []))
print("Soil to Fertilizer Map:", seed_data.get("soil_to_fertilizer_map", []))
print("Fertilizer to Water Map:", seed_data.get("fertilizer_to_water_map", []))
print("Water to Light Map:", seed_data.get("water_to_light_map", []))
print("Light to Temperature Map:", seed_data.get("light_to_temperature_map", []))
print("Temperature to Humidity Map:", seed_data.get("temperature_to_humidity_map", []))
print("Humidity to Location Map:", seed_data.get("humidity_to_location_map", []))
"""
