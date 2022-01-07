#함수
# 노드 구조 생성
class Node():
    def __init__(self):
        # 노드는 데이터와 링크로 구성되어있다.
        self.data = None
        self.link = None

# 연결 리스트 출력
def printNodes(start):
    current = start
    print(current.data, end=' ')
    # 다음 링크가 없을 때까지 즉, None이 아닐때까지 다음링크를 current에 대입 반복
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

# 노드 삽입 삭제
def insertNode(findData, insertData):
    global memory, head, current, pre
    if head.data == findData:   # 첫 노드 앞에
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    # 중간노드 앞에 삽입
    current = head
    while current.link != None:
        # pre가 나 잡고있어
        pre = current
        # 나 다음갈게 다음링크가 없을 때 까지
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    # 마지막에 추가
    node = Node()
    node.data = insertData
    current.link = node

# 노드 삭제
def deleteNode(deleteData):
    global memory, head, current, pre
    if head.data == deleteData: # 첫번째 노드 삭제
        current = head
        head = head.link
        del(current)
        return
    # 첫 노드 외의 나머지 노드삭제
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return

def findNode(findData):
    global memory, head, current, pre
    current = head
    if current.data == findData:
        return current
    while current.link != None:
        current = current.link
        if current.data == findData:
            return current
    return Node()

# 전역
memory = []
head, current, pre = None, None, None
dataArray = ['다', '정', '쯔', '사', '지']

# 메인
node = Node()  # 첫 노드
node.data = dataArray[0]
# head는 반드시 첫 노드를 가져야 한다.
head = node
memory.append(node)

# 연결 리스트 생성
# 2번쨰 원소부터 끝 원소까지 반복
for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)


insertNode('다', '화사')
printNodes(head)
insertNode('사', '솔라')
printNodes(head)
insertNode('재남', '문별')
printNodes(head)
deleteNode('화사')
printNodes(head)
deleteNode('쯔')
printNodes(head)
deleteNode('원빈')
printNodes(head)

fNode = findNode("솔라")
print(fNode.data)
fNode = findNode("재남")
print(fNode.data)