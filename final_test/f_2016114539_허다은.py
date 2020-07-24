from nltk.corpus import stopwords
from collections import Counter
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import re
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer
import operator
import csv
import pandas as pd
import copy
import sys
import collections

#1. Iron man 1
r = requests.get("https://www.imdb.com/title/tt0371746/plotsummary?ref_=tt_stry_pl#synopsis")
c = r.content
soup = BeautifulSoup(c,"html.parser")
Iron1 = soup.find("li",{"class":"ipl-zebra-list__item", "id":"synopsis-py3276086"})
Iron1 = str(Iron1)
Iron1 = re.sub("<.+?>", "", Iron1, 0, re.I | re.S)  # 불필요한 부분 삭제
Iron1 = Iron1.replace('Jr.', '').strip()
Iron1 = Iron1.replace('...', ' ').strip()
Iron1 = Iron1.replace('S.H.I.E.L.D.', 'shield').strip()
Iron1 = Iron1.replace('L.', 'L').strip()
Iron1 = Iron1.replace('Dr.', '').strip()
Iron1 = Iron1.replace('Tony Stark', 'Tony').strip()
Iron1 = Iron1.replace('Howard Stark', 'Howard').strip()
Iron1 = Iron1.replace('Stark','Tony').strip()
Iron1 = Iron1.replace('"Rhodey" Rhodes', 'Rhodey').strip()
Iron1 = Iron1.replace('Rhodes', 'Rhodey').strip()
Iron1 = Iron1.replace('Obadiah Stane', 'Obadiah').strip()
Iron1 = Iron1.replace('Stane', 'Obadiah').strip()
Iron1 = Iron1.replace('Christine Everhart', 'Christine').strip()
Iron1 = Iron1.replace('"Pepper" Potts', 'Pepper').strip()
Iron1 = Iron1.replace('Ho Yinsen', 'Yinsen').strip()
Iron1 = Iron1.replace('Phil Coulson', 'Coulson').strip()
Iron1 = Iron1.replace('.', '.\n').strip()
Iron1 = Iron1.replace('"', '').strip()
f = open('Iron man1.txt','w',encoding='utf-8')
f.write(Iron1)

with open('Iron man1.txt','r',encoding='utf-8') as f:
    Iron1 = f.readlines()
    f.close()
noun=[]

for iron1 in Iron1:
    iron1 = str(iron1)
    tags = pos_tag(word_tokenize(iron1))

    for word, tag in tags:
        if tag in ['NN','NNP']:
            noun.append(word)

#2. 인크레더블 헐크
r = requests.get("https://www.imdb.com/title/tt0800080/plotsummary?ref_=tt_stry_pl#synopsis")
c = r.content
soup = BeautifulSoup(c,"html.parser")
Hulk = soup.find("li",{"class":"ipl-zebra-list__item", "id":"synopsis-py3229019"})
Hulk = str(Hulk)
Hulk = re.sub("<.+?>", "", Hulk, 0, re.I | re.S)  # 불필요한 부분 삭제
Hulk = Hulk.replace('...', ' ').strip()
Hulk = Hulk.replace('..', '').strip()
Hulk = Hulk.replace('Me.', 'Me').strip()
Hulk = Hulk.replace('U.S.', 'US').strip()
Hulk = Hulk.replace('S.H.I.E.L.D.', 'SHIELD').strip()
Hulk = Hulk.replace('Jr.', '').strip()
Hulk = Hulk.replace('Mr.', '').strip()
Hulk = Hulk.replace('Tony Stark', 'Tony').strip()
Hulk = Hulk.replace('Bruce Banner', 'Bruce').strip()
Hulk = Hulk.replace('Banner', 'Bruce').strip()
Hulk = Hulk.replace('Thaddeus Thunderbolt Ross', 'Thaddeus').strip()
Hulk = Hulk.replace('Betty Ross', 'Betty').strip()
Hulk = Hulk.replace('Ross', 'Betty').strip()
Hulk = Hulk.replace('Kathleen Sparr', 'Sparr').strip()
Hulk = Hulk.replace('Joseph Greller', 'Joseph').strip()
Hulk = Hulk.replace('Emil Blonsky', 'Blonsky').strip()
Hulk = Hulk.replace('Leonard Samson', 'Samson').strip()
Hulk = Hulk.replace('Samuel Sterns', 'Samuel').strip()
Hulk = Hulk.replace('Sterns', 'Samuel').strip()
Hulk = Hulk.replace('"', '').strip()
Hulk = Hulk.replace('.', '.\n').strip()

