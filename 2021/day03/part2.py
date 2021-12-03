with open("input", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines if line.strip()]

def count_ones(lines, position):
    return len([1 for line in lines if line[position] == "1"])

def most_common_value(lines, position):
    count_1 = count_ones(lines, position)
    if count_1 < len(lines) / 2:
        return "0"
    return "1"

def least_common_value(lines, position):
    count_1 = count_ones(lines, position)
    if count_1 < len(lines) / 2:
        return "1"
    return "0"

def filter_lines(lines, position, value):
    return [line for line in lines if line[position] == value]

def find_rating(lines, op):
    filtered_lines = lines.copy()
    for i in range(len(lines[0])):
        position = i
        filter_value = op(filtered_lines, position)
        filtered_lines = filter_lines(filtered_lines, position, filter_value)
        if len(filtered_lines) == 1:
            break
    return int(filtered_lines[0], 2)

oxygen_generator_rating = find_rating(lines, most_common_value)
co2_scrubber_rating = find_rating(lines, least_common_value)

print(oxygen_generator_rating * co2_scrubber_rating)
