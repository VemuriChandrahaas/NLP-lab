from pattern.text.en import conjugate

verb = input("Enter a verb: ")

print("Past Tense      :", conjugate(verb, tense="past"))
print("Present Participle :", conjugate(verb, tense="part"))


# Output:
# Enter a verb: play
# Past Tense      : played
# Present Participle : playing
