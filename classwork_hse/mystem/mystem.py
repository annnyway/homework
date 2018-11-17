import os

lst = os.listdir('/Users/anyway/homework/classwork_hse/kek/texts')
for fl in lst:
    text = os.system('/Users/anyway/homework/classwork_hse/kek/mystem {} tagged-{} -id'.format(fl,fl))
    print(text)