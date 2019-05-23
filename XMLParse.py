import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from DataClass import Coms, Jobs

COMAPI = "https://openapi.gg.go.kr/GameSoftwaresManufacture"
JOBAPI = "http://api.saramin.co.kr/job-search"
KEY = "672440af535e4bc5b92d67e16cd09c97"

def buildURL(API, **keys):
    #API 요청 URL 생성
    url = API + '?'
    for k in keys.keys():
        url+=str(k)+'='+str(keys[k])+'&'

    #print(url)
    return url

def make_companyList(sigun, dong):
    companyList = []
    page = 1
    
    #최대 갯수 받아오기
    url = buildURL(COMAPI, KEY=KEY, Type='xml', pSize=1, pIndex=page, SIGUN_CD=sigun)
    res = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(res, 'lxml-xml')
    total = soup.find("list_total_count")
    total = int(total.string)

    #전체 데이터 받아오기
    for i in range((total//1000)+1):
        url = buildURL(COMAPI, KEY=KEY, Type='xml', pSize=1000, pIndex=page, SIGUN_CD=sigun)
        res = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(res, 'lxml-xml')
        companys = soup.find_all('row')
        for com in companys:
            if (com.BSN_STATE_DIV_CD.string == "13"): #영업중인 업체만 필터링
                if dong in com.REFINE_LOTNO_ADDR.string:
                    companyList.append(Coms(com.BIZPLC_NM.string, com.REFINE_LOTNO_ADDR.string, (com.REFINE_WGS84_LOGT.string, com.REFINE_WGS84_LAT.string)))
        page+=1

    #영업중인 회사리스트와 전체 페이지 리턴
    return companyList


def make_jobList(com, sigun):
    jobList = []
    page = 0
    
    name = urllib.parse.quote("펄 어비스")
    
    # 최대 갯수 받아오기
    url = buildURL(JOBAPI, keywords = name, start = page, count = 100)
    res = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(res, 'lxml-xml')
    total = soup.find("jobs")
    total = eval(total["total"])

    #검색 데이터 없을 시 None 반환
    if not total:
        return None

    #전체 데이터 받아오기
    for i in range((total//100)+1):
        url = buildURL(JOBAPI, keywords=name, start=page, count=100)
        res = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(res, 'lxml-xml')
        jobs = soup.find_all('job')
        for job in jobs:
            title=job.find("title").string
            type=job.find("job-type").string
            experience=job.find("experience-level").string
            education=job.find("required-education-level").string
            keyword=job.find("job-category").string
            salary=job.find("salary").string
            url=job.find("url").string
            jobList.append(Jobs(title, type, experience, education, keyword, salary, url))
        page+=1

    return jobList


l = make_jobList("a","a")
print(l[0].keyword)