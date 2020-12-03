# Problem spec: https://adventofcode.com/2020/day/2

from re import findall

with open("input.txt", "r") as input_file:
    input = [line.strip() for line in input_file.readlines()]


def part_1(data):
    valid = 0
    for line in data:
        spec, password = line.split(": ")
        spec_len_rule, letter = spec.split()

        min, max = map(int, spec_len_rule.split("-"))

        letter_count = len(findall(letter, password))
        if letter_count >= min and letter_count <= max:
            valid += 1
    return valid


def part_2(data):
    valid = 0
    for line in data:
        spec, password = line.split(": ")
        spec_pos_rule, letter = spec.split()

        pos1, pos2 = map(int, spec_pos_rule.split("-"))
        char1, char2 = password[pos1 - 1], password[pos2 - 1]

        if char1 != char2 and (char1 == letter or char2 == letter):
            valid += 1
    return valid


print(part_1(input))
print(part_2(input))