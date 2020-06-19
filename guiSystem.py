import tkinter as tk


class GUIMaker:
    def __init__(self):
        # 윈도우로 사용할 아이들

        # 등록 관련 ( 도서, 사용자 )
        self.regiWindow = None
        self.userRegistWindow = None
        self.bookRegistWindow = None

        # 검색 관련
        self.searchWindow = None
        self.userSCWindow = None
        self.bookSCWindow = None

        # 삭제 관련
        self.delWindow = None
        self.userDLWindow = None
        self.bookDLWindow = None

        # 대여 관련
        self.rentWindow = None

        window = tk.Tk()
        window.title("Library System")
        window.geometry("500x500")
        window.resizable(False, False)

        registButton = tk.Button(window, text="등록", command=self.registWindow, height=5, width=50).pack(pady=10)
        searchButton = tk.Button(window, text="조회", command=self.makSHWindow, height=5, width=50).pack(pady=10)
        deleteButton = tk.Button(window, text="삭제", command=self.deleteWindow, height=5, width=50).pack(pady=10)
        rentButton = tk.Button(window, text="대여", command=self.rentalWindow, height=5, width=50).pack(pady=10)

        quitButton = tk.Button(window, text="종료", command=quit, width=10).pack(side="right", padx=10)

        window.mainloop()

    def registWindow(self):
        """
            등록 버튼을 눌렀을 때 띄워지는 윈도우
        :return: nothing
        """
        self.regiWindow = tk.Tk()
        self.regiWindow.title("등록")
        self.regiWindow.geometry("500x270")
        userButton = tk.Button(self.regiWindow, text="사용자 등록", command=self.userRegiWindow, height=5, width=50).pack(
            pady=20)
        bookButton = tk.Button(self.regiWindow, text="도서 등록", command=self.bookRegiWindow, height=5, width=50).pack(
            pady=20)

    def userRegiWindow(self):
        """
            등록 윈도우에서 유저 버튼을 눌렀을 때 나타남.
        :return: nothing
        """
        self.regiWindow.destroy()

        self.userRegistWindow = tk.Tk()
        self.userRegistWindow.title("사용자 등록")
        self.userRegistWindow.geometry("500x300")

    def bookRegiWindow(self):
        """
            등록 윈도우에서 책 버튼을 눌렀을 때 나타남.
        :return: nothing
        """
        self.regiWindow.destroy()

        self.bookRegistWindow = tk.Tk()
        self.bookRegistWindow.title("도서 등록")
        self.bookRegistWindow.geometry("500x300")

        ##################################################################################################################
        ##################################################################################################################
        ##################################################################################################################
        ##################################################################################################################
        # 등록 부분 등록 부분 등록 부분 등록 부분 등록 부분 등록 부분 등록 부분 등록 부분 등록 부분 등록 부분 등록 부분 등록 부분 등록 부분 끝끝
        ##################################################################################################################
        ##################################################################################################################
        ##################################################################################################################
        ##################################################################################################################

    def makSHWindow(self):
        """
            조회 버튼을 눌렀을 때 띄워지는 윈도우
        :return: nothing
        """

        self.searchWindow = tk.Tk()
        self.searchWindow.title("조회")
        self.searchWindow.geometry("500x270")
        userButton = tk.Button(self.searchWindow, text="사용자 조회", command=self.userSearchWindow, height=5, width=50).pack(pady=20)
        bookButton = tk.Button(self.searchWindow, text="도서 조회", command=self.bookSearchWindow, height=5, width=50).pack(pady=20)

    def userSearchWindow(self):
        """
           조회 윈도우에서 사용자 조회 버튼을 눌렀을 때 나타남.
        :return: nothing
        """
        self.searchWindow.destroy()

        self.userSCWindow = tk.Tk()
        self.userSCWindow.title("사용자 조회")
        self.userSCWindow.geometry("500x300")

    def bookSearchWindow(self):
        """
            조회 윈도우에서 도서 조회 버튼을 눌렀을 때 작동
        :return: nothing
        """
        self.searchWindow.destroy()

        self.userSCWindow = tk.Tk()
        self.userSCWindow.title("도서 조회")
        self.userSCWindow.geometry("500x300")

    def deleteWindow(self):
        """
            삭제 기능을 담당하는 윈도우
        :param self: 클래스 자신
        :return: nothing
        """
        self.delWindow = tk.Tk()
        self.delWindow.title("삭제")
        self.delWindow.geometry("500x270")
        userButton = tk.Button(self.delWindow, text="사용자 삭제", command=self.userDeleteWindow, height=5,
                               width=50).pack(pady=20)
        bookButton = tk.Button(self.delWindow, text="도서 삭제", command=self.bookDeleteWindow, height=5, width=50).pack(
            pady=20)

    def userDeleteWindow(self):
        """
            삭제 윈도우에서 사용자 삭제를 눌렀을 때 실행되는 이벤트
        :return: nothing
        """
        self.delWindow.destroy()

        self.userDLWindow = tk.Tk()
        self.userDLWindow.title("사용자 삭제")
        self.userDLWindow.geometry("500x270")

    def bookDeleteWindow(self):
        """
            삭제 윈도우에서 도서 삭제 버튼을 클릭했을 때 실행되는 이벤트
        :return: nothing
        """
        self.delWindow.destroy()

        self.bookDLWindow = tk.Tk()
        self.bookDLWindow.title("도서 삭제")
        self.bookDLWindow.geometry("500x270")



    def rentalWindow(self):
        """
            대여 기능을 담당하는 윈도우
        :param self: 클래스 자신
        :return: nothing
        """
        self.rentWindow = tk.Tk()
        self.rentWindow.title("대여")
        self.rentWindow.geometry("500x500")


test = GUIMaker()
