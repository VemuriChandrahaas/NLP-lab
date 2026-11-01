# 3. Building a POS Tagger using Python

import nltk

# Download the required resources
nltk.download("punkt_tab", quiet=True)
nltk.download("averaged_perceptron_tagger_eng", quiet=True)

# Input sentence
sentence = input("Enter a sentence: ")

# Tokenize the sentence into words
words = nltk.word_tokenize(sentence)

# Perform POS tagging
tagged_words = nltk.pos_tag(words)

# Display the result
print("\nWord\t\tPOS Tag")
print("-------------------------")
for word, tag in tagged_words:
    print(f"{word}\t\t{tag}")

# Expected output for: The student reads a book.
#
# Word            POS Tag
# -------------------------
# The             DT
# student         NN
# reads           VBZ
# a               DT
# book            NN
# .               .
