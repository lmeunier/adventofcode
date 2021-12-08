import re

with open("input", "r") as f:
    lines = f.readlines()

digits_regexp = re.compile("([a-z]+)")

def all_chars_in_str(chars, digit):
    for c in chars:
        if c not in digit:
            return False
    return True

def determine_segments(digits):
    """
    Segments:

      0000
     1    2
     1    2
      3333
     4    5
     4    5
      6666
    """
    segments = [""] * 7

    # one
    one = [d for d in digits if len(d) == 2][0]
    segments[2] = [c for c in one]
    segments[5] = [c for c in one]

    # seven
    seven = [d for d in digits if len(d) == 3][0]
    segments[0] = [c for c in seven if c not in one]

    # four
    four = [d for d in digits if len(d) == 4][0]
    segments[1] = [c for c in four if c not in one]
    segments[3] = [c for c in four if c not in one]

    # three
    three = [d for d in digits if len(d) == 5 and all_chars_in_str(segments[0], d) and all_chars_in_str(segments[2], d)][0]
    segments[6] = [c for c in three if c not in segments[0] and c not in segments[2] and c not in segments[3]]
    segments[3] = [c for c in three if c not in segments[0] and c not in segments[2] and c not in segments[6]]
    segments[1] = [c for c in segments[1] if c not in segments[3]]
    segments[4] = [c for c in "abcdefg" if c not in [c for s in segments for c in s]]

    # two
    two = [d for d in digits if len(d) == 5 and all_chars_in_str(segments[0], d) and all_chars_in_str(segments[3], d)
    and all_chars_in_str(segments[4], d) and all_chars_in_str(segments[6], d)][0]
    segments[5] = [c for c in segments[5] if c not in two]
    segments[2] = [c for c in segments[2] if c not in segments[5]]

    return [c for s in segments for c in s]

def chars_to_digit(chars, segments):
    # zero
    if len(chars) == 6 and all_chars_in_str([segments[n] for n in [0, 1, 2, 4, 5, 6]], chars):
        return "0"

    # one
    if len(chars) == 2:
        return "1"

    # two
    if len(chars) == 5 and all_chars_in_str([segments[n] for n in [0, 2, 3, 4, 6]], chars):
        return "2"
    
    # three
    if len(chars) == 5 and all_chars_in_str([segments[n] for n in [0, 2, 3, 5, 6]], chars):
        return "3"

    # four
    if len(chars) == 4:
        return "4"
    
    # five
    if len(chars) == 5 and all_chars_in_str([segments[n] for n in [0, 1, 3, 5, 6]], chars):
        return "5"
    
    # six
    if len(chars) == 6 and all_chars_in_str([segments[n] for n in [0, 1, 3, 4, 5, 6]], chars):
        return "6"

    # seven
    if len(chars) == 3:
        return "7"

    # eight
    if len(chars) == 7:
        return "8"

    # nine
    if len(chars) == 6 and all_chars_in_str([segments[n] for n in [0, 1, 2, 3, 5, 6]], chars):
        return "9"

    print(chars, segments)

count = 0
for line in lines:
    digits = digits_regexp.findall(line)
    segments = determine_segments(digits)

    digits = line.split("|")[1].strip().split(" ")
    digit = int("".join([chars_to_digit(d, segments) for d in digits]))
    count += digit

print(count)
