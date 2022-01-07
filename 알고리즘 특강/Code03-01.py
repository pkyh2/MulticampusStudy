# 함수부
# 데이터 추가
def add_data(friend):   # 선형 리스트에 추가
    katok.append(None)
    kLen = len(katok)
    katok[kLen - 1] = friend

# 데이터 삽입
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

# 전역변수부
katok = []  # 선형 리스트, 빈 칸이 있으면 안된다.

# 메인코드부
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
add_data('모모')
print(katok)

insert_data(3, '미나')
insert_data(3, '유정')

print(katok)

delete_data(4)
print(katok)