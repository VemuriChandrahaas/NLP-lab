from collections import defaultdict

# Training data
training_data = [
    [("The", "DT"), ("dog", "NN"), ("runs", "VB")],
    [("The", "DT"), ("cat", "NN"), ("eats", "VB")],
    [("A", "DT"), ("dog", "NN"), ("eats", "VB")],
    [("A", "DT"), ("cat", "NN"), ("runs", "VB")]
]

# Dictionaries
transition_counts = defaultdict(lambda: defaultdict(int))
emission_counts = defaultdict(lambda: defaultdict(int))
tag_counts = defaultdict(int)

# ------------------------------------------------
# STEP 1: Count transitions and emissions
# ------------------------------------------------

for sentence in training_data:

    previous_tag = "<START>"

    for word, tag in sentence:

        # Transition count
        transition_counts[previous_tag][tag] += 1

        # Emission count
        emission_counts[tag][word.lower()] += 1

        # Tag count
        tag_counts[tag] += 1

        previous_tag = tag


# ------------------------------------------------
# STEP 2: Calculate probabilities
# ------------------------------------------------

def transition_probability(previous_tag, current_tag):

    total = sum(transition_counts[previous_tag].values())

    if total == 0:
        return 0

    return transition_counts[previous_tag][current_tag] / total


def emission_probability(tag, word):

    total = tag_counts[tag]

    if total == 0:
        return 0

    return emission_counts[tag][word.lower()] / total


# ------------------------------------------------
# STEP 3: Display probabilities
# ------------------------------------------------

print("Transition Probability")
print("----------------------")

print("P(DT | START) =",
      transition_probability("<START>", "DT"))

print("P(NN | DT) =",
      transition_probability("DT", "NN"))

print("P(VB | NN) =",
      transition_probability("NN", "VB"))


print("\nEmission Probability")
print("--------------------")

print("P(The | DT) =",
      emission_probability("DT", "The"))

print("P(dog | NN) =",
      emission_probability("NN", "dog"))

print("P(eats | VB) =",
      emission_probability("VB", "eats"))


# Output:
# Transition Probability
# ----------------------
# P(DT | START) = 1.0
# P(NN | DT) = 1.0
# P(VB | NN) = 1.0
#
# Emission Probability
# --------------------
# P(The | DT) = 0.5
# P(dog | NN) = 0.5
# P(eats | VB) = 0.5
