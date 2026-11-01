adj = input("Enter an adjective: ")

if len(adj) <= 5:
    print("Comparative :", adj + "er")
    print("Superlative :", adj + "est")
else:
    print("Comparative : more", adj)
    print("Superlative : most", adj)


# Output 1:
# Enter an adjective: tall
# Comparative : taller
# Superlative : tallest
#
# Output 2:
# Enter an adjective: beautiful
# Comparative : more beautiful
# Superlative : most beautiful
