def pattern_match(words, code):
    words_list = words.split(' ')
    code_list = list(code)
    if (len(words_list) != len(code_list)):
        return False

    char_map = {}
    word_map = set()
    for word, char in zip(words_list, code_list):
        if char in char_map:
            if char_map[char] != word:
                return False
        elif word in word_map:
            return False
        else:
            char_map[char] = word
            word_map.add(word)

    return True


if __name__ == "__main__":
    words = 'blue yellow green'
    code = 'abc'
    print(pattern_match(words, code))
