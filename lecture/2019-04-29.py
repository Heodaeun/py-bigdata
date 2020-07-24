import requests
from bs4 import BeautifulSoup
import re

r = requests.get("https://www.imdb.com/?ret_=nv_home")
c = r.content
soup = BeautifulSoup(c,"html.parser")
aux = soup.find("div", {"class":"aux-content-widget-2"})
print('aux = ', aux)
Titles = aux.find_all("a")
print(Titles)
f = open('openingThisWeek.txt','w',encoding='utf-8')
for title in Titles:
    title = str(title)  #str형식 변환
    title = re.sub("<.+?>","",title,0, re.I|re.S)  #불필요한 부분 삭제
    f.write(title)
    f.write('\n')
    print(title)
f.close 