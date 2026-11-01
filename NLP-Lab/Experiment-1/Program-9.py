text = input("Enter text: ")
words = text.split()

lexical_diversity = len(set(words)) / len(words)

print("Lexical Diversity =", round(lexical_diversity, 2))


# Output:
# Enter text: AI AI NLP ML
# Lexical Diversity = 0.75
