import re


def get_bag(bag_rule):
    return re.sub(r"[\d+\.]", "", bag_rule).strip().replace("bags", "bag")


def find_bag(rules, outer_bag, my_bag):
    curr_rules = rules
    if outer_bag is not None:
        curr_rules = [rule for rule in rules if f"{outer_bag}s contain" in rule]

    bags_found = set()
    for rule in curr_rules:
        outer_bag, inner_bag = rule.split(" contain ")
        if my_bag in inner_bag:
            bags_found.add(outer_bag)
        else:
            for bag in inner_bag.split(","):
                check_inner = find_bag(rules, get_bag(bag), my_bag)
                if len(check_inner) > 0:
                    bags_found.add(outer_bag)
                    break
    return bags_found


def part_one(input):
    return find_bag(input, None, "shiny gold bag")


if __name__ == "__main__":
    with open(
        "/Users/rodbv/code/study/advent-of-code-2020/day-07/input.txt", "r"
    ) as input_file:
        input = input_file.read().splitlines()

    print(len(part_one(input)))
