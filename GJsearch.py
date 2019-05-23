from tkinter import *
from tkinter import ttk
import XMLParse
from search_code import *

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
        self.comList = []
        #회사 페이지 [cur, total]
        self.comPage = [0, 0]

        #검색된 직업 리스트
        self.jobList = []
        #직업 페이지 [cur, total]
        self.jobPage = [0, 0]
        
        #시/군 콤보박스 생성
        Label(text="시/군", background='white').place(x=10, y=110)
        self.sigunData = StringVar()
        self.sigunList = ttk.Combobox(root, textvariable = self.sigunData, width = 7)
        self.sigunList['values'] = list(cityList.keys())
        self.sigunList.current(0)
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
        self.comListbox = Listbox(root, width= 15, height= 20, exportselection=0)
        self.comListbox.bind("<<ListboxSelect>>", self.selectCom)
        self.comListbox["state"] = "disabled"
        self.comListbox.place(x=10, y=200)
        #페이지 넘김 버튼
        self.comPageLabel=Label(text="0/0", background = 'white', justify='center')
        self.comPageLabel.place(x=54, y=542)
        Button(text="<", command=lambda : self.changePage("prev", self.comPageLabel, self.comPage, self.comList, self.comListbox)).place(x=20, y=540)
        Button(text=">", command=lambda : self.changePage("next", self.comPageLabel, self.comPage, self.comList, self.comListbox)).place(x=90, y=540)

        #채용공고 검색결과 리스트박스
        Label(text="채용공고", background='white').place(x=120, y=180)
        self.jobListbox = Listbox(root, width= 20, height= 20,exportselection=0)
        self.jobListbox.bind("<<ListboxSelect>>", self.selectJob)
        self.jobListbox["state"] = "disabled"
        self.jobListbox.place(x=120, y=200)
        #페이지 넘김 버튼
        self.jobPageLabel = Label(text="0/0", background = 'white', justify='center')
        self.jobPageLabel.place(x=184, y=542)
        Button(text="<", command=lambda : self.changePage("prev", self.jobPageLabel, self.jobPage, self.jobList, self.jobListbox)).place(x=150, y=540)
        Button(text=">", command=lambda : self.changePage("next", self.jobPageLabel, self.jobPage, self.jobList, self.jobListbox)).place(x=220, y=540)

        #회사 정보
        self.comInfo = StringVar()
        self.comInfo.set("회사정보")
        Label(width = 40, height = 6, textvariable = self.comInfo).place(x=290, y=130)

        #채용 정보
        self.jobInfo = StringVar()
        self.jobInfo.set("채용정보")
        Label(text="채용정보", width=40, height=6, textvariable = self.jobInfo).place(x=290, y=230)

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
        self.comList=XMLParse.make_companyList(cityList[str(self.sigunList.get())], self.gudongData.get())

        #전체 페이지 수 계산
        self.comPage[0]=0
        self.comPage[1] = len(self.comList) // 20

        #페이지 갱신
        self.comListbox["state"] = "normal"
        self.changePage("reset", self.comPageLabel, self.comPage, self.comList, self. comListbox)


    #페이지 라벨 변경
    def changePage(self, direction, label, page, data, out):
        if direction == "next":
            if page[0] < page[1]:
                page[0]+=1
            else: return
        elif direction == "prev":
            if page[0]:
                page[0]-=1
            else: return
        elif direction == "reset":
            page[0] = 0
        label.configure(text=str(page[0]+1) + '/' + str(page[1]+1))
        self.updateListbox(page, data, out)

    #리스트박스 갱신
    def updateListbox(self, page, data, out):
        out.delete(0, END)
        if data == None:
            return

        if page[0] < page[1]:
            for i in range(20):
                out.insert(END, data[20*page[0]+i].name)
        else:
            for i in range(len(data)%20):
                out.insert(END, data[20*page[0] + i].name)

    #회사 리스트 박스 클릭 시
    def selectCom(self, event):
        index = self.comListbox.curselection()[0]
        self.comInfo.set(self.comList[20*self.comPage[0]+index].getString())

        #채용정보 생성
        self.jobList = XMLParse.make_jobList(self.comList[20*self.comPage[0]+index])

        #정보없을 시 리스트박스 초기화 후 종료
        if self.jobList == None:
            self.jobPage[1]=0
            self.changePage("reset", self.jobPageLabel, self.jobPage, self.jobList, self.jobListbox)
            return

        #전체 페이지 수 계산
        self.jobPage[0]=0
        self.jobPage[1] = len(self.jobList) // 20

        #페이지 갱신
        self.jobListbox["state"] = "normal"
        self.changePage("reset", self.jobPageLabel, self.jobPage, self.jobList, self.jobListbox)

    #직업 리스트 박스 클릭 시
    def selectJob(self, event):
        index = self.jobListbox.curselection()[0]
        self.jobInfo.set(self.jobList[20*self.jobPage[0]+index].getString())

GJsearch()