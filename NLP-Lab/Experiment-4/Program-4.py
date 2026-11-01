import nltk
from nltk import trigrams
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

text = input("Enter a sentence: ")
tokens = word_tokenize(text)

tg = list(trigrams(tokens))
freq = Counter(tg)

print("Trigram Frequencies:")
for k, v in freq.items():
    print(k, ":", v)


# Output:
# Enter a sentence: I love NLP and I love Python
# Trigram Frequencies:
# ('I', 'love', 'NLP') : 1
# ('love', 'NLP', 'and') : 1
# ('NLP', 'and', 'I') : 1
# ('and', 'I', 'love') : 1
# ('I', 'love', 'Python') : 1
