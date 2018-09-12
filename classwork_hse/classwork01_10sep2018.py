while True:
    print('Введите слово:')
    word = input()
    if not word:
        break
    else:
        word = word.strip('!?,.')
        word.lower()
        #прилагательное, мужской род, ед.число
        if word.endswith('ий') or word.endswith('ий'):
            print('прилагательное мужского рода в ед.ч., им.п. или вин.п.')
        elif word.endswith('ого') or word.endswith('eго'):
            print('прилагательное мужского рода в ед.ч., род.п.')
        elif word.endswith('ему') or word.endswith('ому'):
            print('прилагательное мужского рода в ед.ч., дат.п.')
        elif word.endswith('им') or word.endswith('ым'):
            print('прилагательное мужского рода в ед.ч., твор.п.')
        elif word.endswith('ом') or word.endswith('ем'):
            print('прилагательное мужского рода в ед.ч., предл.п.')