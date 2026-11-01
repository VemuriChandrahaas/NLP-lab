import string

text = input("Enter text: ")

tokens = [word.strip(string.punctuation) for word in text.split()]
tokens = [word for word in tokens if word]

print("Tokens:")
for token in tokens:
    print(token)


# Output 1:
# Enter text: நான் கணினி அறிவியலை விரும்புகிறேன்.
# Tokens:
# நான்
# கணினி
# அறிவியலை
# விரும்புகிறேன்
#
# Output 2:
# Enter text: मुझे प्राकृतिक भाषा प्रसंस्करण पसंद है.
# Tokens:
# मुझे
# प्राकृतिक
# भाषा
# प्रसंस्करण
# पसंद
# है