f = open('Hulk.txt','w',encoding='utf-8')
f.write(Hulk)

with open('Hulk.txt','r',encoding='utf-8') as f:
    Hulk = f.readlines()
    f.close()

for hulk in Hulk:
    hulk = str(hulk)
    tags = pos_tag(word_tokenize(hulk))

    for word, tag in tags:
        if tag in ['NN','NNP']:
            noun.append(word)


#3. Iron man 2
r = requests.get("https://www.imdb.com/title/tt1228705/plotsummary?ref_=tt_stry_pl#synopsis")
c = r.content
soup = BeautifulSoup(c,"html.parser")
Iron2 = soup.find("li",{"class":"ipl-zebra-list__item", "id":"synopsis-py3239566"})
Iron2 = str(Iron2)
Iron2 = re.sub("<.+?>", "", Iron2, 0, re.I | re.S)  # 불필요한 부분 삭제
Iron2 = Iron2.replace('C.E.O', 'CEO').strip()
Iron2 = Iron2.replace('S.H.I.E.L.D.', 'SHIELD').strip()
Iron2 = Iron2.replace('J.A.R.V.I.S','JARVIS').strip()
Iron2 = Iron2.replace('Col.', 'Col').strip()
Iron2 = Iron2.replace('"', '').strip()
Iron2 = Iron2.replace('.', '.\n').strip()

f = open('Iron2.txt','w',encoding='utf-8')
f.write(Iron2)
with open('Iron2.txt','r',encoding='utf-8') as f:
    Iron2 = f.readlines()
    f.close()
noun.append('jarvis')

for iron2 in Iron2:
    iron2= str(iron2)
    tags = pos_tag(word_tokenize(iron2))
    for word,tag in tags:
        if tag in ['NN','NNP']:
            noun.append(word)

#4. Thor 토르: 천둥의 신
r = requests.get("https://www.imdb.com/title/tt0800369/plotsummary?ref_=tt_stry_pl#synopsis")
c = r.content
soup = BeautifulSoup(c,"html.parser")
Thor = soup.find("li",{"class":"ipl-zebra-list__item", "id":"synopsis-py3229118"})
Thor = str(Thor)
Thor = re.sub("<.+?>", "", Thor, 0, re.I | re.S)  # 불필요한 부분 삭제
Thor = Thor.replace('Jane Foster', 'Jane').strip()
Thor = Thor.replace('Erik Selvig', 'Selvig').strip()
Thor = Thor.replace('Selvig', 'Selvig').strip()
Thor = Thor.replace('Darcy Lewis', 'Darcy').strip()
Thor = Thor.replace('Nick Fury', 'Fury').strip()
Thor = Thor.replace('(Samuel L. Jackson)', '').strip()
Thor = Thor.replace('"', '').strip()
Thor = Thor.replace('.', '.\n').strip()

f = open('Thor.txt','w',encoding='utf-8')
f.write(Thor)
with open('Thor.txt','r',encoding='utf-8') as f:
    Thor = f.readlines()
    f.close()

for thor in Thor:
    thor= str(thor)
    tags = pos_tag(word_tokenize(thor))
    for word,tag in tags:
        if tag in ['NN','NNP']:
            noun.append(word)

# 5. Captian America: The First Avenger 퍼스트 어벤져
r = requests.get("https://www.imdb.com/title/tt0458339/plotsummary?ref_=tt_stry_pl#synopsis")
c = r.content
soup = BeautifulSoup(c,"html.parser")
First = soup.find("li",{"class":"ipl-zebra-list__item", "id":"synopsis-py3216861"})
First = str(First)
First = re.sub("<.+?>", "", First, 0, re.I | re.S)  # 불필요한 부분 삭제
First = First.replace('...', ' ').strip()
First = First.replace('.45', '45').strip()
First = First.replace('Dr.', '').strip()
First = First.replace('.', '.\n').strip()
First = First.replace('Johann Schmidt', 'Johann').strip()
First = First.replace('Schmidt','Johann').strip()
First = First.replace('Steve Rogers', 'Rogers').strip()
First = First.replace('Steve','Rogers').strip()
First = First.replace('Howard Stark', 'Howard').strip()
First = First.replace('Abraham Erskine', 'Erskine').strip()
First = First.replace('Colonel Chester Phillips', 'Phillips').strip()
First = First.replace('Colonel Phillips', 'Phillips').strip()
First = First.replace('Peggy Carter', 'Peggy').strip()
First = First.replace('Carter','Peggy').strip()
First = First.replace('Heinz Kruger', 'Kruger').strip()
First = First.replace('Gabe Jones', 'Gabe').strip()
First = First.replace('Nick Fury', '').strip()
First = First.replace('Samuel L Jackson', 'Fury').strip()
First = First.replace('Tony Stark', 'Tony').strip()
First = First.replace('Bruce Banner', 'Bruce').strip()
First = First.replace('Black Widow', 'Natasha').strip()
First = First.replace('"', '').strip()

