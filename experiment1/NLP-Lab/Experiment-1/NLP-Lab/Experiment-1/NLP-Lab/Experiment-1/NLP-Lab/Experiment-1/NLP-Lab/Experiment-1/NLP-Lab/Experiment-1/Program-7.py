text = input("Enter text: ")
words = text.split()

print("Total Words =", len(words))
print("Unique Words =", len(set(words)))


# Output:
# Enter text: AI AI ML NLP
# Total Words = 4
# Unique Words = 3
