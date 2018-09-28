sent = input('Введите предложение: ').split()

punct_symbols = ',.!?:;-'
if sent[-1][-1] in punct_symbols: #сохраняем последний знак пунктуации в переменную, чтобы потом поставить его в конце зашифрованного предложения
    punct1 = sent[-1][-1]
    sent[-1] = sent[-1][:-1]
else:
    punct1 = ''
if sent[-2][-1] in punct_symbols: #сохраняем знак пунктуации, если он идет между двумя последними словами
    punct2 = sent[-2][-1]
    sent[-2] = sent[-2][:-1]
else:
    punct2 = ''

new_sent = sent[:-2] #создаем новое предложение в виде списка, где два последних слова поменялись местами
new_sent.append(sent[-1])
new_sent.append(sent[-2])

new_sent[-2] += punct2 #возвращаем последние знаки препинания в новое предложение так, как они должны стоять
new_sent[-1] += punct1
new_sent = ' '.join(new_sent) #преобразуем предложение в строку, с которой шифру легче работать

alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'  #создаем сам шифр
caesar_cipher = {i: '' for i in alpha}
for i, letter in enumerate(alpha[:-1]):
    caesar_cipher[letter] = alpha[i + 1]
caesar_cipher['я'] = 'а'
caesar_cipher[' '] = ' '

for letter in new_sent:  #применяем шифр, учитывая регистр букв
    if letter in caesar_cipher:
        print(caesar_cipher[letter], end='')
    else:
        letter = letter.lower()
        if letter in caesar_cipher:
            print(caesar_cipher[letter].upper(), end='')
        else:
            print(letter, end='')  #так в новом предложении сохранятся цифры и оставшиеся знаки препинания исходного предложения
