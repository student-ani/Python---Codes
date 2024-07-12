from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.tokenize import word_tokenize

#data
text_data = ['Rahul is going to university.',
             'He is an intellegent boy.',
             'Rahul lives in hariyana, India.',
             'Rahul studies in phagwara, Punjab, India.',
             'Rahul loves to go University.',
             'His university is Very Big.']

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(text_data)
feature_names = vectorizer.get_feature_names_out()
print("\nVocabulary:\n", feature_names)
print("\nBag of Words:\n", X.toarray())

'''tokenize the text
words = word_tokenize(text_data)'''