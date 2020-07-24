import requests
from bs4 import BeautifulSoup
import re
import networkx as nx
import matplotlib.pyplot as plt
import collections
import numpy as np

A = []
B = []
WORD = []
LIST1= []

#<데이터 가져오기>----------------------------------------------------------------------
r = requests.get("https://www.imdb.com/?ret_=nv_home")
c = r.content
soup = BeautifulSoup(c,"html.parser")
aux = soup.find("div", {"class":"aux-content-widget-2"})
Titles = aux.find_all("a")
print(Titles)

#<영화 제목 가져오기>-------------------------------------------------------------------
for title in Titles:
    title = str(title)  #str형식 변환
    title = re.sub("<.+?>","",title,0, re.I|re.S)  #불필요한 부분 삭제
    A.append(title)
    for a in title:
        if a.isalpha():     #알파벳이면, 소문자로 변환
            a = a.lower()
        WORD.append(a)
A.pop(0)
A.pop()

#<포함된 단어 나열>---------------------------------------------------------------------
WORD = list(set(WORD))
WORD.sort()
print('WORD: ',WORD)
for i in (' ',"'"):
    WORD.remove(i)

print('WORD:', WORD)
print('A:',A)

#<행렬 만들기>----------------------------------------------------------------------------
for i in A:
    for m in WORD:
            if m in i: B.append(1)
            else: B.append(0)
    LIST1.append(B)
    B=[]

LIST1 = np.array(LIST1)
print('LIST1',LIST1)
LIST2 = LIST1.T
print('LIST2',LIST2)
LIST = np.dot(LIST2,LIST1)
print('LIST:',LIST)

#<그래프 그리기>---------------------------------------------------------------------------
G=nx.Graph()
for i in range(len(LIST)):
    for j in range(len(LIST)):
        if i != j:
            if LIST[i][j]!=0:
                G.add_edge(WORD[i],WORD[j], weight=LIST[i][j])

nx.draw(G,with_labels=True)
plt.show()