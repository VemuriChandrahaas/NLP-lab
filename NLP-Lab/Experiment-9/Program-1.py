# 4. Chunking in NLP

import nltk

nltk.download("punkt_tab", quiet=True)
nltk.download("averaged_perceptron_tagger_eng", quiet=True)

sentence = "The clever student reads a book"

# Tokenization and POS tagging
words = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(words)

# Define chunking grammar
grammar = "NP: {<DT>?<JJ>*<NN>+}"

# Perform chunking
parser = nltk.RegexpParser(grammar)
result = parser.parse(tagged)

print(result)

# Expected output:
# (S (NP The/DT clever/JJ student/NN) reads/VBZ (NP a/DT book/NN))
