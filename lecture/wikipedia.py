import nltk
from nltk.corpus import stopwords
from collections import Counter
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import re
import operator
import csv
import pandas as pd
import copy

#Cralling
r = requests.get("https://en.wikipedia.org/wiki/Mathemetics")
c = r.content
soup = BeautifulSoup(c,"html.parser")
wiki = soup.find_all("p")
wiki = str(wiki)
print(wiki)

for i in range(1000):
        wiki = wiki.replace('[{}]'.format(i),'').strip()
wiki = wiki.replace('[','').replace(']','').strip()
wiki = re.sub('<.+?','',wiki,0,re.I|re.S)
wiki = wiki.replace(',,','.\n').strip()
wiki = wiki.replace(',','\n').strip()
print(wiki)

f = open("wiki{}.txt".format(A),'w',encoding = 'utf-8')
f.write(wiki)
f.close()

#Network
stopWords = set(stopwords.words('english'))
lematizer = nltk.wordnet.WordNetLemmatizer()
uniqueNouns = set()
sentences = []

with open('wkik{}.txt'.format(A),'r',encoding='utf-8') as f:
    lines = f.readlines()
    f.close()

for line in lines:
    tokens = nltk.word_tokenize(line)
    tags = nltk.pos_tag(tokens)
    sentences.append(tags)

    for word, tag in tags:
        word = word.lower()
        if tag in ['NN','NNS','NNP','NNPS']:
            uniqueNouns.add(word)