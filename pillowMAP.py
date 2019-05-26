from tkinter import *
from io import BytesIO
import urllib
import urllib.request
from PIL import Image, ImageTk
import XMLParse

MAPAPI = "https://naveropenapi.apigw.ntruss.com/map-static/v2/raster"

map_file=None

def setMap(x, y):
    # openapi로 이미지 url을 가져옴.
    url = XMLParse.buildURL(MAPAPI, w="422", h="246", format="jpg", markers="size:small|pos:"+x+"%20"+y)

    req = urllib.request.Request(url)
    req.add_header("X-NCP-APIGW-API-KEY-ID", "vg8qeonw6o")
    req.add_header("X-NCP-APIGW-API-KEY", "nJnb8oBKFe3zImX2pt1U5NpXwNRH3aDGuB4K3vrd")
    raw_data = urllib.request.urlopen(req).read()

    # 이미지변환
    global map_file
    im = Image.open(BytesIO(raw_data))
    map_file = ImageTk.PhotoImage(im)

    return map_file