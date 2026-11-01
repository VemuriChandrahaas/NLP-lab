root = input("Enter the root word: ")

generated_words = [
    root,
    root + "s",
    root + "ed",
    root + "ing",
    root + "er",
    root + "ly",
    "re" + root,
    "un" + root
]

print("\nGenerated Word Forms")
for word in generated_words:
    print(word)


# Output:
# Enter the root word: teach
#
# Generated Word Forms
# teach
# teachs
# teached
# teaching
# teacher
# teachly
# reteach
# unteach
