import random
# 함수
def findMinIndex(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if(ary[minIdx] > ary[i]):
            minIdx = i
    return minIdx

# 전역
before = [random.randint(1, 99) for _ in range(20)]
after = []


# 메인
print('정렬 전 -->', before)
for i in range(len(before)):
    minPos = findMinIndex(before)   # 최소값 찾기
    after.append(before[minPos])    # 최소값을 결과 맨앞에 넣고
    del(before[minPos])             # 최소값을 지우기

print('정렬 전 -->', after)