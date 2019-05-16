import urllib.request

COMAPI = "https://openapi.gg.go.kr/GameSoftwaresManufacture"
KEY = "672440af535e4bc5b92d67e16cd09c97"

def buildURL(**keys):
    #API 요청 URL 생성
    url = COMAPI + '?'
    url += "KEY="+KEY+'&Type=xml&'
    for k in keys.keys():
        url+=str(k)+keys[k]+'&'
    return url

url = buildURL()
res = urllib.request.urlopen(url)
data = res.read()

test = data.decode("utf-8")
print(test)