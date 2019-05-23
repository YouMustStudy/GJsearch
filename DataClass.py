class Coms:
    def __init__(self, name, addr, coord):
        self.name = name
        self.addr = addr
        self.coord = coord

    def getString(self):
        return "회사명 : "+self.name+"\n주소 : "+self.addr