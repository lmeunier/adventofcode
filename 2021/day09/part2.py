import math


class Location:
    def __init__(self, x, y, height, visited):
        self.x = x
        self.y = y
        self.height = height
        self.visited = visited


def find_basin_locations(hm, current_location, basin_locations):
    surrounding_locations = [
        hm.get((current_location.x, current_location.y-1)),
        hm.get((current_location.x, current_location.y+1)),
        hm.get((current_location.x-1, current_location.y)),
        hm.get((current_location.x+1, current_location.y))
    ]

    for location in surrounding_locations:
        if location and not location.visited:
            basin_locations.append(location)
            location.visited = True
            find_basin_locations(hm, location, basin_locations)

    return basin_locations


with open("input", "r") as f:
    lines = f.readlines()

hm = {}
max_x = len(lines)
max_y = len(lines[0].strip())
for x, line in enumerate(lines):
    for y, height in enumerate(line.strip()):
        hm[(x, y)] = Location(x, y, int(height), int(height) == 9)

basin_sizes = []
for x in range(max_x):
    for y in range(max_y):
        location = hm.get((x, y))

        if location.visited:
            continue

        location.visited = True
        locations = find_basin_locations(hm, location, [location])
        basin_sizes.append(len(locations))

print(math.prod(sorted(basin_sizes)[-3:]))
