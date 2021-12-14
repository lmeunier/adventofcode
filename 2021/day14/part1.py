from collections import Counter

with open("input", "r") as f:
    lines = f.readlines()

template = None
rules = {}
for line in lines:
    line = line.strip()
    if not template:
        template = line
        continue

    if not line:
        # empty line between template and rules
        continue

    pair, element = line.split(" -> ")
    rules[pair] = element


for step in range(10):
    new_template = template[0]
    for i in range(len(template) - 1):
        pair = template[i:i+2]
        new_template += rules[pair] + pair[1]
    template = new_template

elements_count = Counter(template).items()
max_element_qty = max([qty for element, qty in elements_count])
min_element_qty = min([qty for element, qty in elements_count])
print(max_element_qty - min_element_qty)
