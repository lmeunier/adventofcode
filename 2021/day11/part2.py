with open("input", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines if line.strip()]


class Octopuse:
    def __init__(self, swarm, x, y, energy_level):
        self.swarm = swarm
        self.x = x
        self.y = y
        self.energy_level = energy_level
        self.flashed_this_step = False

    def adjacent_octopuses(self):
        positions = [
            (self.x-1, self.y-1),
            (self.x-1, self.y),
            (self.x-1, self.y+1),
            (self.x, self.y-1),
            (self.x, self.y+1),
            (self.x+1, self.y-1),
            (self.x+1, self.y),
            (self.x+1, self.y+1),
        ]
        return [self.swarm.get(p) for p in positions if self.swarm.get(p)]

    def flash(self):
        # an octopus can only flash at most once per step
        if self.flashed_this_step:
            return

        self.flashed_this_step = True

        # increases the energy level of all adjacent octopuses
        for o in self.adjacent_octopuses():
            o.energy_level += 1

        # flashes octopuses with an energy level greater than 9
        for o in [o for o in self.adjacent_octopuses() if o.energy_level > 9]:
            o.flash()


octopuses = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        octopuses[(x, y)] = Octopuse(octopuses, x, y, int(c))

step = 0
while True:
    # reset flashed status for all octopuses
    for o in octopuses.values():
        o.flashed_this_step = False

    # increase energy level of all octopuses
    for o in octopuses.values():
        o.energy_level += 1

    # find octopuses with energy level greater than 9
    for o in [o for o in octopuses.values() if o.energy_level > 9]:
        o.flash()

    for o in octopuses.values():
        if o.flashed_this_step:
            o.energy_level = 0

    if len([o for o in octopuses.values() if o.flashed_this_step]) == len(octopuses):
        print(step+1)
        break

    step += 1
