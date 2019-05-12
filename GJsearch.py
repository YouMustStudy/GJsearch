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
        Label(text="구/동/읍/면").place(x=250, y=20)
        self.gudongData = Entry(root, width=10)
        self.gudongData.place(x=250, y=40)

        root.mainloop()

GJsearch()