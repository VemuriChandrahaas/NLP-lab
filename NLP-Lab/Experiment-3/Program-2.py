import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet', quiet=True)

lemmatizer = WordNetLemmatizer()

words = ["cars", "studies", "playing", "better", "children"]

for word in words:
    print(word, "->", lemmatizer.lemmatize(word))


# Output:
# cars -> car
# studies -> study
# playing -> playing
# better -> better
# children -> child
