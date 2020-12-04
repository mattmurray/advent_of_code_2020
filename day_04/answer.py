# --- Day 4: Passport Processing ---
# https://adventofcode.com/2020/day/4

########################################################################################################################
# data prep
########################################################################################################################

def create_passport_dict(l):
    d = {}
    for item in l:
        k, v = item.split(':')
        d[k] = v
    return d

# load data
with open('input.txt', 'r') as f:
    data = [line.strip() for line in f]

# just adding a final blank line to the file because there's a condition later that breaks on a line break
if data[-1] != '':
    data.append('')

# stores the processed dicts
all_passport_details = []

# process text file
individual_credentials = []  # temp list that gets overwritten whenever a blank line is reached
for item in data:
    if len(item) > 0:
        individual_credentials.extend(item.split(' '))

    # hit a line break -> end of individual details
    if len(item) == 0:
        # converts all the items in the list into a dictionary
        passport_dict = create_passport_dict(individual_credentials)
        # and stores in the cleaned list
        all_passport_details.append(passport_dict)
        # empties temp list for next person
        individual_credentials = []

########################################################################################################################
# part 1
########################################################################################################################

expected_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

valid_passports = []  # saves the valid passports for validation in part 2
valid_count = 0
for passport in all_passport_details:
    key_count = 0
    for key in expected_keys:
        if key in passport.keys():
            key_count += 1
        else:
            break

    if key_count == len(expected_keys):
        valid_count += 1
        valid_passports.append(passport)

print(valid_count)  # 208

########################################################################################################################
# part 2
########################################################################################################################

valid_count = 0
for passport in valid_passports:
    conditions_met = 0

    if len(passport['byr']) == 4 and int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002:
        conditions_met += 1
    else:
        continue

    if len(passport['iyr']) == 4 and int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020:
        conditions_met += 1
    else:
        continue

    if len(passport['eyr']) == 4 and int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030:
        conditions_met += 1
    else:
        continue

    if 'cm' in passport['hgt']:
        height_val = int(passport['hgt'].replace('cm', ''))
        if height_val >= 150 and height_val <= 193:
            conditions_met += 1
        else:
            continue

    if 'in' in passport['hgt']:
        height_val = int(passport['hgt'].replace('in', ''))
        if height_val >= 59 and height_val <= 76:
            conditions_met += 1
        else:
            continue

    if passport['hcl'][0] == '#' and len(passport['hcl']) == 7:
        for char in passport['hcl'][1:]:
            if str(char) not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                continue
        conditions_met += 1

    if passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        conditions_met += 1
    else:
        continue

    if len(passport['pid']) == 9:
        try:
            id_int = int(passport['pid'])
            conditions_met += 1
        except:
            continue

    if conditions_met == 7:
        valid_count += 1

print(valid_count)  # 167
