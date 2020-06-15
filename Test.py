"""
    회원 가입 관련
    필요 정보를 받는 클래스
    작성자 : 김현준
"""


class SignUp:
    """
        생성자.
        변수들을 생성한 후 변수들을 묶을 리스트를 만든다.
    """

    def __init__(self):

        self.name = ''
        self.birthday = ''
        self.sex = ''
        self.phoneNum = ''
        self.eMail = ''
        self.picture = ''

        self.instanceUserData = list()
        self.loadedData = list()

        self.loadData()
        # 기존에 존재하는 사용자 정보를 loadedData 리스트에 저장하는 함수

    """
        기존에 존재하는 사용자 정보를 받는다.
    """

    def loadData(self):

        file = open('userData.txt', 'r', encoding='UTF-8')  # 한글이기 때문에 utf-8 인코딩

        while True:
            line = file.readline()

            if line == '':
                break

            self.dataLoadInClass(line)
            # 사용자 정보를 가공하여 이름과 생년월일을 빼낸다.

        file.close()

    """
        기존에 있던 사용자 정보를 클래스에 적재한다. 
    """

    def dataLoadInClass(self, line):

        instance = line.split(' ')

        for i in range(0, 4):
            instance.pop()
        self.loadedData.append(instance)

    """
        사용자 정보를 입력받는 함수
    """

    def setData(self):

        self.name = input('이름을 입력해 주세요 : ')
        self.birthday = input('생년월일을 입력해 주세요 ex)19960203 : ')
        self.sex = input('성별을 입력해 주세요 남자 / 여자 : ')
        self.phoneNum = input('전화번호를 입력해 주세요 ex) 01043362155 : ')
        self.eMail = input('이메일을 입력해 주세요 : ')
        self.picture = input('사진경로를 입력해 주세요 : ')

        # 이름과 생일을 검사하여 같은 값이 있는지 확인
        chk = False
        chkList = [self.name, self.birthday]
        for i in self.loadedData:
            if i == chkList:
                chk = True

        if chk == True:
            print('이름과 생년월일이 같은 사람이 이미 존재합니다. ')
        else:
            pass

        self.makeUserData()
        # 입력받은 사용자 정보를 리스트화 시켜주는 함수를 실행한다.

    """
        입력받은 사용자 정보를 리스트로 만든다.
    """

    def makeUserData(self):
        self.instanceUserData.append(self.name)
        self.instanceUserData.append(self.birthday)
        self.instanceUserData.append(self.sex)
        self.instanceUserData.append(self.phoneNum)
        self.instanceUserData.append(self.eMail)
        self.instanceUserData.append(self.picture)

    """
        방금 입력받은 사용자 정보를 리턴
    """

    def getUserData(self):
        return self.instanceUserData


if __name__ == '__main__':
    d = SignUp()
    d.setData()

