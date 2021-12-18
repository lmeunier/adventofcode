import math
import re

with open("input", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines if line.strip()]


class SnailfishNumber:
    explode_regexp1 = re.compile("([0-9]+,[0-9]+)")
    explode_regexp2 = re.compile("([0-9]+)")
    split_regexp = re.compile("([0-9]+)")
    magnitude_regexp = re.compile("([0-9]+,[0-9]+)")

    def __init__(self, snailfish_number):
        self.snailfish_number = snailfish_number
        self.reduce()

    def add(self, snailfish_number):
        self.snailfish_number = "[{},{}]".format(self.snailfish_number, snailfish_number)
        self.reduce()
        return self

    def explode(self):
        level = 0
        for idx, c in enumerate(self.snailfish_number):
            if c == "[":
                level += 1
            elif c == "]":
                level -= 1
            if level == 5:
                break

        if level != 5:
            return self, False

        after_pair = self.snailfish_number[idx+1:]
        pair = self.explode_regexp1.findall(after_pair)[0]
        pair_index = after_pair.find(pair)
        before_pair = self.snailfish_number[:idx+pair_index]
        after_pair = self.snailfish_number[idx+pair_index+2+len(pair):]

        previous_numbers = self.explode_regexp2.findall(before_pair)
        previous_number = None
        if previous_numbers:
            previous_number = previous_numbers[-1]
            new_previous_number = int(pair.split(",")[0]) + int(previous_number)
            before_pair = str(new_previous_number).join(before_pair.rsplit(previous_number, 1))

        next_numbers = self.explode_regexp2.findall(after_pair)
        next_number = None
        if next_numbers:
            next_number = next_numbers[0]
            new_next_number = int(pair.split(",")[1]) + int(next_number)
            after_pair = after_pair.replace(next_number, str(new_next_number), 1)

        self.snailfish_number = before_pair + "0" + after_pair
        return self, True

    def split(self):
        found = False
        for number in self.split_regexp.findall(self.snailfish_number):
            if int(number) >= 10:
                found = True
                break

        if not found:
            return self, False

        idx = self.snailfish_number.find(number)
        new_pair = "[{},{}]".format(
            math.floor(int(number) / 2),
            math.ceil(int(number) / 2)
        )

        self.snailfish_number = self.snailfish_number[:idx] + new_pair + self.snailfish_number[(idx+len(number)):]
        return self, True

    def reduce(self):
        changed = True
        while changed:
            _, changed = self.explode()
            if changed:
                continue
            _, changed = self.split()
        return self

    def magnitude(self):
        sn = self.snailfish_number
        while True:
            for pair in self.magnitude_regexp.findall(sn):
                pair = pair.split(",")
                sn = sn.replace(
                    "[{},{}]".format(pair[0], pair[1]),
                    str(3 * int(pair[0]) + 2 * int(pair[1])),
                    1
                )
            if not "[" in sn:
                return int(sn)


sn = None
for line in lines:
    if sn is None:
        sn = SnailfishNumber(line)
    else:
        sn.add(line)

print(sn.magnitude())
