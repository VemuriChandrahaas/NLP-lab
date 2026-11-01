import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

text = input("Enter a sentence: ")
tokens = word_tokenize(text)

print("Unigrams:")
print(list(ngrams(tokens, 1)))

print("\nBigrams:")
print(list(ngrams(tokens, 2)))

print("\nTrigrams:")
print(list(ngrams(tokens, 3)))


# Output:
# Enter a sentence: I love natural language processing
# Unigrams:
# [('I',), ('love',), ('natural',), ('language',), ('processing',)]
#
# Bigrams:
# [('I', 'love'), ('love', 'natural'), ('natural', 'language'), ('language', 'processing')]
#
# Trigrams:
# [('I', 'love', 'natural'), ('love', 'natural', 'language'), ('natural', 'language', 'processing')]
