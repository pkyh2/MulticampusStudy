'''
N이 주어졌을 때 완전 이진트리의 루트노드 값과 N/2번에 값을 출력하시오.
트리는 중위 순회 방식으로 값이 저장된다.
'''

# 풀이1
# 노드 생성
class TreeNode():
    def __init__(self):
        self.left = None
        self.index = None
        self.right = None

# N값 입력
treeNum = list(range(1, int(input())+1))
memory = []

# 루트 노드 생성
node = TreeNode()
node.index = treeNum[0]
root = node
memory.append(node)

# 완전 이진 트리 생성
for i in treeNum[1:]:
    # 2번 트리 변수
    cnt = 2
    # 새로운 노드 생성 2 대입
    node = TreeNode()
    node.index = i

    current = root
    while True:
        if current.left == None:
            current.left = node
            break
        elif current.right == None:
            current.right = node
            break 
        else:
            current.left = node
        




    while True:
        cnt += 1
        if i < current.data:
            # 왼쪽 노드가 비어있으면 값을 넣고
            if current.left == None:
                current.left = node
                break
            # 비어있지 않으면ㅇ current를 다시 대입
            current = current.left
        # 오른쪽 트리 구성
        else:
            if current.right == None:
                pass


# 풀이2(배열로 트리구현)
T = int(input())

for t in range(T):
    N = int(input())
    tree = [1]
    for i in range(2, N):
        pass

# ing...