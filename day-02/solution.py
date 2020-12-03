# Problem spec: https://adventofcode.com/2020/day/2

import re

with open("input.txt", "r") as input_file:
    input = [line.strip() for line in input_file.readlines()]


def part_1():
    valid = 0
    for line in input:
        # a typical line looks like this: "1-3 b: cdefg"
        min, max, letter, password = re.split("-|: | ", line)
        letter_count = len(re.findall(letter, password))
        valid += 1 if int(min) <= letter_count <= int(max) else 0

    return valid


def part_2():
    valid = 0
    for line in input:
        spec, password = line.split(": ")
        spec_pos_rule, letter = spec.split()

        pos1, pos2 = map(int, spec_pos_rule.split("-"))
        char1, char2 = password[pos1 - 1], password[pos2 - 1]

        if char1 != char2 and (char1 == letter or char2 == letter):
            valid += 1
    return valid


print(part_1())
print(part_2())