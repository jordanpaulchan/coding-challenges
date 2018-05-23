import re


def greeting():
    print "***** Hangman ****\n"


def get_word():
    return 'hangman'


def generate_string(word, letters):
    string = []
    for l in word:
        if l in letters:
            string.append(l)
        else:
            string.append('_')
    return ''.join(string)


def has_won(word, letters):
    for l in word:
        if l not in letters:
            return False

    return True


def is_valid(letter, letters):
    regex = r"[a-zA-Z]"
    if not re.search(regex, letter):
        return False

    if letter in letters:
        return False
    return True


def main():
    greeting()

    word = get_word()

    letters = set()

    while True:
        print generate_string(word, letters)

        if has_won(word, letters):
            print "Congrats, you've won!"
            return

        letter = raw_input("Enter a letter: ")

        if not is_valid(letter, letters):
            print "You've already selected that letter"

        letters.add(letter)


main()
