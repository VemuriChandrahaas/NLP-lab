import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

text = input("Enter a sentence: ")
stop_words = set(stopwords.words('english'))

tokens = word_tokenize(text)
filtered_words = [w for w in tokens if w.isalpha() and w.lower() not in stop_words]

print(filtered_words)


# Output:
# Enter a sentence: This is a Natural Language Processing Lab.
# ['Natural', 'Language', 'Processing', 'Lab']
