# https://adventofcode.com/2020/day/5

with open("input.txt", "r") as input_file:
    boarding_passes = input_file.read().splitlines()



def to_decimal(code):
    binary = code.strip().replace('B', '1').replace('F', '0').replace('L', '0').replace('R', '1')
    return int(binary, 2)

def seat_id(row, seat):
    return (8 * row) + seat


def get_seat_ids():
    for boarding_pass in boarding_passes:
        row = to_decimal(boarding_pass[:7])
        seat = to_decimal(boarding_pass[-3:])
        yield seat_id(row, seat)
        
def part_one():
    return  max(get_seat_ids())

def  part_two():
    seat_ids = sorted(get_seat_ids())
    min_id = min(seat_ids)
    max_id = max(seat_ids)
    return [seat for seat in range(min_id, max_id) if seat not in seat_ids][0]
    

print(part_one())
print(part_two())