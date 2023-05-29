import csv
import random
import pandas as pd
import argparse

# Create parser and define argument
parser = argparse.ArgumentParser(description='Read people data from a CSV file and create groups.')
parser.add_argument('filename', type=str, help='The name of the CSV file')
parser.add_argument('num_groups', type=int, help='The number of groups to create')
parser.add_argument('group_size', type=int, help='The size of each group (except possibly the last one)')

# Parse arguments
args = parser.parse_args()

# Read data from CSV file
data = []
with open(args.filename, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)  # We use DictReader to convert each row to a dictionary
    for row in reader:
        if row['known']:  # Convert comma-separated 'known' to a list, if not empty
            row['known'] = row['known'].split(',')
        else:
            row['known'] = []
        data.append(row)

# Define group size and number of groups
group_size = args.group_size
num_groups = args.num_groups

# Initialize sets of groups
set1_groups = [[] for _ in range(num_groups)]
set2_groups = [[] for _ in range(num_groups)]

def find_best_person(group, candidates):
    best_person = None
    best_score = float('-inf')  # Initialize the best score to negative infinity

    for person in candidates:
        # Calculate a score for this person
        # Here, we simply count the number of unique units and topics in the group
        # if this person is added, and subtract the number of people this person knows in the group
        score = len(set([p['unit'] for p in group + [person]])) + \
                 len(set([p['topic'] for p in group + [person]])) - \
                 sum(p['name'] in person['known'] for p in group)

        # If this person's score is better than the current best score, update the best person and best score
        if score > best_score:
            best_person = person
            best_score = score

    return best_person


# Populate groups for Set 1
data_copy = data.copy()
for i in range(num_groups - 1):
    while len(set1_groups[i]) < group_size and data_copy:
        person = find_best_person(set1_groups[i], data_copy)
        set1_groups[i].append(person)
        data_copy.remove(person)

# Fill the last group in Set 1 with the remaining people
set1_groups[-1].extend(data_copy)

# Repeat the same process for Set 2
data_copy = data.copy()
random.shuffle(data_copy)  # Shuffle data

for i in range(num_groups - 1):
    while len(set2_groups[i]) < group_size and data_copy:
        person = find_best_person(set2_groups[i], data_copy)
        set2_groups[i].append(person)
        data_copy.remove(person)

set2_groups[-1].extend(data_copy)

# Output the groups
print("Set 1 groups:")
for i, group in enumerate(set1_groups, 1):
    print(f"Group {i}: {[person['name'] for person in group]}")

print("\nSet 2 groups:")
for i, group in enumerate(set2_groups, 1):
    print(f"Group {i}: {[person['name'] for person in group]}")

# Export to Excel
df = pd.DataFrame(data)
df['Set1Group'] = pd.Series([next((i+1 for i, group in enumerate(set1_groups) if person in group), None) for person in data])
df['Set2Group'] = pd.Series([next((i+1 for i, group in enumerate(set2_groups) if person in group), None) for person in data])
df.to_excel('groups.xlsx', index=False)
