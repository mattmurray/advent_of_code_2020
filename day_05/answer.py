# --- Day 5: Binary Boarding ---
# https://adventofcode.com/2020/day/5

# load data
with open('input.txt', 'r') as f:
    data = [line.strip() for line in f]

def parse_string(s, range_min, range_max, upper_char, lower_char):
    all_seats = list(range(range_min, range_max))

    for char in list(s):
        num_seats = len(all_seats)
        mid_point = num_seats // 2
        if char == lower_char:
            all_seats = all_seats[:mid_point]

        if char == upper_char:
            all_seats = all_seats[mid_point:]

    return all_seats[0]

# process data into list of dicts
results = []
for s in data:
    row_string = s[:-3]
    seat_string = s[-3:]

    row_number = parse_string(row_string, 0, 128, 'B', 'F')
    seat_number = parse_string(seat_string, 0, 8, 'R', 'L')
    seat_id = (row_number * 8) + seat_number

    seat_data = {
        'row_number': row_number,
        'seat_number': seat_number,
        'seat_id': seat_id
    }
    results.append(seat_data)

########################################################################################################################
# part 1
########################################################################################################################

# go through all parsed data and get all seat ids
all_seat_ids = set()
for boarding_pass in results:
    all_seat_ids.add(boarding_pass['seat_id'])

seat_id_min = min(all_seat_ids)
seat_id_max = max(all_seat_ids)

print(seat_id_max)  # 855

########################################################################################################################
# part 2
########################################################################################################################

# find missing seat id(s) between the min and max seat ids already processed
missing_seat_ids = set()
for id in range(seat_id_min, seat_id_max):
    if id not in all_seat_ids:
        missing_seat_ids.add(id)

print(missing_seat_ids)  # {552}
