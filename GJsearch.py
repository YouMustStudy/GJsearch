from tkinter import *
from tkinter import ttk
import XMLParse

sigun = ["안양시", "과천시", "흥흥"]


class GJsearch:
    width = 600
    height = 600
    def __init__(self):
        #Tk 기본설정
        root = Tk()
        root.configure(background='white')
        root.geometry(str(GJsearch.width)+"x"+str(GJsearch.height))
        root.resizable(width = False, height = False)
        root.title("GJsearch")

        #검색된 회사 리스트
        self.companyList = []
        
        #시/군 콤보박스 생성
        Label(text="시/군", background='white').place(x=10, y=110)
        self.sigunData = StringVar()
        self.sigunList = ttk.Combobox(root, textvariable = self.sigunData, width = 7)
        self.sigunList['values'] = sigun
        self.sigunList.place(x=10, y=130)

        #구/동 엔트리 생성
        Label(text="동/읍/면", background='white').place(x=120, y=110)
        self.gudongData = Entry(root, width=10)
        self.gudongData.place(x=120, y=130)

        #검색 버튼
        self.search = Button(root, text="검색", command=self.clickSearch)
        self.search.place(x=220, y=125)

        #회사 검색결과 리스트박스
        Label(text="게임회사", background='white').place(x=10, y=180)
        self.comList = Listbox(root, width= 15, height= 20)
        self.comList.place(x=10, y=200)
        #페이지 넘김 버튼
        self.comPage=self.comTotalPage=0
        Label(text="0/1", background = 'white').place(x=54, y=542)
        Button(text="<").place(x=20, y=540)
        Button(text=">").place(x=90, y=540)

        #채용공고 검색결과 리스트박스
        Label(text="채용공고", background='white').place(x=120, y=180)
        self.jobList = Listbox(root, width= 20, height= 20)
        self.jobList.place(x=120, y=200)
        #페이지 넘김 버튼
        Label(text="0/1", background = 'white').place(x=184, y=542)
        Button(text="<").place(x=150, y=540)
        Button(text=">").place(x=220, y=540)

        #회사 정보
        Label(text="회사정보", width = 40, height = 6).place(x=290, y=130)
        
        #채용 정보
        Label(text="채용정보", width=40, height=6).place(x=290, y=230)

        #지도
        Label(text="지도", width=40, height=16).place(x=290, y=330)

        #즐겨찾기 버튼
        Button(text="즐겨찾기").place(x=375, y=100)
        #공고 보기 버튼
        Button(text="공고보기").place(x=440, y=100)
        #메일보내기 버튼
        Button(text="메일보내기").place(x=505, y=100)

        root.mainloop()

    def clickSearch(self):
        #검색버튼 클릭
        global companyList
        companyList=XMLParse.make_companyList()
        
        #전체 페이지수
        self.comTotalPage = len(companyList) // 20
        
        #검색건수가 20건 이상이면
        if self.comTotalPage:
            for i in range(20):
                self.comList.insert(END, companyList[i].BIZPLC_NM.string)
        else:
            for i in range(len(companyList)):
                self.comList.insert(END, companyList[i].BIZPLC_NM.string)

    def changeComPage(self):
        pass


GJsearch()