f = open('First.txt','w',encoding='utf-8')
f.write(First)
with open('First.txt','r',encoding='utf-8') as f:
    First = f.readlines()
    f.close()
for first in First:
    first= str(first)
    tags = pos_tag(word_tokenize(first))
    for word,tag in tags:
        if tag in ['NN','NNP']:
            noun.append(word)

#6. Marvel's The Avengers 어벤져스
r = requests.get("https://www.imdb.com/title/tt0848228/plotsummary?ref_=tt_stry_pl#synopsis")
c = r.content
soup = BeautifulSoup(c,"html.parser")
Aven = soup.find("li",{"class":"ipl-zebra-list__item", "id":"synopsis-py3230367"})
Aven = str(Aven)
Aven = re.sub("<.+?>", "", Aven, 0, re.I | re.S)  # 불필요한 부분 삭제
Aven = Aven.replace('S.H.I.E.L.D', 'SHIELD').strip()
Aven = Aven.replace('Dr.','').strip()
Aven = Aven.replace('Samuel L. Jackson','Fury').strip()
Aven = Aven.replace('Erik Selvig','Selvig').strip()
Aven = Aven.replace('Phil Coulson','Coulson').strip()
Aven = Aven.replace('Natasha Romanoff','Natasha').strip()
Aven = Aven.replace('"Hawkeye" Barton','Hawkeye').strip()
Aven = Aven.replace('Barton','Hawkeye').strip()
Aven = Aven.replace('Maria Hill','Maria').strip()
Aven = Aven.replace('Bruce Banner','Bruce').strip()
Aven = Aven.replace('Steve Rogers','Rogers').strip()
Aven = Aven.replace('Tony Stark','Tony').strip()
Aven = Aven.replace('Pepper Potts','pepper').strip()
Aven = Aven.replace('"', '').strip()
Aven = Aven.replace('.', '.\n').strip()

f = open('Aven.txt','w',encoding='utf-8')
f.write(Aven)
with open('Aven.txt','r',encoding='utf-8') as f:
    Aven = f.readlines()
    f.close()

for aven in Aven:
    aven= str(aven)
    tags = pos_tag(word_tokenize(aven))
    for word,tag in tags:
        if tag in ['NN','NNP']:
            noun.append(word)

#7. Iron man 3
r = requests.get("https://www.imdb.com/title/tt1300854/plotsummary?ref_=tt_stry_pl#synopsis")
c = r.content
soup = BeautifulSoup(c,"html.parser")
Iron3 = soup.find("li",{"class":"ipl-zebra-list__item", "id":"synopsis-py3241770"})
Iron3 = str(Iron3)
Iron3 = re.sub("<.+?>", "", Iron3, 0, re.I | re.S)  # 불필요한 부분 삭제
Iron3 = Iron3.replace('Dr.','').strip()
Iron3 = Iron3.replace('Jr.','').strip()
Iron3 = Iron3.replace('..','.').strip()
Iron3 = Iron3.replace('Maya Hansen','Maya').strip()
Iron3 = Iron3.replace('Aldrich Killian','Aldrich').strip()
Iron3 = Iron3.replace('Killian','Aldrich').strip()
Iron3 = Iron3.replace('Colonel James Rhodes','Rhodes').strip()
Iron3 = Iron3.replace('Pepper Potts','Pepper').strip()
Iron3 = Iron3.replace('Happy Hogan','Happy').strip()
Iron3 = Iron3.replace('Eric Savin','Savin').strip()
Iron3 = Iron3.replace('Harley Keener','Harley').strip()
Iron3 = Iron3.replace('Trevor Slattery ','Slattery').strip()
Iron3 = Iron3.replace('Bruce Banner','Bruce').strip()
Iron3 = Iron3.replace('"', '').strip()
Iron3 = Iron3.replace('.', '.\n').strip()

