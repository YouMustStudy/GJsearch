from tkinter import *
from tkinter import ttk
import XMLParse
import pillowMAP
import gmail
from PIL import ImageTk
from search_code import *
from tkinter.messagebox import showinfo, askyesno
from time import time
from spam import getNormal

class GJsearch:
    width = 730
    height = 600
    def __init__(self):
        #Tk 기본설정
        root = Tk()
        root.configure(background='white')
        root.geometry(str(GJsearch.width)+"x"+str(GJsearch.height))
        root.resizable(width = False, height = False)
        root.title("GJsearch")

        self.basic_map = ImageTk.PhotoImage(file = "map_logo.jpg")

        #검색된 회사 리스트
        self.comList = []
        #회사 페이지 [cur, total]
        self.comPage = [0, 0]

        #즐겨찾기 리스트
        self.favList = []
        self.favPage = [0, 0]

        #사용중인 리스트
        self.curList = []
        self.curPage = []

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
        self.LB = Button(text="<", command=lambda : self.changePage("prev", self.comPageLabel, self.comPage, self.comList, self.comListbox))
        self.LB.place(x=20, y=540)
        self.RB = Button(text=">", command=lambda : self.changePage("next", self.comPageLabel, self.comPage, self.comList, self.comListbox))
        self.RB.place(x=90, y=540)
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
        Label(width = 60, height = 6, textvariable = self.comInfo).place(x=290, y=130)

        #채용 정보
        self.jobInfo = StringVar()
        self.jobInfo.set("채용정보")
        Label(text="채용정보", width=60, height=6, textvariable = self.jobInfo).place(x=290, y=230)
        self.canvas = Canvas(root, width=10, height=93, background='light gray')
        self.canvas.place(x=290, y=230)

        #지도
        self.mapImage = Label(root, image = self.basic_map, )
        self.mapImage.place(x=290, y=330)

        #즐겨찾기 버튼
        self.favButton = Button(text="북마크 모드", width=8, command=self.favMode)
        self.favButton.place(x=510, y=100)
        #공고 보기 버튼
        Button(text="공고보기", command=self.openURL).place(x=515+65, y=100)
        #메일보내기 버튼
        Button(text="메일보내기", command = self.clickMail).place(x=515+130, y=100)
        #즐겨찾기 추가/삭제 버튼
        self.addfavButton=Button(text="추가", command=self.addFav)
        self.addfavButton.place(x=470, y=100)

        root.mainloop()

    def addFav(self):
        answer = askyesno("북마크", "추가하시겠습니까?")
        if not answer:
            return

        #회사정보 출력
        try:
            index = self.comListbox.curselection()[0]
        except:
            return
        com = self.curList[20 * self.curPage[0] + index]
        self.favList.append(com)
        self.favPage[1] = len(self.favList) // 20
        self.favPage[0] = 0

    def delFav(self):
        answer = askyesno("북마크", "삭제하시겠습니까?")
        if not answer:
            return

        #회사정보 출력
        try:
            index = self.comListbox.curselection()[0]
        except:
            return
        com = self.favList[20 * self.favPage[0] + index]
        self.favList.remove(com)
        del(com)
        self.favPage[1] = len(self.favList) // 20
        self.favPage[0] = 0

        #라벨 초기화
        self.comInfo.set("회사정보")
        self.jobInfo.set("채용정보")
        self.mapImage["image"] = self.basic_map
        self.jobListbox.delete(0, END)
        self.canvas.delete("all")

        self.changePage("renew", self.comPageLabel, self.favPage, self.favList, self.comListbox)

    def favMode(self):
        #라벨 초기화
        self.comInfo.set("회사정보")
        self.jobInfo.set("채용정보")
        self.mapImage["image"] = self.basic_map
        self.jobListbox.delete(0, END)
        self.canvas.delete("all")

        #버튼 기능 변경
        self.favButton.configure(text="검색모드", command=self.searchMode)
        self.search["state"] = "disabled"

        self.addfavButton.configure(text="삭제", command=self.delFav)

        self.curList = self.favList
        self.curPage = self.favPage

        self.LB.configure(text=">", command=lambda: self.changePage("prev", self.comPageLabel, self.favPage, self.favList, self.comListbox))
        self.RB.configure(text=">", command=lambda: self.changePage("next", self.comPageLabel, self.favPage, self.favList, self.comListbox))
        self.changePage("renew", self.comPageLabel, self.favPage, self.favList, self.comListbox)

    def searchMode(self):
        #라벨 초기화
        self.comInfo.set("회사정보")
        self.jobInfo.set("채용정보")
        self.mapImage["image"] = self.basic_map
        self.jobListbox.delete(0, END)
        self.canvas.delete("all")
        
        #버튼 기능 변경
        self.favButton.configure(text="북마크 모드", command=self.favMode)
        self.search["state"] = "normal"
        self.addfavButton.configure(text="추가", command=self.addFav)



        self.curList = self.comList
        self.curPage = self.comPage

        self.LB.configure(text=">", command=lambda: self.changePage("prev", self.comPageLabel, self.comPage, self.comList, self.comListbox))
        self.RB.configure(text=">", command=lambda: self.changePage("next", self.comPageLabel, self.comPage, self.comList, self.comListbox))
        self.changePage("renew", self.comPageLabel, self.comPage, self.comList, self.comListbox)

    def clickMail(self):
        try:
            self.comListbox.curselection()[0]
        except:
            showinfo("에러발생", "회사를 선택해주세요")
            return

        root = Tk()
        Label(root, text="메일 주소 입력").pack()
        self.mail_entry = Entry(root)
        self.mail_entry.pack()
        Button(root, text="전송", command = lambda : self.sendMail(root)).pack()
        root.mainloop()

    def sendMail(self, tk):
        index = self.comListbox.curselection()[0]
        addr = self.mail_entry.get()

        try :
            gmail.send_mail(addr, self.comList[20 * self.comPage[0] + index].getString(), pillowMAP.raw_data)
        except:
            showinfo("에러발생", "전송 실패")
        else:
            showinfo("메일 전송", "전송 성공")

        tk.destroy()


    def clickSearch(self):
        #라벨 초기화
        self.comInfo.set("회사정보")
        self.jobInfo.set("채용정보")
        self.mapImage.image = self.basic_map
        self.jobListbox.delete(0, END)
        self.canvas.delete("all")

        #검색버튼 클릭
        self.comList=XMLParse.make_companyList(cityList[str(self.sigunList.get())], self.gudongData.get())

        #전체 페이지 수 계산
        self.comPage[0]=0
        self.comPage[1] = len(self.comList) // 20

        self.curList = self.comList
        self.curPage = self.comPage

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
        #라벨 초기화
        self.comInfo.set("회사정보")
        self.jobInfo.set("채용정보")
        self.mapImage["image"] = self.basic_map
        self.jobListbox.delete(0, END)
        self.canvas.delete("all")

        #회사정보 출력
        try:
            index = self.comListbox.curselection()[0]
        except:
            return

        com = self.curList[20 * self.curPage[0] + index]

        self.comInfo.set(com.getString())

        #회사위치 출력
        self.mapImage['image'] = pillowMAP.setMap( *(com.coord))

        #채용정보 생성
        self.jobList = XMLParse.make_jobList(com)

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
        try:
            index = self.jobListbox.curselection()[0]
        except:
            return
        job = self.jobList[20*self.jobPage[0]+index]
        self.jobInfo.set(job.getString())

        #남은 공고기간 색칠
        height = getNormal(job.start, int(time()), job.end)
        self.canvas.delete('all')
        self.canvas.create_rectangle(0, 93*height, 10, 93, fill = 'blue')

    def openURL(self):
        import webbrowser
        index = self.jobListbox.curselection()[0]
        webbrowser.open_new(self.jobList[20 * self.jobPage[0] + index].url)

    def showRatio(self, cur, total):
        ratio = cur/total
        w = Tk()
        w.geometry("200x200")
        c = Canvas(w, width=200, height=200)
        c.pack()
        c.create_arc(0, 0, 200, 200, start=0, extent=360, fill='blue')
        c.create_arc(0, 0, 200, 200, start=0, extent=ratio, fill='red')
        w.mainloop()

GJsearch()