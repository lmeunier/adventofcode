with open("input", "r") as f:
    lines = f.readlines()

template = None
rules = {}
pair_count = {}
element_count = {}
for line in lines:
    line = line.strip()
    if not template:
        template = line
        for element in template:
            element_count[element] = element_count.get(element, 0) + 1
        continue

    if not line:
        # empty line between template and rules
        continue

    pair, element = line.split(" -> ")
    rules[pair] = element
    pair_count[pair] = 0

# initialize the `pair_count` dict with the initial template
for i in range(len(template) - 1):
    pair = template[i:i+2]
    pair_count[pair] += 1


for step in range(40):
    for pair, count in pair_count.copy().items():
        # the new element added between the two elements formed by the pair
        element = rules[pair]

        # update the `pair_count` dict
        pair_count[pair] -= count
        pair_count[pair[0] + element] += count
        pair_count[element + pair[1]] += count

        # add the new element in the `element_count` dict
        element_count[element] = element_count.get(element, 0) + count


max_element_qty = max(element_count.values())
min_element_qty = min(element_count.values())
print(max_element_qty - min_element_qty)
