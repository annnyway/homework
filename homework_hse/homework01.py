word = input('Введите слово: ')
word = word.strip("!?,.").lower()
letters = []
for indx, letter in enumerate(word, start=1):
    if indx % 2 == 0 and letter != 'к' and letter != 'а':
        letters.append(letter)
print('Ответ: ')
for letter in letters:
    print(letter)

number = int(input('Введите число: '))
for i in range(number):
    word = input('Введите слово: ')
    if word != 'программирование':
        print(word)
    else:
        break
print('Конец!')

word = input('Введите слово: ').strip('!?,.')
middle_index = len(word) // 2
word_half1 = word[0:middle_index]
word_half2 = word[:middle_index - 1:-1]
new_word = word_half1 + word_half2
print('Ответ: ')
for letter in new_word:
    print(letter, end=' ')
