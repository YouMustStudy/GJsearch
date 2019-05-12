from tkinter import *

class GJsearch:
    width = 400
    height = 200
    def __init__(self):
        root = Tk()
        root.geometry(str(GJsearch.width)+"x"+str(GJsearch.height))
        root.resizable(width = False, height = False)
        root.title("GJsearch")

        root.mainloop()

GJsearch()