f = open('Iron3.txt','w',encoding='utf-8')
f.write(Iron3)
with open('Iron3.txt','r',encoding='utf-8') as f:
    Iron3 = f.readlines()
    f.close()

for iron3 in Iron3:
    iron3= str(iron3)
    tags = pos_tag(word_tokenize(iron3))
    for word,tag in tags:
        if tag in ['NN','NNP']:
            noun.append(word)

#8. Thor: The Dark World 토르: 다크월드
r = requests.get("https://www.imdb.com/title/tt1981115/plotsummary?ref_=tt_stry_pl#synopsis")
c = r.content
soup = BeautifulSoup(c,"html.parser")
Thor2 = soup.find("li",{"class":"ipl-zebra-list__item", "id":"synopsis-py3255367"})
Thor2 = str(Thor2)
Thor2 = re.sub("<.+?>", "", Thor2, 0, re.I | re.S)  # 불필요한 부분 삭제
Thor2 = Thor2.replace('Dr.', '').strip()
Thor2 = Thor2.replace('Dark Elf Malekith', 'Malekith').strip()
Thor2 = Thor2.replace('Jane Foster', 'Jane').strip()
Thor2 = Thor2.replace('Darcy Lewis', 'Darcy').strip()
Thor2 = Thor2.replace('Eric Selvig', 'Selvig').strip()
Thor2 = Thor2.replace('"', '').strip()
Thor2 = Thor2.replace('.', '.\n').strip()

f = open('Thor2.txt','w',encoding='utf-8')
f.write(Thor2)
with open('Thor2.txt','r',encoding='utf-8') as f:
    Thor2 = f.readlines()
    f.close()

for thor2 in Thor2:
    thor2= str(thor2)
    tags = pos_tag(word_tokenize(thor2))
    for word,tag in tags:
        if tag in ['NN','NNP']:
            noun.append(word)

#9. Captain America: The Winter Soldier 캡틴아메리카: 원터솔져
r = requests.get("https://www.imdb.com/title/tt1843866/plotsummary?ref_=tt_stry_pl#synopsis")
c = r.content
soup = BeautifulSoup(c,"html.parser")
Winter = soup.find("li",{"class":"ipl-zebra-list__item", "id":"synopsis-py3253321"})
Winter = str(Winter)
Winter = re.sub("<.+?>", "", Winter, 0, re.I | re.S)  # 불필요한 부분 삭제
Winter = Winter.replace('D.C.', '').strip()
Winter = Winter.replace('a.k.a.', '').strip()
Winter = Winter.replace('Steve Rogers', 'Steve').strip()
Winter = Winter.replace('Natasha Romanoff', 'Natasha').strip()
Winter = Winter.replace('S.H.I.E.L.D.', 'SHIELD').strip()
Winter = Winter.replace('Nick Fury', 'Fury').strip()
Winter = Winter.replace('L.', '').strip()
Winter = Winter.replace('Maria Hill', 'Maria').strip()
Winter = Winter.replace('Tony Stark', 'Tony').strip()
Winter = Winter.replace('Bruce Banner', 'Bruce').strip()
Winter = Winter.replace('Stephen Strange', 'Stephen').strip()
Winter = Winter.replace('Bucky Barnes', 'Bucky').strip()
Winter = Winter.replace('...',' ').strip()
Winter = Winter.replace('Brock Rumlow','Rumlow').strip()
Winter = Winter.replace('Georges Batroc','Batroc').strip()
Winter = Winter.replace('Jasper Sitwell','Sitwell').strip()
Winter = Winter.replace('Peggy Carter','Peggy').strip()
Winter = Winter.replace('Alexander Pierce','Pierce').strip()
Winter = Winter.replace('Sharon Carter','Sharon').strip()
Winter = Winter.replace('Arnim Zola', 'Zola').strip()
Winter = Winter.replace('Councilman Singh', 'Singh').strip()
Winter = Winter.replace('Councilwoman Hawley', 'Hawley').strip()
Winter = Winter.replace('Von Strucker', 'Von').strip()
Winter = Winter.replace('Scarlet Witch', 'Scarlet').strip()
Winter = Winter.replace('"', '').strip()
Winter = Winter.replace('.', '.\n').strip()

