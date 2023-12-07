from itertools import chain, islice

conversion_maps = []

def convert_number(number, conversion_map):
    for dest_start, source_start, length in conversion_map:
        if source_start <= number < source_start + length:
            return dest_start + (number - source_start)
    return number  # If no mapping found, return the original number

def chunked(iterable, size):
    """Chunk an iterable into chunks of the given size."""
    it = iter(iterable)
    return iter(lambda: list(islice(it, size)), [])

def find_lowest_location(initial_seeds, conversion_maps):
    current_numbers = initial_seeds
    block_size = 100  # Set the block size to a reasonable value

    for conversion_map in conversion_maps:
        new_numbers = []
        for block in chunked(current_numbers, block_size):
            converted_block = (convert_number(seed_number, conversion_map) for seed_number in block)
            new_numbers.extend(converted_block)
        current_numbers = new_numbers

    return min(current_numbers)

def pairs_from_list(numbers):
    return [(numbers[i], numbers[i + 1]) for i in range(0, len(numbers), 2)]

def numbers_from_pairs(pairs, block_size=1000):
    result = []
    for start, length in pairs:
        if len(result) + length > block_size:
            yield result
            result = []
        result.extend(range(start, start + length))
    yield result

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
file_path = 'seeds2.txt'
seed_data = read_seed_file(file_path)
conversion_maps.extend([
    seed_data.get("seed_to_soil_map", []),
    seed_data.get("soil_to_fertilizer_map", []),
    seed_data.get("fertilizer_to_water_map", []),
    seed_data.get("water_to_light_map", []),
    seed_data.get("light_to_temperature_map", []),
    seed_data.get("temperature_to_humidity_map", []),
    seed_data.get("humidity_to_location_map", []),
])

seeds = chain.from_iterable(numbers_from_pairs(pairs_from_list(seed_data.get("seeds", []))))

lowest_location = find_lowest_location(seeds, conversion_maps)

print(f"Lowest Location: {lowest_location}")
