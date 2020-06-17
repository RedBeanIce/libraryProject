"""
    파일에서 데이터 로드를 위해 존재하는 파일
"""


class DataSaver:
    """
        파일에 데이터를 저장하기 위한 클래스.
    """

    def __init__(self, dataList):
        self.dataLine = ''
        # 파일 저장을 위한 데이터라인 한 줄

        self.fomattingData(dataList)

    """
        받은 데이터를 저장한다.
    """

    def saveData(self, fileName):
        file = open(fileName, 'a')
        # file 열기 모드는 a 덧붙인다는 뜻.
        file.write(self.dataLine)

        file.close()

    def fomattingData(self, dataList):
        for i in dataList:
            makeString = str(i) + ' '
            self.dataLine = self.dataLine + makeString

        self.dataLine = self.dataLine + '\n'


class DataLoader:
    """
        기존에 존재하는 파일에서 정보를 받는다.
    """

    def __init__(self):
        self.data = list()
        # list 형태로 데이터를 내보낸다.

    def loadData(self, fileName):

        file = open(fileName, 'r')  # 한글이기 때문에 utf-8 인코딩

        while True:
            line = file.readline()

            if line == '':
                break

            self.makeList(line)
            # 한 라인씩 읽은 데이터를 리스트로 가공.

        file.close()

    """
        기존에 있던 사용자 정보를 클래스에 적재한다. 
    """

    def makeList(self, line):

        instance = line.split(' ')
        instance.pop()
        self.data.append(instance)

    def returnData(self):
        return self.data
