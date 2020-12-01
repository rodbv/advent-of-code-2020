with open("input.txt", "r") as input_file:
    input = [int(value) for value in input_file.readlines()]

result = [(a, b, a * b) for a in input for b in input if a > b and a + b == 2020]

print(result)