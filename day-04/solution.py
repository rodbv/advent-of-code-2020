# Problem spec: https://adventofcode.com/2020/day/4

with open("input.txt", "r") as input_file:
    passports = (
        input_file.read()
        .replace("\n\n", "%%")
        .replace("\n", " ")
        .replace("%%", "\n")
        .split("\n")
    )


def part_one():
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return len(
        [
            passport
            for passport in passports
            if all([f"{key}:" in passport for key in required_fields])
        ]
    )


print(part_one())