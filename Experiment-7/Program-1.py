# 2. POS Tagging using Viterbi Decoding – Python Program

tags = ["DET", "NOUN", "VERB"]
words = ["The", "dog", "runs"]

# Initial probabilities
initial = {
    "DET": 0.6,
    "NOUN": 0.3,
    "VERB": 0.1,
}

# Transition probabilities
transition = {
    "DET": {"DET": 0.1, "NOUN": 0.7, "VERB": 0.2},
    "NOUN": {"DET": 0.1, "NOUN": 0.2, "VERB": 0.7},
    "VERB": {"DET": 0.3, "NOUN": 0.3, "VERB": 0.4},
}

# Emission probabilities
emission = {
    "DET": {"The": 0.9, "dog": 0.05, "runs": 0.01},
    "NOUN": {"The": 0.05, "dog": 0.8, "runs": 0.05},
    "VERB": {"The": 0.01, "dog": 0.05, "runs": 0.7},
}

# Viterbi tables
V = [{}]
backpointer = [{}]

# Initialization
for tag in tags:
    V[0][tag] = initial[tag] * emission[tag][words[0]]
    backpointer[0][tag] = None

# Recursion
for position in range(1, len(words)):
    V.append({})
    backpointer.append({})

    for current_tag in tags:
        probabilities = []

        for previous_tag in tags:
            probability = (
                V[position - 1][previous_tag]
                * transition[previous_tag][current_tag]
                * emission[current_tag][words[position]]
            )
            probabilities.append((probability, previous_tag))

        best_probability, best_previous_tag = max(probabilities)
        V[position][current_tag] = best_probability
        backpointer[position][current_tag] = best_previous_tag

# Find the best final tag
best_final_tag = max(V[-1], key=V[-1].get)

# Backtracking
best_tags = [best_final_tag]
for position in range(len(words) - 1, 0, -1):
    best_final_tag = backpointer[position][best_final_tag]
    best_tags.append(best_final_tag)

best_tags.reverse()

# Display result
print("POS Tagged Sentence:")
for word, tag in zip(words, best_tags):
    print(word, "->", tag)

# Expected output:
# POS Tagged Sentence:
# The -> DET
# dog -> NOUN
# runs -> VERB
