import urllib.request
from bs4 import BeautifulSoup

COMAPI = "https://openapi.gg.go.kr/GameSoftwaresManufacture"
KEY = "672440af535e4bc5b92d67e16cd09c97"

def buildURL(**keys):
    #API 요청 URL 생성
    url = COMAPI + '?'
    for k in keys.keys():
        url+=str(k)+'='+str(keys[k])+'&'

    #print(url)
    return url

def make_companyList():
    companyList = []
    page = 1
    
    #최대 갯수 받아오기
    url = buildURL(KEY=KEY, Type='xml', pSize=1, pIndex=page)
    res = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(res, 'lxml-xml')
    total = soup.find("list_total_count")
    total = int(total.string)

    #전체 데이터 받아오기
    for i in range((total//1000)+1):
        url = buildURL(KEY=KEY, Type='xml', pSize=1000, pIndex=page)
        res = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(res, 'lxml-xml')
        companys = soup.find_all('row')
        for com in companys:
            if (com.BSN_STATE_DIV_CD.string == "13"): #영업중인 업체만 필터링
                companyList.append(com)

    print("XML Load Done")
    #영업중인 회사리스트와 전체 페이지 리턴
    return companys

make_companyList()