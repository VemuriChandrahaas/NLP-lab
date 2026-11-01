from collections import Counter

# Training corpus
sentences = [
    "I like NLP",
    "I like Python",
    "I love NLP"
]

# Tokenize sentences
tokenized_sentences = [sentence.lower().split() for sentence in sentences]

# Create vocabulary
vocabulary = set()
for sentence in tokenized_sentences:
    vocabulary.update(sentence)

V = len(vocabulary)

# Count unigrams and bigrams
unigram_counts = Counter()
bigram_counts = Counter()

for sentence in tokenized_sentences:
    for word in sentence:
        unigram_counts[word] += 1
    for i in range(len(sentence) - 1):
        bigram = (sentence[i], sentence[i + 1])
        bigram_counts[bigram] += 1


# Laplace smoothing function
def laplace_probability(previous_word, current_word):
    bigram_count = bigram_counts[(previous_word, current_word)]
    previous_count = unigram_counts[previous_word]
    probability = (bigram_count + 1) / (previous_count + V)
    return probability


# Test probabilities
print("Vocabulary size:", V)

print("\nP(NLP | like):")
print(laplace_probability("like", "nlp"))

print("\nP(love | like):")
print(laplace_probability("like", "love"))


# Output:
# Vocabulary size: 5
#
# P(NLP | like):
# 0.2857142857142857
#
# P(love | like):
# 0.14285714285714285
