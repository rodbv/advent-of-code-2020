# Problem spec: https://adventofcode.com/2020/day/2

import re

with open("input.txt", "r") as input_file:
    input = [line.strip() for line in input_file.readlines()]


def get_line_rule(line):
    """
    Splits a line from input that has the following pattern:
    1-3 b: cdefg
    into value1 (1), value2 (3), letter (b) and password (cdefg)
    """
    value1, value2, letter, password = re.split("-|: | ", line)
    return int(value1), int(value2), letter, password


def part_1():
    valid = 0
    for line in input:
        min, max, letter, password = get_line_rule(line)
        letter_count = len(re.findall(letter, password))
        valid += 1 if min <= letter_count <= max else 0

    return valid


def part_2():
    valid = 0
    for line in input:
        pos1, pos2, letter, password = get_line_rule(line)
        char1, char2 = password[pos1 - 1], password[pos2 - 1]

        if char1 != char2 and (char1 == letter or char2 == letter):
            valid += 1

    return valid


print(part_1())
print(part_2())