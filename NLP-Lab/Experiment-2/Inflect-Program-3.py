import inflect

p = inflect.engine()

word = input("Enter a word: ")
print(p.a(word))


# Output:
# Enter a word: apple
# an apple
