import nltk
from nltk import bigrams
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

text = input("Enter a sentence: ")
tokens = word_tokenize(text)

bg = list(bigrams(tokens))
freq = Counter(bg)

print("Bigram Frequencies:")
for k, v in freq.items():
    print(k, ":", v)


# Output:
# Enter a sentence: I love NLP I love Python
# Bigram Frequencies:
# ('I', 'love') : 2
# ('love', 'NLP') : 1
# ('NLP', 'I') : 1
# ('love', 'Python') : 1
