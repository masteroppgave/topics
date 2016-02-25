from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import json
from tools import twokenize
import pyLDAvis.gensim

f = open("27jan_tweets.json", "r")

lines = f.readlines()

#tweets = [json.loads(line)["text"] for line in lines]

tweets = []

for line in lines:
	try:
		tweets.append(json.loads(line)["text"])
	except:
		continue

p_stemmer = PorterStemmer()

en_stop = get_stop_words("en")

texts = [[p_stemmer.stem(token) for token in tokenizer.tokenize(doc.lower()) if not token in en_stop] for doc in tweets]

"""
tokens = [twokenize.simpleTokenize(doc.lower()) for doc in tweets]

stemmed = [[p_stemmer.stem(i) for i in token] for token in tokens]

texts = [i for i in stemmed if i not in en_stop]
"""

dictionary = corpora.Dictionary(texts)

corpus = [dictionary.doc2bow(text) for text in texts]

lda = models.ldamodel.LdaModel(corpus=corpus, num_topics = 5, id2word = dictionary, passes=10)

data = pyLDAvis.gensim.prepare(lda, corpus, dictionary)

pyLDAvis.save_html(data, "test.html")
