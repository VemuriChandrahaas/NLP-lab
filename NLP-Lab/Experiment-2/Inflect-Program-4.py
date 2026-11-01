import inflect

p = inflect.engine()

number = int(input("Enter a number: "))
print(p.number_to_words(number))


# Output:
# Enter a number: 125
# one hundred and twenty-five
