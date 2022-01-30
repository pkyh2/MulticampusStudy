N = int(input())
board = [[0]*N for i in range(N)]
list1 = list(range(1, N*N+1))

# 첫 줄과 맨 밑 줄
for i in range(N):
    board[0].append(list1[i])
    board[-1].append(list1[N*2+(N-3)-i])
print(board)

for i in range(1, N-1):
    board[i]