import re

# Problem spec: https://adventofcode.com/2020/day/4

with open("input.txt", "r") as input_file:
    passports = input_file.read().split("\n\n")


def check_height(height):
    if "cm" in height:
        return 150 <= int(height.replace("cm", "")) <= 193
    if "in" in height:
        return 59 <= int(height.replace("in", "")) <= 76
    return False


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
rules = {
    "byr": lambda year: check_year(year, 1920, 2002),
    "iyr": lambda year: check_year(year, 2010, 2020),
    "eyr": lambda year: check_year(year, 2020, 2030),
    "hgt": check_height,
    "hcl": lambda color: bool(re.fullmatch(r"#[a-f0-9]{6}", color)),
    "ecl": lambda color: color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda pid: len(pid) == 9 and pid.isnumeric(),
    "cid": lambda cid: True,
}


def has_required_fields(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return all([f"{field}:" in passport for field in required_fields])


def check_year(year, min, max):
    return len(year) == 4 and min <= int(year) <= max


def passport_is_valid(passport):
    if not has_required_fields(passport):
        return False

    for field in passport.split():
        key, value = field.split(":")
        if not rules[key](value):
            return False
    return True


def part_one():
    return len([p for p in passports if has_required_fields(p)])


def part_two():
    return len([p for p in passports if passport_is_valid(p)])


print(part_two())