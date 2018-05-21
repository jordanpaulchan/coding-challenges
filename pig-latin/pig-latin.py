def move_first_char(word, capitalize):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    if word[0] in vowels:
        return word + 'ay'
    elif len(word) > 1 and word[:2].lower() == 'qu':
        if capitalize:
            return word[2:].capitalize() + word[:2].lower() + 'ay'
        else:
            return word[2:] + word[:2] + 'ay'
    else:
        idx = 0
        while word[idx] not in vowels:
            idx += 1

        if capitalize:
            return word[idx:].capitalize() + word[:idx].lower() + 'ay'
        else:
            return word[idx:] + word[:idx] + 'ay'


def pig_latin(word):
    if not word:
        return ''

    if len(word) == 1 and word[0].isalpha():
        return word + 'ay'

    # punctuation
    suffix_ptr = len(word) - 1
    while not word[suffix_ptr].isalpha():
        suffix_ptr -= 1

    prefix = word[:suffix_ptr + 1]
    suffix = word[suffix_ptr + 1:]

    is_upper = prefix[0].isupper()
    return move_first_char(prefix, is_upper) + suffix


def pig_latin_sentence(sentence):
    phrase = []
    for word in sentence.split(' '):
        phrase.append(pig_latin(word))

    return ' '.join(phrase)


print pig_latin_sentence('Hello, world!!')
print pig_latin_sentence('eat apples')
print pig_latin_sentence('quick brown fox')
