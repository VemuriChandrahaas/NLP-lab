import inflect

p = inflect.engine()

number = int(input("Enter a number: "))
print("Ordinal :", p.ordinal(number))


# Output:
# Enter a number: 21
# Ordinal : 21st
