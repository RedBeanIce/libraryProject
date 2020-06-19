import tkinter as tk


class GUIMaker:
    def __init__(self):
        pass

    def registWindow(self):
        """
            윈도우 생성
        :return: x
        """
        regiWindow = tk.Tk()
        regiWindow.title("등록")
        regiWindow.geometry("500x500")

    def searchWindow(self):
        searchWindow = tk.Tk()
        searchWindow.title("조회")
        searchWindow.geometry("500x500")

    def deleteWindow(self):
        delWindow = tk.Tk()
        delWindow.title("삭제")
        delWindow.geometry("500x500")

    def rentalWindow(self):
        rentWindow = tk.Tk()
        rentWindow.title("대여")
        rentWindow.geometry("500x500")



# 윈도우 창 생성
window = tk.Tk()
window.title("Library System")
window.geometry("500x500")
window.resizable(False, False)

regiGui = GUIMaker()

registButton = tk.Button(window, text="등록", command=regiGui.registWindow, height=5, width=50).pack(pady=10)
searchButton = tk.Button(window, text="조회", command=regiGui.searchWindow, height=5, width=50).pack(pady=10)
deleteButton = tk.Button(window, text="조회", command=regiGui.deleteWindow, height=5, width=50).pack(pady=10)
rentButton = tk.Button(window, text="조회", command=regiGui.rentalWindow, height=5, width=50).pack(pady=10)

quitButton = tk.Button(window, text="종료", command=quit, width=10).pack(side="right", padx=10)



window.mainloop()