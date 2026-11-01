import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

text = input("Enter a paragraph: ")
sentences = sent_tokenize(text)

for i, sentence in enumerate(sentences, 1):
    print(f"Sentence {i}: {sentence}")


# Output:
# Enter a paragraph: NLP is interesting. It is a branch of AI.
# Sentence 1: NLP is interesting.
# Sentence 2: It is a branch of AI.
