import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

text = input("Enter a sentence: ")
n = int(input("Enter the value of n: "))

tokens = word_tokenize(text)

print(f"{n}-Grams:")
for gram in ngrams(tokens, n):
    print(gram)


# Output:
# Enter a sentence: I love NLP programming
# Enter the value of n: 2
# 2-Grams:
# ('I', 'love')
# ('love', 'NLP')
# ('NLP', 'programming')
