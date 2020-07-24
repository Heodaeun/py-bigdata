import nltk



#<말뭉치>--------------------------------------------------------
nltk.download('book',quiet=True)
# from nltk.book import *      #목록을 불러옴
nltk.corpus.gutenberg.fileids()

emma_raw = nltk.corpus.gutenberg.raw("austen-emma.txt")
#print(emma_raw[:1302])      #글을 불러옴(말뭉치)




#<토근 생성>------------------------------------#토큰: 긴 문자열의 분석을 위한 문자열의 작은 단위
from nltk.tokenize import sent_tokenize
print('문장 토큰: ',sent_tokenize(emma_raw[:1000])[3])        #sent_tokenize: 3문단의 첫 문장 전체를 가져옴

from nltk.tokenize import word_tokenize
print('단어 토큰: ', word_tokenize(emma_raw[50:100]))          #word_tokenize: 50:100의 문장 속에 있는 각 단어를 리스트로 만듦

from nltk.tokenize import RegexpTokenizer                    #Regexptokenizer(토큰 생성 함수): 문자열을 토큰으로 분리하는 함수
retokenize = RegexpTokenizer("[\w]+")
print('토큰 생성 함수: ',retokenize.tokenize(emma_raw[50:100]))     #문자열을 입력받아 토큰 문자열의 리스트로 출력함




#<형태소 분석>------------------------------------------------------
words = ['lives','crying','flies','dying']

from nltk.stem import PorterStemmer              #PorterStemmer(어간 추출): 변화된 단어의 접미사나 어미를 제거하여 같은 의미를 가지는 형태소의 기본형을 찾는 방법
st = PorterStemmer()                               #어간 추출법: 단순히 어미를 제거할 뿐이므로 단어 원형을 정확히 찾아주지는 않음
print('어간 추출: ',[st.stem(w) for w in words])    #겉에 []리스트로 둘러싸서, 결과가 리스트 값으로 나오는 것임

from nltk.stem import WordNetLemmatizer         #WordNetLemmatizer(원형 복원): 같은 의미를 가지는 여러 단어를 사전형으로 통일하는 작업
Im = WordNetLemmatizer()
print('원형 복원(단어): ',[Im.lemmatize(w) for w in words])       #겉에 []리스트로 둘러싸서, 결과가 리스트 값으로 나오는 것임
print('원형 복원(동사): ',Im.lemmatize("dying",pos="v"))          #겉에 []리스트 두르지 않아서, 결과가 리스트가 아님




#<POS(품사) tagging>--------------------------------------------------------
#품사: 낱말을 문법적인 기능이나 형태, 뜻에 따라 구분한 것
#NLTK -> NNP    : 단수 고유명사
#        VB     : 동사
#        VBP    : 동사 현재형
#        TO     : to 전치사
#        NN     : 명사
#        DT     : 관형사

nltk.help.upenn_tagset('VB')        #nltk.help.upenn_tagset(명령): 품사의 자세한 설명을 볼 수 있음

from nltk.tag import pos_tag       #pos_tag(명령): [('단어 토큰', '품사'), ( , ), ... ]  토큰과 품사를 부착하여 튜플로 출력
sentence = "Emma refused to permit us to obtain the refuse permit"
tagged_list = pos_tag(word_tokenize(sentence))
print('pos_tag([("단어 토큰", "품사"), ( , ), ... ]): ', tagged_list)

nouns_list = [t[0] for t in tagged_list if t[1] == "NN"]        #pos_tag를 통한 튜플 중에서 NN의 단어만 찾아냄
print(nouns_list)

from nltk.tag import untag              #튜플에서 태그 품사 제거
print('품사(태그 튜플) 제거: ',untag(tagged_list))

def tokenizer(doc):
    return ["/".join(p) for p in tagged_list]
print('tagged_list중 :',tokenizer(sentence))
