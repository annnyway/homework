import re

with open('wiki_chinese_space_program.txt', 'r') as f:
    text = f.read()
spacecrafts = re.findall("(«[А-Я].[а-я]+?[нуэ].+?(-[0-9]{1,3})?»)", text)

for i, spacecraft in enumerate(spacecrafts):
    spacecrafts[i] = spacecraft[0]

print(list(spacecrafts))
