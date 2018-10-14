import random


def adjective():
    with open('adjectives.tsv', 'r') as f:
        adjectives = f.read().split()
    return random.choice(adjectives)


def noun():
    with open('nouns.tsv', 'r') as f:
        nouns = f.read().split()
    return random.choice(nouns)


def transitive_verb():
    with open('trans_verbs.tsv', 'r') as f:
        verbs = f.read().split()
    return random.choice(verbs)


def intransitive_verb():
    with open('intrans_verbs.tsv', 'r') as f:
        verbs = f.read().split()
    return random.choice(verbs)


def transitive_verb_with_s():
    with open('trans_verbs.tsv', 'r') as f:
        verbs = f.read().split()
    verb = random.choice(verbs)
    ends = ['ss', 'x', 'z', 'ch', 'sh']
    vowels = 'aeiou'
    if verb.endswith('y') and verb[-2] not in vowels:
        verb = verb[0:-1] + 'ies'
    elif verb.endswith(tuple(ends)):
        verb += 'es'
    else:
        verb += 's'
    return verb


def intransitive_verb_with_s():
    with open('intrans_verbs.tsv', 'r') as f:
        verbs = f.read().split()
    verb = random.choice(verbs)
    ends = ['ss', 'x', 'z', 'ch', 'sh']
    vowels = 'aeiou'
    if verb.endswith('y') and verb[-2] not in vowels:
        verb = verb[0:-1] + 'ies'
    elif verb.endswith(tuple(ends)):
        verb = verb + 'es'
    else:
        verb = verb + 's'
    return verb


def adverb():
    with open('adverbs.tsv', 'r') as f:
        adverbs = f.read().split()
    return random.choice(adverbs)


def comparative_adjective():
    with open('comparative_adjectives.tsv', 'r') as f:
        adjectives = f.read().split()
    return random.choice(adjectives)


def affirmative_sentence():
    sentence = str(adjective().capitalize() + ' ' + noun() + ' ' + transitive_verb_with_s() +\
                   ' ' + noun() + ' that ' + intransitive_verb_with_s() + ' ' + adverb() + '.')
    return sentence


def interrogative_sentence():
    sentence = 'Did ' + noun() + ' ' + transitive_verb() + ' ' + adjective() + ' ' +\
               noun() + ' ' + 'yesterday?'
    return sentence


def negative_sentence():
    sentence = adjective().capitalize() + ' ' + noun() + ' will not ' + transitive_verb() +\
               ' ' + noun() + '.'
    return sentence


def conditional_sentence():
    sentence = 'If ' + noun() + ' ' + transitive_verb_with_s() + ' ' + noun() + ', ' +\
               noun() + ' will ' + intransitive_verb() + ' ' + comparative_adjective() + '.'
    return sentence


def imperative_sentence():
    sentence = transitive_verb().capitalize() + ' the ' + adjective() + ' ' + noun() + ', please.'
    return sentence


def random_sentences():
    sentences = [affirmative_sentence(), interrogative_sentence(), negative_sentence(), conditional_sentence(),
                 imperative_sentence()]
    random.shuffle(sentences)
    return sentences


def main():
    with open('random_sentences.txt', 'w') as f:
        for sent in random_sentences():
            f.write(sent + '\n')
    return 0


if __name__ == '__main__':
    main()
