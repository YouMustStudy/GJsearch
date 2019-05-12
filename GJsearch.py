from tkinter import *
from tkinter import ttk

sigun = ["안양시", "과천시", "흥흥"]

class GJsearch:
    width = 800
    height = 600
    def __init__(self):
        #Tk 기본설정
        root = Tk()
        root.configure(background='white')
        root.geometry(str(GJsearch.width)+"x"+str(GJsearch.height))
        root.resizable(width = False, height = False)
        root.title("GJsearch")

        #시/군 콤보박스 생성
        Label(text="시/군").place(x=150, y=20)
        self.sigunData = StringVar()
        self.sigunList = ttk.Combobox(root, textvariable = self.sigunData, width = 7)
        self.sigunList['values'] = sigun
        self.sigunList.place(x=150, y=40)

        #구/동 엔트리 생성
        Label(text="동/읍/면").place(x=250, y=20)
        self.gudongData = Entry(root, width=10)
        self.gudongData.place(x=250, y=40)

        #회사 검색결과 리스트박스
        Label(text="게임회사").place(x=10, y=130)
        self.searchList = Listbox(root, width= 15, height= 20)
        self.searchList.place(x=10, y=150)

        #채용공고 검색결과 리스트박스
        Label(text="채용공고").place(x=120, y=130)
        self.searchList = Listbox(root, width= 20, height= 20)
        self.searchList.place(x=120, y=150)

        root.mainloop()

GJsearch()