import os
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

corpus = []
path = '.'
for i in os.walk(path).next()[2]:
    if i.endswith('.txt'):
        f = open(os.path.join(path,i))
        corpus.append(f.read())
frequencies = Counter([])
for text in corpus:
    token = word_tokenize(text)
    bigrams = ngrams(token, 2)
    frequencies += Counter(bigrams)

for item in frequencies.items():
    print str(item[1])+"\t"+str(' '.join(item[0]))

