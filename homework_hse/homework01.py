word = input('Введите слово: ') # задание решено без создания списка
word = word.strip("!?,.").lower()
for indx, letter in enumerate(word):
    if indx % 2 == 1 and letter != 'к' and letter != 'а':
        print(letter)

number = int(input('Введите число: '))
for i in range(number):
    word = input('Введите слово: ')
    if word != 'программирование':
        print(word)
    else:
        break
print('Конец!')

word = input('Введите слово: ').strip('!?,.') #задание решено без срезов
half = len(word)//2
for indx, letter in enumerate(word):
    if indx < half:
        print(letter, end=' ')
i = -1
if len(word)%2 == 0:
    while i >= -half:
        print(word[i], end=' ')
        i -= 1
else:
    while i >= -half-1:
        print(word[i], end=' ')
        i -= 1
