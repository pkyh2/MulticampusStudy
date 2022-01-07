import random
# 이진 검색
# 함수
def binSearch(ary, fData):
    pos = -1
    start = 0
    end = len(ary)-1

    while start <= end:         # 처음 index가 끝 index보다 작거나 같을때
        mid = (start + end) // 2
        if fData == ary[mid]:   # 중앙과 같으면
            return mid
        elif fData > ary[mid]:  # 중앙보다 작으면
            start = mid + 1
        else:                   # 중앙보다 크면
            end = mid - 1
    return pos

# 전역
dataAry = [random.randint(1, 999) for _ in range(10)]
findData = dataAry[random.randint(0, 9)]
dataAry.sort()

# 메인
print('배열 -->', dataAry)
position = binSearch(dataAry, findData)
if position == -1:
    print(findData, '없어요')
else:
    print(findData, '는', position, '위치에 있어요')