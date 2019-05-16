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

    url = buildURL(KEY=KEY, Type='xml', pSize=20, pIndex=1)
    res = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(res, 'lxml-xml')

    companys = soup.find_all('row')
    total = soup.find("list_total_count")

    for com in companys:
        #if (com.BSN_STATE_DIV_CD.string == "13"):
            companyList.append(com)
    print("XML Load Done")
    return companys, total