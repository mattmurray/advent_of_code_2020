# --- Day 1: Report Repair ---
# https://adventofcode.com/2020/day/1

# import
from itertools import combinations

# data
with open('input.txt', 'r') as f:
    num_list = f.readlines()

target = 2020
combination_size = 3
num_list = [int(n) for n in num_list if int(n) < target]
num_list = sorted(num_list)

for combo in list(combinations(num_list, combination_size)):
    if sum(combo) == target:
        result = 1
        for num in combo:
            result *= num
        print(result)
        break


