import csv
from sys import argv

if len(argv) != 3:
    print('expected 2 command line arguments')
    exit(1)

file = open(argv[1], 'r')

dna_strands = []
people = {}
# this is how to assign an index while iterating in python
for index, row in enumerate(file):
    if index == 0:
        dna_strands = [dna_strand for dna_strand in row.strip().split(',')][1:]
    else:
        current_row = row.strip().split(',')
        people[current_row[0]] = [int(x) for x in current_row[1:]]

strand = open(argv[2], 'r').read()

result_strands = []
for dna_strand in dna_strands:
    i = 0
    max_strand = -1
    current_max = 0
    while i < len(strand):
        current_select = strand[i:i + len(dna_strand)]
        if current_select == dna_strand:
            max_strand_length = max(max_strand, current_max) 
            i += len(dna_strand)
        else:
            current_max = 0
            i += 1
    result_strands.append(max_strand)

for name,data in people.items():
    if data == result_strands:
        print(name)
        exit(0)
    else:
        print('No match')

print(strands)
print(people)
print(result_strands)
