# 함수
class Graph():
    def __init__(self, size):   # 정점의 개수를 넘겨받기위해 size
        self.SIZE = size
        # size x size 배열 선언
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

# 전역
G = None

# 메인
# 4 x 4 그래프 객체 생성(원소가 모두 0인)
G = Graph(4)
G.graph[0][1] = 1   # (A, B)
G.graph[0][2] = 1   # (A, C)
G.graph[0][3] = 1   # (A, D)

G.graph[1][0] = 1
G.graph[1][2] = 1
G.graph[1][3] = 1

G.graph[2][0] = 1
G.graph[2][1] = 1
G.graph[2][3] = 1

G.graph[3][0] = 1
G.graph[3][1] = 1
G.graph[3][2] = 1

# 무방향 그래프의 인접 행렬은 대각선을 기준으로 서로 대칭된다.
for row in range(4):
    for col in range(4):
        print(G.graph[row][col], end=' ')
    print()