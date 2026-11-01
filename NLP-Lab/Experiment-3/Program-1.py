from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "played", "plays", "studies", "connected"]

for word in words:
    print(word, "->", ps.stem(word))


# Output:
# playing -> play
# played -> play
# plays -> play
# studies -> studi
# connected -> connect
