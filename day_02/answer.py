# --- Day 2: Password Philosophy ---
# https://adventofcode.com/2020/day/2

# imports
from collections import Counter

# data
with open('input.txt', 'r') as f:
    passwords = [line.strip() for line in f]

########################################################################################################################
# Part 1
########################################################################################################################

valid_passwords = 0
for policy in passwords:
    rules, password = policy.split(': ')
    min_max, letter = rules.split(' ')
    min_val, max_val = min_max.split('-')

    counts = Counter(password)
    letter_count = counts[letter]
    if letter_count >= int(min_val) and letter_count <= int(max_val):
        valid_passwords += 1

print(valid_passwords)

########################################################################################################################
# Part 2
########################################################################################################################

valid_passwords = 0
for policy in passwords:
    rules, password = policy.split(': ')
    min_max, letter = rules.split(' ')
    min_val, max_val = min_max.split('-')

    min_pw_character = password[int(min_val)-1]
    max_pw_character = password[int(max_val)-1]
    letter_count = 0
    for char in [min_pw_character, max_pw_character]:
        if char == letter:
            letter_count += 1

    if letter_count == 1:
        valid_passwords += 1

print(valid_passwords)
