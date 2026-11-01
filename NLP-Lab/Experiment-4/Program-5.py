import nltk
from nltk import bigrams
from nltk.tokenize import word_tokenize
from collections import defaultdict

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

text = input("Enter training sentence: ")
tokens = word_tokenize(text)

model = defaultdict(list)

for w1, w2 in bigrams(tokens):
    model[w1].append(w2)

word = input("Enter a word: ")

if word in model:
    print("Possible next words:", model[word])
else:
    print("No prediction available.")


# Output:
# Enter training sentence: I love NLP I love Python
# Enter a word: love
# Possible next words: ['NLP', 'Python']
