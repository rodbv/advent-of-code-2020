# Problem spec: https://adventofcode.com/2020/day/3


with open("input.txt", "r") as input_file:
    input = [line.strip() for line in input_file.readlines()]

TREE = "#"
repeat_width = len(input[0])


def traverse(steps_right, steps_down):
    trees_found = 0
    x_position = 0
    for line in input[::steps_down]:
        tree_or_space_pos = x_position % repeat_width
        tree_or_space = line[tree_or_space_pos]
        if tree_or_space == TREE:
            trees_found += 1
        x_position += steps_right
    return trees_found


print("Part 1:", traverse(3, 1))
print(
    "Part 2:",
    traverse(1, 1) * traverse(3, 1) * traverse(5, 1) * traverse(7, 1) * traverse(1, 2),
)
