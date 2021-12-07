with open("input", "r") as f:
    lines = f.readlines()

positions = list(map(int, lines[0].strip().split(",")))

position_min = min(positions)
position_max = max(positions)

best_fuel_qty = None
for position in range(position_min, position_max + 1):
    fuel_qty = sum(map(lambda x: abs(x-position), positions))
    if best_fuel_qty is None:
        best_fuel_qty = fuel_qty
    elif fuel_qty < best_fuel_qty:
        best_fuel_qty = fuel_qty

print(best_fuel_qty)
