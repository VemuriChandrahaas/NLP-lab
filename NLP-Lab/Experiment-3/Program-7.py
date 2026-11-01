from pattern.en import pluralize, singularize, conjugate

# Noun morphology
word = "child"
print("Noun Morphology")
print("----------------")
print("Singular :", singularize(word))
print("Plural   :", pluralize(word))

# Verb morphology
verb = "play"
print("\nVerb Morphology")
print("----------------")
print("Base     :", verb)
print("Past     :", conjugate(verb, tense="past"))
print("Present  :", conjugate(verb, tense="present"))
print("Participle:", conjugate(verb, tense="present", aspect="progressive"))


# Output:
# Noun Morphology
# ----------------
# Singular : child
# Plural   : children
#
# Verb Morphology
# ----------------
# Base     : play
# Past     : played
# Present  : play
# Participle: playing
