class Coms:
    def __init__(self, name, addr, coord):
        self.name = name
        self.addr = addr
        self.coord = coord

    def getString(self):
        return "회사명\n"+self.name+"\n\n주소\n"+self.addr

class Jobs:
    def __init__(self, name, type, experience, education, keyword, salary, url):
        self.name = name
        self.type = type
        self.experience = experience
        self.education = education
        self.keyword = keyword
        self.salary = salary
        self.url=url

    def getString(self):
        return "공고명 : " + self.name + "\n채용형태 : " + self.type + "\n경력 : " + self.experience + "\n학력 : " + self.education + "\n업무 : " + self.keyword + "\n연봉 : " + self.salary