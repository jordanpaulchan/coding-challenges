# internationalization - i18n
# foobar - f4r
# it - it


def abbrevation(word):
    if not word or len(word) < 3:
        return word

    return word[0] + str(len(word) - 2) + word[-1]


print(abbrevation('internationalization'))
print(abbrevation('foobar'))
print(abbrevation('it'))
print(abbrevation('a'))
