# Problem spec: https://adventofcode.com/2020/day/4

with open("input.txt", "r") as input_file:
    passports = input_file.read().split("\n\n")


def part_one():
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return len(
        [
            passport
            for passport in passports
            if all([f"{field}:" in passport for field in required_fields])
        ]
    )


import re


def check_height(height):
    if "cm" in height:
        return 150 <= int(height.replace("cm", "")) <= 193
    if "in" in height:
        return 59 <= int(height.replace("in", "")) <= 76
    return False


def part_two():
    """
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    """

    check_year = lambda year, min, max: len(year) == 4 and min <= int(year) <= max

    rules = {
        "byr": lambda year: check_year(year, 1920, 2002),
        "iyr": lambda year: check_year(year, 2010, 2020),
        "eyr": lambda year: check_year(year, 2020, 2030),
        "hgt": check_height,
        "hcl": lambda color: re.fullmatch(r"#[a-f0-9]{6}", color),
        "ecl": lambda color: color in "amb blu brn gry grn hzl oth".split(),
        "pid": lambda pid: len(pid) == 9 and pid.isnumeric(),
        "cid": lambda cid: True,
    }

    for passport in passports[0:1]:
        for field in passport.split():
            print("checking", field)
            key, value = field.split(":")
            is_valid = rules[key](value)
            print("=> valid!" if is_valid else "=> not valid")


print(part_two())