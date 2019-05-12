from tkinter import *
from tkinter import ttk

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
        self.search = Button(root, text="검색")
        self.search.place(x=220, y=125)

        #회사 검색결과 리스트박스
        Label(text="게임회사", background='white').place(x=10, y=180)
        self.searchList = Listbox(root, width= 15, height= 20)
        self.searchList.place(x=10, y=200)
        

        #채용공고 검색결과 리스트박스
        Label(text="채용공고", background='white').place(x=120, y=180)
        self.searchList = Listbox(root, width= 20, height= 20)
        self.searchList.place(x=120, y=200)

        #회사 정보
        Label(text="회사정보", width = 40, height = 6).place(x=300, y=100)
        
        #채용 정보
        Label(text="채용정보", width=40, height=6).place(x=300, y=200)

        #지도
        Label(text="지도", width=40, height=16).place(x=300, y=300)


        root.mainloop()

GJsearch()