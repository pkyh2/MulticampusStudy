'''
8x8 평면에서 회문의 개수를 구하시오.
길이 입력
8x8평면 입력
'''

# 풀이1

def palindromeCheck(list):
    for i in range(len(list)//2):
        if list[i] == list.pop():
            continue
        else:
            return 0
    return 1

for t in range(10):
    length = int(input())
    board = [list(input()) for _ in range(8)]

    cnt = 0
    # 가로줄 확인
    for i in range(8):
        for j in range(8 - length + 1):
            abc = board[i][j:j+length]
            if palindromeCheck(abc):
                cnt += 1
    # 세로줄 확인
    for i in range(8):
        for j in range(8 - length + 1):
            abc = []
            for k in range(length):
                abc.append(board[k+j][i])
            if palindromeCheck(abc):
                cnt += 1
    
    print('#{} {}'.format(t+1, cnt))
