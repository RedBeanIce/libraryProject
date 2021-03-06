"""
    회원 가입 관련
    필요 정보를 받는 클래스
    작성자 : 김현준
"""

import dataControl


class SignUp:

    def __init__(self):
        """
            생성자.
            변수들을 생성한 후 변수들을 묶을 리스트를 만든다.
        """
        # 변수 선언부
        self.name = ''
        self.birthday = ''
        self.sex = ''
        self.phoneNum = ''
        self.eMail = ''
        self.picture = ''

        self.dataLoader = dataControl.DataLoader()
        # 파일 데이터 로딩을 위한 클래스 dataLoader 생성

        self.instanceUserData = list()
        # 입력받은 user 데이터를 list화 한 변수.

        self.dataLoader.loadData('userData.txt')
        # 파일명을 입력하면 데이터를 로딩한다.

        self.loadedData = self.dataLoader.returnData()
        # 기존에 존재하는 사용자 정보를 DataLoader 클래스를 사용하여 loadedData 리스트에 저장하는 함수

        self.loadedData = self.cuttingList()
        # 필요한 데이터만 남기고 자른다.

    def addUser(self, name, birthday, sex, phoneNum, eMail, picture="c://temp"):
        """
            사용자 정보를 입력받고 체크 후 저장.
        """
        self.name = name
        self.birthday = birthday
        self.sex = sex
        self.phoneNum = phoneNum
        self.eMail = eMail
        self.picture = picture

        # 이름과 생일을 검사하여 같은 값이 있는지 확인
        chk = False
        chkList = [self.name, self.birthday]
        for i in self.loadedData:
            if i == chkList:
                chk = True

        if chk == True:
            print('이름과 생년월일이 같은 사람이 이미 존재합니다. 사용자 등록 실패 ')
        else:
            self.makeUserData()
            # 입력받은 사용자 정보를 리스트화 시켜주는 함수를 실행한다.

            saver = dataControl.DataSaver(self.getUserData())
            saver.saveData('userData.txt')
            # DataSaver 클래스를 사용한 사용자 정보 저장.
        return chk

    def makeUserData(self):
        """
            입력받은 사용자 정보를 리스트로 만든다.
        """
        self.instanceUserData = [self.name, self.birthday, self.sex, self.phoneNum, self.eMail, self.picture]

    def getUserData(self):
        """
            방금 입력받은 사용자 정보를 리턴
            :return: 리스트화 된 유저 정보
        """
        return self.instanceUserData

    def cuttingList(self):
        """
            필요한 데이터만 두고 나머지는 삭제한다.
        :return: instanceList -> 필요한 값만 남긴 리스트.
        """
        instanceList = list()
        for i in self.loadedData:
            instanceList.append( [i[0] , i[1]])

        return instanceList

    def delete_user(self):
        pass




