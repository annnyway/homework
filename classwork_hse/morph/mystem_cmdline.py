# -*- coding: utf-8 -*-
import os
import re

lst = os.listdir('./texts/')
print(lst)
# path = path.decode("utf8")


for fl in lst:
    text = os.system('/Users/anyway/homework/classwork_hse/morph/mystem {} tagged-{} -i -d -n'.format('./texts/' + fl, fl))

lst = os.listdir('.')

tagged_words = []
for fl in lst:
    if fl.startswith('tagged-'):
        f = open(fl, 'r')
        f = f.read().split('}')
        for i in f:
            i = i.split('{')
            tagged_words += [i]

lemmas_and_pos = []
for fl in lst:
    if fl.startswith('tagged-'):
        f = open(fl, 'r', encoding="UTF-8")
        f = f.read()
        lemmas_and_pos += re.findall(r"{(.*?=[A-Z]{1,6})", f)
print(lemmas_and_pos)
#41594

for i, word in enumerate(lemmas_and_pos):
    lemmas_and_pos[i] = re.sub('=', '\t', word)

with open('mystem_dataset.txt', 'w', encoding='UTF-8') as wf:
    for item in lemmas_and_pos:
        wf.write("%s\n" % item)