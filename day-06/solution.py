from functools import reduce 

with open("input.txt", "r") as input_file:
    input = input_file.read().split('\n\n')

def part_one():
    return(sum([len(set(group.replace('\n', ''))) for group in input]))
    
def part_two():
    result = 0
    for group in input:
        sets = 6[set(answer) for answer in group.split('\n') if answer != '']
        result += len(reduce(set.intersection, sets))
    return result 
    
# print(part_one())
print(part_two())
