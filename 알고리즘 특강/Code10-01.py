# 함수
def openBox():
    global count
    print('상자열기~~')
    count -= 1
    if count == 0:
        print('반지 넣기')
        return
    openBox()
    print('상자 닫기!!!')
    return

# 메인
count = 10
openBox()
