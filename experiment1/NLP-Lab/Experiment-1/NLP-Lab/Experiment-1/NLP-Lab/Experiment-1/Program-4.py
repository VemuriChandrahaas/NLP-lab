from collections import Counter

text = input("Enter text: ")
words = text.split()

frequency = Counter(words)

for word, count in frequency.most_common():
    print(word, ":", count)


# Output:
# Enter text: NLP NLP AI AI AI
# AI : 3
# NLP : 2
