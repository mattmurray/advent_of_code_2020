# --- Day 6: Custom Customs ---
# https://adventofcode.com/2020/day/6

from collections import Counter

def process_forms(l, return_count=False):
    characters = []
    for item in l:
        characters.extend(list(item))

    unique_characters = set(characters)

    if return_count == True:
        return Counter(characters)
    else:
        return unique_characters

# load data
with open('day_06/input.txt', 'r') as f:
    data = [line.strip() for line in f]

# just adding a final blank line to the file because there's a condition later that breaks on a line break
if data[-1] != '':
    data.append('')

########################################################################################################################
# part 1
########################################################################################################################

# stores the processed dicts
all_form_responses = []

group_responses = []
for item in data:

    if len(item) > 0:
        individual_questions = list(item)
        group_responses.extend(individual_questions)

    if len(item) == 0:
        question_responses = process_forms(group_responses, return_count=False)
        all_form_responses.append(question_responses)
        group_responses = []

total_count = 0
for response in all_form_responses:
    total_count += len(response)

print(total_count)

########################################################################################################################
# part 2
########################################################################################################################

# stores the processed dicts
all_form_responses = []

group_responses = []
group_person_count = 0
for item in data:

    if len(item) > 0:
        group_person_count += 1
        individual_questions = list(item)
        group_responses.extend(individual_questions)

    if len(item) == 0:
        all_answered_questions = []
        question_responses = process_forms(group_responses, return_count=True)
        # iterate over all responses and only keep the ones where every person answered yes
        for question_key, count in question_responses.items():
            if count == group_person_count:
                all_answered_questions.extend(question_key)

        all_form_responses.append(all_answered_questions)
        group_responses = []
        group_person_count = 0

total_count = 0
for response in all_form_responses:
    total_count += len(response)

print(total_count)