f = open('Iron2.txt','w',encoding='utf-8')
f.write(Winter)
with open('Iron2.txt','r',encoding='utf-8') as f:
    Winter = f.readlines()
    f.close()

for winter in Winter:
    winter= str(winter)
    tags = pos_tag(word_tokenize(winter))
    for word,tag in tags:
        if tag in ['NN','NNP']:
            noun.append(word)

#10. Guardians of the Galaxy 가디언즈 오브 갤럭시
r = requests.get("https://www.imdb.com/title/tt2015381/plotsummary?ref_=tt_stry_pl#synopsis")
c = r.content
soup = BeautifulSoup(c,"html.parser")
Gal = soup.find("li",{"class":"ipl-zebra-list__item", "id":"synopsis-py3256133"})
Gal = str(Gal)
Gal = re.sub("<.+?>", "", Gal, 0, re.I | re.S)  # 불필요한 부분 삭제
Gal = Gal.replace('no.1','no1').strip()
Gal = Gal.replace('no.2','no2').strip()
Gal = Gal.replace('a.k.a.','').strip()
Gal = Gal.replace('Peter Quill','Peter').strip()
Gal = Gal.replace('"', '').strip()
Gal = Gal.replace('.', '.\n').strip()

f = open('Gal.txt','w',encoding='utf-8')
f.write(Gal)
with open('Gal.txt','r',encoding='utf-8') as f:
    Gal = f.readlines()
    f.close()

for gal in Gal:
    gal= str(gal)
    tags = pos_tag(word_tokenize(gal))
    for word,tag in tags:
        if tag in ['NN','NNP']:
            noun.append(word)

#11. Avengers: Age of Ultron 어벤져스: 에이지 오브 울트론
r = requests.get("https://www.imdb.com/title/tt2395427/plotsummary?ref_=tt_stry_pl#synopsis")
c = r.content
soup = BeautifulSoup(c,"html.parser")
Aven2 = soup.find("li",{"class":"ipl-zebra-list__item", "id":"synopsis-py3261753"})
Aven2 = str(Aven2)
Aven2 = re.sub("<.+?>", "", Aven2, 0, re.I | re.S)  # 불필요한 부분 삭제
Aven2 = Aven2.replace('...',' ').strip()
Aven2 = Aven2.replace('Dr.','').strip()
Aven2 = Aven2.replace('Tony Stark','Tony').strip()
Aven2 = Aven2.replace('Bruce Banner','Bruce').strip()
Aven2 = Aven2.replace('Clint Barton','Hawkeye').strip()
Aven2 = Aven2.replace('"', '').strip()
Aven2 = Aven2.replace('.', '.\n').strip()

f = open('Aven2.txt','w',encoding='utf-8')
f.write(Aven2)
with open('Aven2.txt','r',encoding='utf-8') as f:
    Aven2 = f.readlines()
    f.close()

for aven2 in Aven2:
    aven2= str(aven2)
    tags = pos_tag(word_tokenize(aven2))
    for word,tag in tags:
        if tag in ['NN','NNP']:
            noun.append(word)

#12. Ant-Man 앤트맨
r = requests.get("https://www.imdb.com/title/tt0478970/plotsummary?ref_=tt_stry_pl#synopsis")
c = r.content
soup = BeautifulSoup(c,"html.parser")
Ant = soup.find("li",{"class":"ipl-zebra-list__item", "id":"synopsis-py3217570"})
Ant = str(Ant)
Ant = re.sub("<.+?>", "", Ant, 0, re.I | re.S)  # 불필요한 부분 삭제
Ant = Ant.replace('T.I.','').strip()
Ant = Ant.replace('U.S.','US').strip()
Ant = Ant.replace('"', '').strip()
Ant = Ant.replace('.', '.\n').strip()

f = open('Ant.txt','w',encoding='utf-8')
f.write(Ant)
with open('Ant.txt','r',encoding='utf-8') as f:
    Ant = f.readlines()
    f.close()

for ant in Ant:
    ant= str(ant)
    tags = pos_tag(word_tokenize(ant))
    for word,tag in tags:
        if tag in ['NN','NNP']:
            noun.append(word)

