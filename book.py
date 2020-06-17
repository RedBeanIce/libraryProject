import dataControl


class Book:

    def __init__(self):
        self.dataloader = dataControl.DataLoader('bookData.txt')
        self.loadedData = self.dataloader.returnData()

        # 변수 선언부 제목, 저자, 가격, 링크, isbn, 책설명
        self.titile = None
        self.writer = None
        self.price = None
        self.hyperLink = None
        self.isbn = None
        self.bookShortDetail = None

    def addBook(self):
        self.titile = input('책 이름 : ')
        self.writer = input('저자 : ')
        self.price = input('가격 : ')
        self.hyperLink = input('하이퍼링크 : ')
        self.isbn = input('책의 ISBN : ')
        self.bookShortDetail = input('책 간략 소개 : ')

    def deleteBook(self, title):
        pass

    def searchBook(self, title, writer):
        pass

    def isOverlap(self, title):
        pass
