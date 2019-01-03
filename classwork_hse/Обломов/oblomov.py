import os, re


def text(): #
    with open('oblomov.txt') as text:
        text = text.read().split('ЧАСТЬ')
    for i, j in enumerate(text):
        if i != 0:
            text[i] = 'ЧАСТЬ' + j
    with open('1.txt', 'w') as wf:
        wf = wf.write(text[2])
    return text


def part_names(text):
    names = []
    for i in range(len(text())):
        names.append('part' + str(i))
    return names


def create_part_files(part_names, text):
    for part_name in part_names(text):
        dir_name = 'oblomov' + os.sep + part_name
        if os.path.isdir(dir_name):
            continue
        os.mkdir(dir_name)
    return 0


def write_parts():
    parts = dict(zip(part_names(text), text()))
    for root, dirs, files in os.walk('.'):
        for _dir in dirs:
            if _dir in parts.keys():
                f = open(root + os.sep + _dir + os.sep + _dir + '.txt', 'w')
                f = f.write(parts[_dir])
    return 0


'''
def split_chapters():
    regexp = re.compile(r"\n\n\n\n\n([IVX]{1,4}.*?)\n\n\n\n\n", re.DOTALL)
    numbers_of_chapters = []
    for root, dirs, files in os.walk('.'):
        for fl in files:
            with open(fl, 'r', encoding="utf-8") as f:
                f = f.read()
                numbers_of_chapters += regexp.findall(f)
    print(numbers_of_chapters)
    return 0
'''

def main():
    text()
    part_names(text)
    create_part_files(part_names, text)
    write_parts()

if __name__ == '__main__':
    main()



