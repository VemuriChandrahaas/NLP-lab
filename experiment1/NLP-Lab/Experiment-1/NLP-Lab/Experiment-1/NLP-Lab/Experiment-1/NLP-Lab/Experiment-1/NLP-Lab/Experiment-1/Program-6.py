text = input("Enter text: ")
words = text.split()

longest = max(words, key=len)
shortest = min(words, key=len)
average = sum(len(w) for w in words) / len(words)

print("Longest Word:", longest)
print("Shortest Word:", shortest)
print("Average Length:", round(average, 2))


# Output:
# Enter text: Natural Language Processing
# Longest Word: Processing
# Shortest Word: Natural
# Average Length: 8.33
