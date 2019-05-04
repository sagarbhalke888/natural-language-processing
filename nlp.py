from nltk.corpus import stopwords
import nltk
from nltk.stem import PorterStemmer
from nltk import word_tokenize,sent_tokenize
import pandas as pd
ps=PorterStemmer()
mytext= open('mahal.txt').read()


sent_tokenized=sent_tokenize(mytext)

for i in sent_tokenized:
    word_tokenized = word_tokenize(i)

    tagged=nltk.pos_tag(word_tokenized)
    print(tagged)



#IN THIS CODE WE HAVE PERFORMED SENTENCE TOKENIXZING AS WELL AS WORD TOKENIZING
#WE HAD FOUND OUT THE TAGS OF EACH SENTENCE IN THE GIVEN CODE
