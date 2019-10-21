"""
Input:
{
  "articles": [
    {
      "text": "This is a short article."
    },
    {
      "text": "Now for a longer article. This one has a lot of text."
    },
    {
      "text": "Another article with medium length."
    }
  ],
  "width": 55
}

Output:
+-------------------------------------------------------+
|This is a short article.                               |
+-------------------------------------------------------+
|Now for a longer article. This one has a lot of text.  |
+-------------------------------------------------------+
|Another article with medium length.                    |
+-------------------------------------------------------+

+------------+
|This is a   |
|short       |
|article.    |
+------------+
|Now for a   |
|longer      |
|article.    |
|This one has|
|a lot of    |
|text.       |
+------------+
|Another     |
|article with|
|medium      |
|length.     |
+------------+

"""


class Article:
    def __init__(self, text):
        self.text = text


articles = [
    Article("This is a short article."),
    Article("Now for a longer article. This one has a lot of text."),
    Article("Wonderland is another article with medium length.")
]

width = 10


def printBorder(width):
    dashes = '-' * width
    print('+{}+'.format(dashes))


def calcCurrentWidth(currentWords):
    currentWidth = len(' '.join(currentWords))
    if currentWidth > 0:
        return currentWidth + 1
    return 0


def printCurrent(currentWords, width):
    text = ' '.join(currentWords)
    print('|{message: <{fill}}|'.format(
        message=text, fill=(width)))


def printArticles(articles, width):
    printBorder(width)

    current = []

    for article in articles:
        words = article.text.split(' ')
        for word in words:
            if calcCurrentWidth(current) + len(word) > width:
                printCurrent(current, width)
                current = [word]
            else:
                current.append(word)

        if current:
            printCurrent(current, width)
        current = []

        printBorder(width)


printArticles(articles, width)
