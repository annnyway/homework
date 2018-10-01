def clean_text(text):
    with open(text.txt, 'r') as text:
        text = text.read()
    text = text.lower().split()
    for i, word in enumerate(text):
        text[i] = word.strip('.,!?:();')
    return(text)