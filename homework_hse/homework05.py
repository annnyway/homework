import os
import re

#подразумевается, что программа может работать из любой папки

# сначала вводятся функции, которые будут использоваться внутри других функций
def dir_paths():
    dirpaths = []
    for i in os.walk('.'):
        dirpaths.append([i][0][0])
    return dirpaths  # функция возвращает список путей к папкам


def file_names():
    filenames = []
    for root, dirs, files in os.walk('.'):
        for fl in files:
            filenames.append(fl)
    return filenames  # функция возвращает список названий файлов


def max_count(lst):
    count = {i: lst.count(i) for i in lst}
    return max(count.values())  # функция принимает на вход список и возвращает словарь, в котором ключ
    # - элемент списка, а значение - частота этого элемента в списке


def lists_of_files_in_dirs():
    lists_of_files = []
    for i in os.walk('.'):
        lists_of_files.append([i][0][2])
    return lists_of_files  # функция возвращает список списков файлов в директориях

# отсюда начинаются основные функции

def max_depth():
    depth = []
    for dirpath in dir_paths():
        depth.append(dirpath.count(str(os.sep)))
    return '1. Максимальная глубина папки: ' + str(max(depth))


def count_cyrillic_names():
    cyrillic_names = []
    for root, dirs, files in os.walk('.'):
        for _dir in dirs:
            if re.search('^[а-яА-Я]+$', _dir):
                cyrillic_names.append(str(_dir))
    return '2. Число папок с полностью кириллическими названиями: ' + str(len(cyrillic_names))


def max_filename_extension():
    extensions = []
    for fl in file_names():
        fl, file_extension = os.path.splitext(fl)
        if file_extension.startswith('.'):
            extensions.append(file_extension)
    max_extension = ''
    for i in extensions:
        if extensions.count(i) == max_count(extensions):
            max_extension = i
    return '3. Самое частотное расширение файлов: ' + max_extension

def files_with_diff_names():
    filenames_without_extension = set()
    for fl in file_names():
        fl, file_extension = os.path.splitext(fl)
        filenames_without_extension.add(fl)
    return '5. Число разных названий файлов без учета расширений: ' + str(len(filenames_without_extension))


def max_fist_letter_of_dirs():
    first_letters = []
    for root, dirs, files in os.walk('.'):
        for directory in dirs:
            first_letters.append(directory[0])
    max_letter = ''
    for i in first_letters:
        if first_letters.count(i) == max_count(first_letters):
            max_letter = i
    return '4. Самая частотная первая буква в названии папок: ' + max_letter


def dirs_with_same_extension_of_files():
    count_dirs = 0
    for _dir in lists_of_files_in_dirs():
        for i, fl in enumerate(_dir):
            fl, file_extension = os.path.splitext(fl)
            _dir[i] = file_extension
        if len(_dir) > len(set(_dir)):
            count_dirs += 1
    return '6. Число папок с несколькими файлами с одним и тем же расширением: ' + str(count_dirs)


def max_dir_with_files():
    number_of_files = {}
    max_dir = ''

    for _dir in dir_paths():
        number_of_files[_dir] = len([name for name in os.listdir(_dir) if os.path.isfile(name)])
        max_number_of_files = max(number_of_files.values())
        if number_of_files[_dir] == max_number_of_files:
            max_dir = _dir

    if max_dir == '.':
        return '7. Папка с максимальным числом файлов: ' + max_dir + ' (папка с этой программой)'
    else:
        return '7. Папка с максимальным числом файлов: ' + max_dir  # функция возвращает папку, где больше всего файлов, вместе с путем к ней


def main():
    output = [max_depth(), count_cyrillic_names(), max_filename_extension(), max_fist_letter_of_dirs(), files_with_diff_names(), dirs_with_same_extension_of_files(), max_dir_with_files()]
    output = '\n'.join(output)
    with open('homework05.txt', 'w') as wf:
            wf = wf.write(output)
    return 0


if __name__ == '__main__':
    main()
