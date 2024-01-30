import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "this is my pen"
words = word_tokenize(text)

print(words)
tag1 = pos_tag(words)
print(tag1)
