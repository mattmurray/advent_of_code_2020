# --- Day 3: Toboggan Trajectory ---
# https://adventofcode.com/2020/day/3

# data
with open('input.txt', 'r') as f:
    data = [line.strip() for line in f]

# create list of lists
data = [list(row) for row in data]

# simple function to check the coordinates of the numpy array
def check_for_tree(tree_map, coords):
    char = tree_map[coords[0]][coords[1]]
    if char == '#':
        return 1
    else:
        return 0

def traverse(right, down, data):
    counter = 0
    max_rows = len(data)
    max_cols = len(data[0])
    coords = (0, 0)

    # loop over array and update counter
    for i in range(0, max_rows):
        new_row = coords[0] + down
        new_col = coords[1] + right

        if new_col >= max_cols:
            new_col = new_col - max_cols

        if new_row >= max_rows:
            break

        coords = (new_row, new_col)
        counter += check_for_tree(data, coords)

    return counter

########################################################################################################################
# Part 1
########################################################################################################################

result = traverse(right=3, down=1, data=data)

print(result)  # 162

########################################################################################################################
# Part 2
########################################################################################################################

slopes = [
    (1, 1),  # right 1, down 1
    (3, 1),  # right 3, down 1
    (5, 1),  # right 5, down 1
    (7, 1),  # right 7, down 1
    (1, 2)   # right 1, down 2
]

results = []
for slope in slopes:
    result = traverse(right=slope[0], down=slope[1], data=data)
    results.append(result)

answer = 1
for num in results:
    answer *= num

print(answer)  # 3064612320

