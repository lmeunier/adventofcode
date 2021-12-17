import re

with open("input", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines if line.strip()]


class TargetArea:
    def __init__(self, desc_str):
        target_area_regexp = re.compile("target area: x=([0-9]+)\\.\\.([0-9]+), y=(-[0-9]+)\\.\\.(-[0-9]+)")
        bounds = target_area_regexp.findall(desc_str)[0]
        self.x_bounds = (int(bounds[0]), int(bounds[1]))
        self.y_bounds = (int(bounds[2]), int(bounds[3]))

    def point_inside(self, x, y):
        return self.x_bounds[0] <= x <= self.x_bounds[1] and self.y_bounds[0] <= y <= self.y_bounds[1]

    def point_beyond(self, x, y):
        return x > max(self.x_bounds) or y < min(self.y_bounds)


ta = TargetArea(lines[0])
initial_velocitiy_values = []

for ivx in range(1, max(ta.x_bounds) + 1):
    # iterate over Initial Velocity X (ivx)
    # the maximum ivx value is the furthest side of the target area (on the X axis)

    for ivy in range(min(ta.y_bounds), max(abs(ta.y_bounds[0]), abs(ta.y_bounds[1]))):
        # iterate over Initial Velocity Y (ivy)
        #
        # the Initial Velocity Y (ivy) starts at the deepest side of the target area (on the Y axis)
        #
        # there is always a step with y=0 (whatever ivy is)
        # so there is no point trying ivy greater than the deepest side of
        # target area as we are sure the probe will always miss
        # this is the end of the `while True` loop over ivy

        # probe's initial position and velocity
        x = 0
        y = 0
        vy = ivy
        vx = ivx

        while not ta.point_beyond(x, y):
            # update probe's position
            x += vx
            y += vy

            if ta.point_inside(x, y):
                # the probe landed insed the target area
                initial_velocitiy_values.append((ivx, ivy))
                break

            # update vx and vy
            if vx > 0:
                vx -= 1
            elif vx < 0:
                vx += 1
            vy -= 1


print(len(initial_velocitiy_values))