#13. Captain America: Civil War 캡틴아메리카: 시빌워
r = requests.get("https://www.imdb.com/title/tt3498820/plotsummary?ref_=tt_stry_pl#synopsis")
c = r.content
soup = BeautifulSoup(c,"html.parser")
Civil = soup.find("li",{"class":"ipl-zebra-list__item", "id":"synopsis-py3268444"})
Civil = str(Civil)
Civil = re.sub("<.+?>", "", Civil, 0, re.I | re.S)  # 불필요한 부분 삭제
Civil = Civil.replace('U.S.','US').strip()
Civil = Civil.replace('S.H.I.E.L.D.','SHIELD').strip()
Civil = Civil.replace('Jr.','').strip()
Civil = Civil.replace('.', '.\n').strip()
Civil = Civil.replace('"', '').strip()

f = open('Civil.txt','w',encoding='utf-8')
f.write(Civil)
with open('Civil.txt','r',encoding='utf-8') as f:
    Civil = f.readlines()
    f.close()

for civil in Civil:
    civil= str(civil)
    tags = pos_tag(word_tokenize(civil))
    for word,tag in tags:
        if tag in ['NN','NNP']:
            noun.append(word)

#14. Doctor Strange 닥터스트레인지
r = requests.get("https://www.imdb.com/title/tt1211837/plotsummary?ref_=tt_stry_pl#synopsis")
c = r.content
soup = BeautifulSoup(c,"html.parser")
Doctor = soup.find("li",{"class":"ipl-zebra-list__item", "id":"synopsis-py3277428"})
Doctor = str(Doctor)
Doctor = re.sub("<.+?>", "", Doctor, 0, re.I | re.S)  # 불필요한 부분 삭제
Doctor = Doctor.replace('Dr.','').strip()
Doctor = Doctor.replace('Steven Strange','Strange').strip()
Doctor = Doctor.replace('.', '.\n').strip()
Doctor = Doctor.replace('"', '').strip()

f = open('Doctor.txt','w',encoding='utf-8')
f.write(Doctor)
with open('Doctor.txt','r',encoding='utf-8') as f:
    Doctor = f.readlines()
    f.close()

for doctor in Doctor:
    doctor= str(doctor)
    tags = pos_tag(word_tokenize(doctor))
    for word,tag in tags:
        if tag in ['NN','NNP']:
            noun.append(word)

#15. Guardians of the galaxy Vol.2 가디언즈 오브 갤럭시 Vol.2
r = requests.get("https://www.imdb.com/title/tt3896198/plotsummary?ref_=tt_stry_pl#synopsis")
c = r.content
soup = BeautifulSoup(c,"html.parser")
Gal2 = soup.find("li",{"class":"ipl-zebra-list__item", "id":"synopsis-py3270263"})
Gal2 = str(Gal2)
Gal2 = re.sub("<.+?>", "", Gal2, 0, re.I | re.S)  # 불필요한 부분 삭제
Gal2 = Gal2.replace('"','').strip()
Gal2 = Gal2.replace('.', '.\n').strip()

f = open('Gal2.txt','w',encoding='utf-8')
f.write(Gal2)
with open('Gal2.txt','r',encoding='utf-8') as f:
    Gal2 = f.readlines()
    f.close()

for gal2 in Gal2:
    gal2= str(gal2)
    tags = pos_tag(word_tokenize(gal2))
    for word,tag in tags:
        if tag in ['NN','NNP']:
            noun.append(word)

#16. Spider-Man: homecoming 스파이더맨: 홈커밍
r = requests.get("https://www.imdb.com/title/tt2250912/plotsummary?ref_=tt_stry_pl#synopsis")
c = r.content
soup = BeautifulSoup(c,"html.parser")
Spider = soup.find("li",{"class":"ipl-zebra-list__item", "id":"synopsis-py3259532"})
Spider = str(Spider)
Spider = re.sub("<.+?>", "", Spider, 0, re.I | re.S)  # 불필요한 부분 삭제
Spider = Spider.replace('Jr.','').strip()
Spider = Spider.replace('"', '').strip()
Spider = Spider.replace('.', '.\n').strip()

f = open('Spider.txt','w',encoding='utf-8')
f.write(Spider)
with open('Spider.txt','r',encoding='utf-8') as f:
    Spider = f.readlines()
    f.close()

for spider in Spider:
    spider= str(spider)
    tags = pos_tag(word_tokenize(spider))
    for word,tag in tags:
        if tag in ['NN','NNP']:
            noun.append(word)

