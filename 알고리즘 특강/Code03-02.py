# 함수 선언 부분
def add_data(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend
    
def insert_data(position, friend):
    # 맨뒤에 None을 추가해 전체 배열 크기를 증가
    katok.append(None)
    kLen = len(katok)
    print(kLen)

    # 맨뒤에 index에서 넣고자 하는 위치까지 1씩 감소
    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend

def delete_data(position):
    katok[position] = None
    kLen = len(katok)

    for i in range(position+1, kLen):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1])
# 전역변수 선언
katok = []
select = -1 # 1: 추가, 2:삽입, 3:삭제, 4:종료

# 메인 코드 부분
if __name__=="__main__":
    while(select!=4):
        select = int(input())

        if select == 1:
            data = input("추가할 데이터 : ")
            add_data(data)
            print(katok)
        elif select == 2:
            pos = int(input("삽입할 위치 : "))
            data = input("추가할 데이터 : ")
            insert_data(pos, data)
            print(katok)
        elif select == 3:
            pos = int(input("삽입할 위치 : "))
            delete_data(pos)
            print(katok)
        elif select == 4:
            print(katok)
            exit
        else:
            print("1 ~ 4중 하나를 입력하세요.")
            continue
