import csv

with open('amkharskiy.tsv', 'r') as f:
    lines = f.readlines()

consonants = []
for i,line in enumerate(lines):
    lines[i] = line.split()
    if i > 0:
        consonants.append(line[0])

vowels = lines[0]

syllables = []
for i in vowels:
    for j in consonants:
        syll = j+i
        syllables.append(syll)

dict = {}
for syll in syllables:
    dict[syll] = ''
print(dict)
