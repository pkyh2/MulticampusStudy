'''
연속된 N일 동안의 물건의 매매가를 예측
하루에 최대 1만큼 구입
'''

T = int(input())

def exchange(saleprice, profit):
    sum, cnt = 0, 0
    maxIdx = saleprice.index(max(saleprice))+1      # 최댓값의 위치
    for i in range(maxIdx):                         # 그 위치까지 반복
        if i == maxIdx-1:                           # 최댓값 index일때
            profit += (saleprice[i] * cnt) - sum
            if i == len(saleprice) - 1:
                return profit
            else:
                return exchange(saleprice[i+1:], profit)
        else:
            sum += saleprice[i]                     # 최댓값이 나오기 전까지 값들을 더한다. 
            cnt += 1
    if profit == 0:
        return profit

for t in range(T):
    N = int(input())
    salePrice = list(map(int, input().split()))
    profit = 0
    
    print('#{} {}'.format(t+1, exchange(salePrice, profit)))
# 시간초과 ㅜㅜ

T = int(input())

for t in range(T):
    N = int(input())
    salePrice = list(map(int, input().split()))
    profit = 0
    buy = 0

    for i in salePrice[::-1]:
        if i > buy:
            buy = i
        profit += buy - i

    print('#{} {}'.format(t+1, profit))