#순차검색

import random
# 함수
def seqSearch(ary, fData):
    pos = -1
    for i in range(len(ary)):   # 배열을 돌면서
        if ary[i] == fData:     # 원하는 데이터를 찾으면
            pos = i             # pos에 해당 index를 대입
            break

    return pos

# 전역
dataAry = [random.randint(1, 99) for _ in range(20)]
findData = dataAry[random.randint(0, 19)]
# 메인
print('배열 -->', dataAry)
position = seqSearch(dataAry, findData)
if position == -1:
    print(findData, '없어요')
else:
    print(findData, '는', position, '위치에 있어요')