'''
N이 주어졌을 때 완전 이진트리의 루트노드 값과 N/2번에 값을 출력하시오.
트리는 중위 순회 방식으로 값이 저장된다.
'''

# 풀이1()
# 노드 생성
class Tree:
  def __init__(self, N):
    self.lst=[0]*(N+1)  # N+1 개의 0 생성
    self.N=N
    self.cnt=1
    self.numbering(1)   # 함수 실행 1번부터

  def numbering(self, num):
    if num <= N :       # 
      self.numbering(num*2)
      self.lst[num]=self.cnt
      self.cnt+=1
      self.numbering(num*2+1)

  def my_result(self):
    return ' '.join(map(str, (self.lst[1], self.lst[self.N//2])))

T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    tree=Tree(N)
    print("#{} {}".format(test_case, tree.my_result()))



# 풀이2(재귀)
def makeTree(n):
    global count
    # 배열이니까 배열크기 넘어가지 않도록
    if n <= N :
        # 왼쪽 노드는 현재 인덱스의 2배
        makeTree(n*2)
        # 더이상 못가면 값넣기
        tree[n]=count
        # 값 넣었으면 증가시키기
        count+=1
        # 우측 노드는 인덱스 2배+1
        makeTree(n*2+1)

for t in range(int(input())):
    N=int(input())
    tree=[0 for i in range(N+1)]
    count=1
    makeTree(1)
    print('#{} {} {}'.format(t+1, tree[1], tree[N//2]))



  # 재귀로 표현
def checkchild(start) :
    global N
    if start*2 <= N :
        array[start][1] = start*2
        checkchild(start*2)
    if start*2+1 <= N :
        array[start][2]=start*2+1
        checkchild(start*2+1)

# 시작점은 1번 노드
def inorder(start):
    global n
    if start :  
        inorder(array[start][1])
        array[start][0]=n
        n+=1
        inorder(array[start][2])

# 코드 구현
T=int(input())
for tc in range(T):
    N=int(input())

    array=[[0 for _ in range(3)] for __ in range(N+1) ] # 내 값, 왼쪽 자식, 오른쪽 자식
    checkchild(1)   # 1번부터 자식 있는 것까지 다 표시

    n=1
    inorder(1)

    # 결과 출력
    print("#%d" %(tc+1), array[1][0], array[N//2][0])