#17. Thor: Ragnarok 토르:라그나로크
r = requests.get("https://www.imdb.com/title/tt3501632/plotsummary?ref_=tt_stry_pl#synopsis")
c = r.content
soup = BeautifulSoup(c,"html.parser")
Thor3 = soup.find("li",{"class":"ipl-zebra-list__item", "id":"synopsis-py3573283"})
Thor3 = str(Thor3)
Thor3 = re.sub("<.+?>", "", Thor3, 0, re.I | re.S)  # 불필요한 부분 삭제
Thor3 = Thor3.replace('...',' ').strip()
Thor3 = Thor3.replace('D.C.','DC').strip()
Thor3 = Thor3.replace('U.S.','US').strip()
Thor3 = Thor3.replace('.', '.\n').strip()
Thor3 = Thor3.replace('"', '').strip()

f = open('Thor3.txt','w',encoding='utf-8')
f.write(Thor3)
with open('Thor3.txt','r',encoding='utf-8') as f:
    Thor3 = f.readlines()
    f.close()

for thor3 in Thor3:
    thor3= str(thor3)
    tags = pos_tag(word_tokenize(thor3))
    for word,tag in tags:
        if tag in ['NN','NNP']:
            noun.append(word)

#18. Black Panther 블랙팬서
r = requests.get("https://www.imdb.com/title/tt1825683/plotsummary?ref_=tt_stry_pl#synopsis")
c = r.content
soup = BeautifulSoup(c,"html.parser")
Black = soup.find("li",{"class":"ipl-zebra-list__item", "id":"synopsis-py3748588"})
Black = str(Black)
Black = re.sub("<.+?>", "", Black, 0, re.I | re.S)  # 불필요한 부분 삭제
Black = Black.replace('U.S.','US').strip()
Black = Black.replace('...',' ').strip()
Black = Black.replace('.', '.\n').strip()
Black = Black.replace('"', '').strip()

f = open('Black.txt','w',encoding='utf-8')
f.write(Black)
with open('Black.txt','r',encoding='utf-8') as f:
    Black = f.readlines()
    f.close()

for black in Black:
    black= str(black)
    tags = pos_tag(word_tokenize(black))
    for word,tag in tags:
        if tag in ['NN','NNP']:
            noun.append(word)

#19. Avengers: Infinity War 어벤져스:인피니티워
r = requests.get("https://www.imdb.com/title/tt4154756/plotsummary?ref_=tt_stry_pl#synopsis")
c = r.content
soup = BeautifulSoup(c,"html.parser")
Aven3 = soup.find("li",{"class":"ipl-zebra-list__item", "id":"synopsis-py3881753"})
Aven3 = str(Aven3)
Aven3 = re.sub("<.+?>", "", Aven3, 0, re.I | re.S)  # 불필요한 부분 삭제
Aven3 = Aven3.replace('...', ' ').strip()
Aven3 = Aven3.replace('S.H.I.E.L.D.', 'SHIELD').strip()
Aven3 = Aven3.replace('.', '.\n').strip()
Aven3 = Aven3.replace('"', '').strip()

f = open('Aven3.txt','w',encoding='utf-8')
f.write(Aven3)
with open('Aven3.txt','r',encoding='utf-8') as f:
    Aven3 = f.readlines()
    f.close()

for aven3 in Aven3:
    aven3= str(aven3)
    tags = pos_tag(word_tokenize(aven3))
    for word,tag in tags:
        if tag in ['NN','NNP']:
            noun.append(word)

#20. Ant-Man and the Wasp 앤트맨과 와스프
r = requests.get("https://www.imdb.com/title/tt5095030/plotsummary?ref_=tt_stry_pl#synopsis")
c = r.content
soup = BeautifulSoup(c,"html.parser")
Ant2 = soup.find("li",{"class":"ipl-zebra-list__item", "id":"synopsis-py3994279"})
Ant2 = str(Ant2)
Ant2 = re.sub("<.+?>", "", Ant2, 0, re.I | re.S)  # 불필요한 부분 삭제
Ant2 = Ant2.replace('.', '.\n').strip()
Ant2 = Ant2.replace('"', '').strip()

f = open('Ant2.txt','w',encoding='utf-8')
f.write(Ant2)
with open('Ant2.txt','r',encoding='utf-8') as f:
    Ant2 = f.readlines()
    f.close()

for ant2 in Ant2:
    ant2= str(ant2)
    tags = pos_tag(word_tokenize(ant2))
    for word,tag in tags:
        if tag in ['NN','NNP']:
            noun.append(word)

