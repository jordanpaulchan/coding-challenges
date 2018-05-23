class Autocomplete:
    def __init__(self):
        self.trie = {}

    def get_words(self, start, temp, words):
        if start['isWord']:
            words.append((temp, start['isWord']))

        for key, val in start.items():
            if key != 'isWord':
                self.get_words(val, temp + key, words)

    def get(self, prefix):
        current = self.trie
        for char in prefix:
            if char not in current:
                return []
            current = current[char]

        words = []
        self.get_words(current, prefix, words)
        sorted_words = sorted(words, key=lambda x: x[1], reverse=True)
        return sorted_words

    def put(self, word):
        current = self.trie
        for char in word:
            if char not in current:
                current[char] = {'isWord': 0}
            current = current[char]
        current['isWord'] += 1


autocomplete = Autocomplete()
autocomplete.put('boat')
autocomplete.put('boat')
autocomplete.put('boat')

autocomplete.put('goat')
autocomplete.put('book')
autocomplete.put('booking')
print(autocomplete.get('bo'))
