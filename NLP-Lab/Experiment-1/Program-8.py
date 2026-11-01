text = input("Enter text: ")

vowels = consonants = digits = spaces = special = 0

for ch in text:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1

print("Vowels =", vowels)
print("Consonants =", consonants)
print("Letters =", vowels + consonants)
print("Digits =", digits)
print("Spaces =", spaces)
print("Special Characters =", special)


# Output:
# Enter text: NLP 2026!
# Vowels = 0
# Consonants = 3
# Letters = 3
# Digits = 4
# Spaces = 1
# Special Characters = 1
