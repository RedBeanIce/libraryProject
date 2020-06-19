import dataControl


class Book:

    def __init__(self):
        """
            생성자
            이미 저장되어 있는 도서 데이터를 가져온다.
        """
        self.dataloader = dataControl.DataLoader()
        self.dataloader.loadData('bookData.txt')
        self.loadedData = self.dataloader.returnData()

        self.isbnList = self.cuttingData(self.loadedData)

        # 변수 선언부 제목, 저자, 가격, 링크, isbn, 책설명
        self.titile = None
        self.writer = None
        self.price = None
        self.hyperLink = None
        self.isbn = None
        self.bookShortDetail = None

    def addBook(self, title, writer, price, hypr, isbn, shotDtail):
        """
            도서 정보를 추가한다.
        :return: null
        """
        self.title = title
        self.writer = writer
        self.price = price
        self.hyperLink = hypr
        self.isbn = isbn
        self.bookShortDetail = shotDtail

        userData = [self.title, self.writer, self.price, self.hyperLink, self.isbn, self.bookShortDetail]

        # 유저 데이터 리스트를 만든다.
        for i in range(0, 6):
            userData[i] = userData[i].replace(' ', '%')
            # 띄어쓰기를 %로 바꾼다.

        print(userData)

        # 중복되는 isbn이 있는지 검출한다.
        chk = False
        for isbn in self.isbnList:

            if self.isbn == isbn:
                chk = True
            # if 끝
        # for 끝

        if chk:
            print('이미 존재하는 도서입니다. 도서 등록 실패 *동일한 isbn 존재')
        else:
            dataSaver = dataControl.DataSaver(userData)
            dataSaver.saveData('bookData.txt')
        return chk

    def cuttingData(self, dataList):
        """
            뭉터기로 가져온 데이터 리스트에서 내가 필요한 isbn 정보만 자른다.
        :param dataList: 책에 관련된 모든 정보가 담겨있는 리스트.
        :return: isbnList : isbn 정보만 담긴 리스트 중복 제어에 쓰인다.
        """
        isbnList = list()
        for data in dataList:
            isbnList.append(data[4])
            # 5번째에 담겨있는 데이터가 isbn 코드이기 때문에 그것만 뺀다.

        print(isbnList)

        return isbnList

    def deleteBook(self, title):
        pass

    def searchBook(self, title, writer):
        pass
