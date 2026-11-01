import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)

print("English Stop Words:")
print(stopwords.words('english'))