#21. Captain Marvel 캡틴마블
r = requests.get("https://www.imdb.com/title/tt4154664/plotsummary?ref_=tt_stry_pl#synopsis")
c = r.content
soup = BeautifulSoup(c,"html.parser")
Marvel = soup.find("li",{"class":"ipl-zebra-list__item", "id":"synopsis-py4408383"})
Marvel = str(Marvel)
Marvel = re.sub("<.+?>", "", Marvel, 0, re.I | re.S)  # 불필요한 부분 삭제
Marvel = Marvel.replace('S.H.I.E.L.D.','SHIELD').strip()
Marvel = Marvel.replace('.', '.\n').strip()
Marvel = Marvel.replace('"', '').strip()

f = open('Marvel.txt','w',encoding='utf-8')
f.write(Marvel)
with open('Marvel.txt','r',encoding='utf-8') as f:
    Marvel = f.readlines()
    f.close()

for marvel in Marvel:
    marvel= str(marvel)
    tags = pos_tag(word_tokenize(marvel))
    for word,tag in tags:
        if tag in ['NN','NNP']:
            noun.append(word)

#22. Avengers: Endgame 어벤져스: 엔드게임
r = requests.get("https://www.imdb.com/title/tt4154796/plotsummary?ref_=tt_stry_pl#synopsis")
c = r.content
soup = BeautifulSoup(c,"html.parser")
Aven4 = soup.find("li",{"class":"ipl-zebra-list__item", "id":"synopsis-py4495824"})
Aven4 = str(Aven4)
Aven4 = re.sub("<.+?>", "", Aven4, 0, re.I | re.S)  # 불필요한 부분 삭제
Aven4 = Aven4.replace('U.S.','US').strip()
Aven4 = Aven4.replace('.', '.\n').strip()
Aven4= Aven4.replace('"', '').strip()

f = open('Aven4.txt','w',encoding='utf-8')
f.write(Aven4)
with open('Aven4.txt','r',encoding='utf-8') as f:
    Aven4 = f.readlines()
    f.close()

for aven4 in Aven4:
    aven4= str(aven4)
    tags = pos_tag(word_tokenize(aven4))
    for word,tag in tags:
        if tag in ['NN','NNP']:
            noun.append(word)

#--------------------------------------------------------------------------------------------------------
noun=list(set(noun))
list=[]
list.append(Iron1)
list.append(Hulk)
list.append(Iron2)
list.append(Thor)
list.append(First)
list.append(Aven)
list.append(Iron3)
list.append(Thor2)
list.append(Winter)
list.append(Gal)
list.append(Aven2)
list.append(Ant)
list.append(Civil)
list.append(Doctor)
list.append(Gal2)
list.append(Spider)
list.append(Thor3)
list.append(Black)
list.append(Aven3)
list.append(Ant2)
list.append(Marvel)
list.append(Aven4)

B=[]
LIST1=[]

for i in list:
    for m in noun:
        for n in m:
            if n in i: B.append(1)
            else: B.append(0)
    LIST1.append(B)
    B=[]

for i in ('A','/','%','AC/DC','Dr','Jr','F','S','C','D','II','III','L','Bucky/Winter','Man/Tony','Natalie/Natasha','Quill/Star-Lord','Rogers/Captain','Wars/Trek','a/k/a/','crown/skull','partner/mentor','party/orgy'):
    noun.remove(i)

for i in range (len(noun)):
    for j in range (len(noun)):
        if i != j:
            if noun[i].lower == noun[j]:
                noun.pop(j)
noun.sort()
print(noun)

LIST1 = np.array(LIST1)
LIST2 = LIST1.T
LIST = np.dot(LIST2,LIST1)

# <그래프 그리기>---------------------------------------------------------------------------
#1 node graph
G=nx.Graph()
for i in range(len(np.dot(LIST2,LIST1))):
    for j in range(len(LIST)):
        if i != j:
            if LIST[i][j]!=0:
                G.add_edge(noun[i],noun[j], weight=LIST[i][j])

nx.draw(G,with_labels=True)
plt.show()

#2 Degree Histogram
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
degreeCount = collections.Counter(degree_sequence)
deg,cnt = zip(*degreeCount.items())
plt.bar(deg,cnt)
plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
plt.show()

#3 betweenness
G1 = nx.betweenness_centrality(G)
plt.show()

#4 closeness
G2 = nx.closeness_centrality(G)