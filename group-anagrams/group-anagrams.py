from collections import OrderedDict


def toKeyString(word):
    return ''.join(sorted(word.lower()))


def findAnagrams(arr):
    anagrams = OrderedDict()
    for word in arr:
        key = toKeyString(word)

        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]

    return anagrams


def writeToFile(anagrams, file):
    file = open(file, 'w')
    for key, value in anagrams.iteritems():
        file.write(', '.join(value))
        file.write('\n')

    file.close()


def getInputFromFile(file):
    with open(file) as f:
        content = f.readlines()
        return [x.strip() for x in content]


input = getInputFromFile('input.txt')
writeToFile(findAnagrams(input), 'output.txt')
