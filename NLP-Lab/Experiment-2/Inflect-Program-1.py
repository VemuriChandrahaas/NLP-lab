import inflect

p = inflect.engine()

word = input("Enter a singular noun: ")
plural = p.plural(word)

print("Singular :", word)
print("Plural   :", plural)


# Output:
# Enter a singular noun: city
# Singular : city
# Plural   : cities
