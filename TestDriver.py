"""
    main 이 포함된 테스트 드라이버
"""

import user
import datetime
import dataControl


if __name__ == '__main__':
    #test = User.SignUp()
    #date = datetime.date
    '''
    test = dataControl.DataLoader()
    test.loadData('userData.txt')
    a = test.returnData()
    print(a)
    '''

    userTest = user.SignUp()
    userTest.setData()

    # file 열기 모드는 a 덧붙인다.


