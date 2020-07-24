#위키피디아 Python 본문 내용 긁어와서 형태소 불러와서 네트워크 짜기
import requests
from bs4 import BeautifulSoup
import re

r = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
c = r.content
soup = BeautifulSoup(c,"html.parser")
aux = soup.find("div", {"class":"aux-content-widget-2"})
print('aux = ', aux)
Titles = aux.find_all("a")

f = open('openingThisWeek.txt','w',encoding='utf-8')
for title in Titles:
    title = str(title)  #str형식 변환
    title = re.sub("<.+?>","",title,0, re.I|re.S)  #불필요한 부분 삭제
    f.write(title)
    f.write('\n')
    print(title)
f.close