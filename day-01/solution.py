with open("input.txt", "r") as input_file:
    input = [int(value) for value in input_file.readlines()]

result_part_one = [
    (a, b, a * b) for a in input for b in input if a > b and a + b == 2020
]

result_part_two = [
    (a, b, c, a * b * c)
    for a in input
    for b in input
    for c in input
    if a > b and b > c and a + b + c == 2020
]

print(result_part_one)
print(result_part_two)