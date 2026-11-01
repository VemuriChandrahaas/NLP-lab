import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

text = input("Enter a sentence: ")
tokens = word_tokenize(text)
print(tokens)


# Output:
# Enter a sentence: Natural Language Processing is interesting.
# ['Natural', 'Language', 'Processing', 'is', 'interesting', '.']
