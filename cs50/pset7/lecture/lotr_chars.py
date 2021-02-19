import csv

counts = {}

with open("lotr_characters.csv", 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        title = row["name"]
        
        if title in counts:
            counts[title] += 1
        else: 
            counts[title] = 1

for title, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
    print(title, count, sep=" | ")
