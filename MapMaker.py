import random

def generate_ray_caster_map(width, height, num_blocks):
    # Create an empty map
    map_data = [["_" for _ in range(width)] for _ in range(height)]

    # Add border blocks
    for i in range(width):
        map_data[0][i] = "1"
        map_data[height - 1][i] = "1"
    for j in range(height):
        map_data[j][0] = "1"
        map_data[j][width - 1] = "1"

    # Add random blocks
    for _ in range(num_blocks):
        x = random.randint(1, width - 2)
        y = random.randint(1, height - 2)
        map_data[y][x] = random.choice(["1", "2"])

    # Write map data to a text file
    with open("ray_caster_map", "w") as file:
        for row in map_data:
            file.write(",".join(row) + "\n")

# Example usage
#generate_ray_caster_map(20, 10, 15)
