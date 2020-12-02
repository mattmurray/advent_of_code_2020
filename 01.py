# --- Day 1: Report Repair ---
# https://adventofcode.com/2020/day/1

from itertools import combinations

with open('./inputs/01.txt', 'r') as f:
    num_list = f.readlines()

target = 2020
combination_size = 3

num_list = [int(n) for n in num_list if int(n) < target]
num_list = sorted(num_list)

# num_list = [1721, 979, 366, 299, 675, 1456]

for combo in list(combinations(num_list, combination_size)):
    if sum(combo) == target:
        result = 1
        for num in combo:
            result *= num
        print(result)
        break


