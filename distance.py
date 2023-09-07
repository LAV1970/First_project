points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}

def calculate_distance(coordinates):
    total_distance = 0
    
    if len(coordinates) <= 1:
        return 0
    
    for i in range(len(coordinates) - 1):
        coord_pair = (coordinates[i], coordinates[i + 1])
        reversed_coord_pair = (coordinates[i + 1], coordinates[i])
        
        if coord_pair in points:
            total_distance += points[coord_pair]
        elif reversed_coord_pair in points:
            total_distance += points[reversed_coord_pair]
    
    return total_distance

coordinates_to_calculate = [0, 1, 3, 2, 0, 2]
total_distance = calculate_distance(coordinates_to_calculate)
print(f"Total distance: {total_distance}")
  