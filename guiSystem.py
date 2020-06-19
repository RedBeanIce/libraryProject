import tkinter as tk
from tkinter import *
import user
import book
import dataControl
from tkinter import messagebox

class GUIMaker:
    def quit(self):
        self.loopChk = False
        quit()

    def __init__(self):

        self.loopChk = True
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


        # 초기 윈도우
        self.window = tk.Tk()
        self.window.title("Library System")
        self.window.geometry("500x500")
        self.window.resizable(False, False)

        registButton = tk.Button(self.window, text="등록", command=self.registWindow, height=5, width=50).pack(pady=10)
        searchButton = tk.Button(self.window, text="조회", command=self.makSHWindow, height=5, width=50).pack(pady=10)
        deleteButton = tk.Button(self.window, text="삭제", command=self.deleteWindow, height=5, width=50).pack(pady=10)
        rentButton = tk.Button(self.window, text="대여", command=self.rentalWindow, height=5, width=50).pack(pady=10)

        quitButton = tk.Button(self.window, text="종료", command=self.quit, width=10).pack(side="right", padx=10)

        self.window.mainloop()

    def registWindow(self):
        """
            등록 버튼을 눌렀을 때 띄워지는 윈도우
        :return: nothing
        """
        self.window.destroy()

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
        self.userRegistWindow.geometry("300x300")

        name = StringVar()
        birthday = StringVar()
        sex = StringVar()
        phoneNum = StringVar()
        eMail = StringVar()

        def send_data():
            """
                입력 버튼의 이벤트.
                여기서 유저 객체를 생성하고 값들을 집어넣을 것이다.
            :return: nothing
            """
            print(name.get(), birthday.get(), sex.get(), phoneNum.get(), eMail.get())
            # 유저 패키지에 있는 SignUp 클래스를 불러 데이터 전달.
            userAdder = user.SignUp()
            flag = userAdder.addUser(name.get(), birthday.get(),sex.get(), phoneNum.get(), eMail.get())
            if flag:
                messagebox.showerror('등록 실패', '이름, 생년월일이 같은 사용자가 이미 존재. 등록실패')
            else:
                messagebox.showinfo('등록성공', '사용자 등록에 성공하셨습니다.')


        nameLabel = Label(self.userRegistWindow, text="이름").grid(row=0, column=1, sticky="W")
        nameTextBox = Entry(self.userRegistWindow, textvariable=name).grid(row=1, column=1, sticky="W")

        birthDayLabel = Label(self.userRegistWindow, text="생년월일 ex)19960203").grid(row=2, column=1, sticky="W")
        birthDayTextBox = Entry(self.userRegistWindow, textvariable=birthday).grid(row=3, column=1, sticky="W")

        sexLabel = Label(self.userRegistWindow, text="성별 남자 / 여자").grid(row=4, column=1, sticky="W")
        sexTextBox = Entry(self.userRegistWindow, textvariable=sex).grid(row=5, column=1, sticky="W")

        phoneNumLabel = Label(self.userRegistWindow, text="전화번호 ex) 01043362155").grid(row=6, column=1, sticky="W")
        phoneNumTextBox = Entry(self.userRegistWindow, textvariable=phoneNum).grid(row=7, column=1, sticky="W")

        eMailLabel = Label(self.userRegistWindow, text="이메일").grid(row=8, column=1, sticky="W")
        eMailTextBox = Entry(self.userRegistWindow, textvariable=eMail, width=30).grid(row=9, column=1, sticky="W")

        oKayButton = Button(self.userRegistWindow, text="입력 완료", width=10, command=send_data).grid(row=10, column=3)

    def bookRegiWindow(self):
        """
            등록 윈도우에서 책 버튼을 눌렀을 때 나타남.
        :return: nothing
        """

        self.regiWindow.destroy()

        self.bookRegistWindow = tk.Tk()
        self.bookRegistWindow.title("도서 등록")
        self.bookRegistWindow.geometry("500x300")

        title = StringVar()
        writer = StringVar()
        price = StringVar()
        hyperLink = StringVar()
        isbn = StringVar()
        shortDetail = StringVar()

        def send_data():
            """
            입력 버튼의 이벤트.
            여기서 유저 객체를 생성하고 값들을 집어넣을 것이다.
            :return: nothing
            """
            # 유저 패키지에 있는 SignUp 클래스를 불러 데이터 전달.
            bookAdder = book.Book()
            flag = bookAdder.addBook(title.get(), writer.get(), price.get(), hyperLink.get(), isbn.get(), shortDetail.get())
            if flag:
                messagebox.showerror('등록실패', '이미 존재하는 도서입니다. *동일한 isbn 존재')
            else:
                messagebox.showinfo('등록성공', '도서 등록에 성공하였습니다.')

        titleLabel = Label(self.bookRegistWindow, text="책 이름").grid(row=0, column=1, sticky="W")
        titleTextBox = Entry(self.bookRegistWindow, textvariable=title).grid(row=1, column=1, sticky="W")

        writerLabel = Label(self.bookRegistWindow, text="저자").grid(row=2, column=1, sticky="W")
        writerTextBox = Entry(self.bookRegistWindow, textvariable=writer).grid(row=3, column=1, sticky="W")

        priceLabel = Label(self.bookRegistWindow, text="가격 (원)").grid(row=4, column=1, sticky="W")
        priceTextBox = Entry(self.bookRegistWindow, textvariable=price).grid(row=5, column=1, sticky="W")

        hyperLinkLabel = Label(self.bookRegistWindow, text="하이퍼링크").grid(row=6, column=1, sticky="W")
        hyperLinkTextBox = Entry(self.bookRegistWindow, textvariable=hyperLink).grid(row=7, column=1, sticky="W")

        isbnLabel = Label(self.bookRegistWindow, text="isbn 값").grid(row=8, column=1, sticky="W")
        isbnTextBox = Entry(self.bookRegistWindow, textvariable=isbn).grid(row=9, column=1, sticky="W")

        shortDetailLabel = Label(self.bookRegistWindow, text="간단 설명").grid(row=8, column=1, sticky="W")
        shortDetailTextBox = Entry(self.bookRegistWindow, textvariable=shortDetail, width=50).grid(row=9, column=1, sticky="W")

        oKayButton = Button(self.bookRegistWindow, text="입력 완료", width=10, command=send_data).grid(row=10, column=3)

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
        self.window.destroy()

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

        dataLoader = dataControl.DataLoader()
        dataLoader.loadData('userData.txt')
        userlist = list()
        userlist = dataLoader.returnStringData()

        self.userSCWindow = tk.Tk()
        self.userSCWindow.title("사용자 조회")
        self.userSCWindow.geometry("500x300")

        talkingLabel = Label(self.userSCWindow, text='유저 목록').pack(pady=5)
        userListbox = Listbox(self.userSCWindow, height=0, selectmode="extended", width=30)

        for i in range(0, len(userlist)):
            userlist[i] = userlist[i].split(' ')[0] + ' ' + userlist[i].split(' ')[1]

        for i in userlist:
            print(i)
            userListbox.insert(0,i)
        userListbox.pack()


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


chk = True
while chk:

    test = GUIMaker()
    chk = test.loopChk

