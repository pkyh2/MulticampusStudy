#함수
# 노드 구조 생성
class Node():
    def __init__(self):
        # 노드는 데이터와 링크로 구성되어있다.
        self.data = None
        self.link = None

# 메인
# 노드 생성(객체)
# node1 ~ 5까지의 연결 리스트 생성
node1 = Node()
node1.data = '다현'

node2 = Node()
node2.data = '정연'
# 이전 노드의 링크에 다음 노드객체를 대입하여 연결한다.
node1.link = node2

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5

# link로 연결되어있다는 의미
# print(node1.data, end=' ')
# print(node1.link.data, end=' ')
# print(node1.link.link.data, end=' ')
# print(node1.link.link.link.data, end=' ')
# print(node1.link.link.link.link.data, end=' ')

# 데이터 삽입
# newNode = Node()
# newNode.data = '재남'
# newNode.link = node2.link
# node2.link = newNode

# 데이터 삭제
# 3의 링크를 2의 링크에 대입하고 node3을 삭제
node2.link = node3.link
del(node3) 

current = node1
print(current.data, end=' ')
# 다음 링크가 없을 때까지 즉, None이 아닐때까지 다음링크를 current에 대입 반복
while current.link != None:
    current = current.link
    print(current.data, end=' ')