# Program to generate words using prefixes and suffixes
root = input("Enter the root word: ")

prefixes = ["un", "re", "dis", "pre", "mis"]
suffixes = ["ing", "ed", "er", "ly", "ness"]

print("\nGenerated Words using Prefixes")
for p in prefixes:
    print(p + root)

print("\nGenerated Words using Suffixes")
for s in suffixes:
    print(root + s)


# Output:
# Enter the root word: play
#
# Generated Words using Prefixes
# unplay
# replay
# display
# preplay
# misplay
#
# Generated Words using Suffixes
# playing
# played
# player
# playly
# playness
