with open('amkharskiy.tsv', 'r') as f:
    lines = f.readlines()
dict = {}
for line in lines:
    line.split('\t')
print(lines)
for i,line in enumerate(lines):
        if i != 0:
            dict[line[0]] = ''
print(dict)