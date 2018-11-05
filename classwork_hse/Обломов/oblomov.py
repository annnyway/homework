import os, re


def text():
    with open('oblomov.txt') as text:
        text = text.read().split('ЧАСТЬ')
    for i, part in enumerate(text):
        text[i+1] = 'ЧАСТЬ' + part
    return text

def part_names(text):
    names = []
    for i in range(len(text())):
        names.append('part' + str(i))
    return names
print(part_names(text))

def create_parts(part_names, text):
    lst = os.listdir("oblomov")
    for root, dirs, files in os.walk('.'):
        for part_name in part_names(text):
            dir_name = 'oblomov' + os.sep + part_name
            if os.path.isdir(dir_name):
                continue
            os.mkdir(dir_name)

#for root, dirs, files in os.walk('dir1/dir2') или ('.'):
#f = open(part_name + '.txt', 'w')
            #f = f.write(part)
        # os.mkdir(k)
    #for i, part_name in enumerate(part_names):
     #   k =
      #  if os.path.isdir(k):
       #     continue


       # lst = os.listdir(k)
        #for part in text:
         #   with open(part_name + ".txt", 'w') as f:
          #      f = f.write(part)
   # return 0

def main():
    create_parts(part_names, text)

if __name__ == '__main__':
    main()



