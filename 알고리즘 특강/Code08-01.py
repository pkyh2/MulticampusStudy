# 함수/클래스
# 트리노드 구조
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

# 전역

# 메인
node1 = TreeNode()
node1.data = '화사'

# rootnode의 왼쪽 노드
node2 = TreeNode()
node2.data = '솔라'
node1.left = node2

node4 = TreeNode()
node4.data = '휘인'
node2.left = node4

node5 = TreeNode()
node5.data = '쯔위'
node2.right = node5

# rootnode의 오른쪽 노드
node3 = TreeNode()
node3.data = '문별'
node1.right = node3

node6 = TreeNode()
node6.data = '선미'
node3.left = node6

print(node1.data)
print(node1.left.data, node1.right.data)    # 높이1
print(node1.left.left.data, node1.left.right.data, node1.right.left.data)   # 높이2

# 이진탐색트리
# 루트노드 기준으로 왼쪽트리는 루트노드 보다 작고, 오른쪽 트리는 루트노드보다 값이 크다