from functools import reduce 

with open("input.txt", "r") as input_file:
    input = input_file.read().split('\n\n')

def part_one():
    return(sum([len(set(group)) for group in input]))
    
def part_two():
    result = 0
    for group in input:
        result += len(reduce(set.intersection, [set(answer) for answer in group.split()]))
    return result 
    
print(part_one())
print(part_two())
