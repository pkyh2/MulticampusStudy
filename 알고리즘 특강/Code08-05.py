# root 연결리스트의 head와 비슷한 역할

# 함수
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

# 전역
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

# 메인
# root노드 생성
node = TreeNode()
node.data = nameAry[0]  # 첫번째 원소 root node 값 대입
root = node             # root 변수에 node 대입
memory.append(node)

# 이진 트리 생성 -> 
for name in nameAry[1:]: # 2번째 원소부터 마지막 원소까지 반복해준다.
    # 트리 번호 변수
    cnt = 2
    # 새로운 노드 생성
    node = TreeNode()
    node.data = name    # 원소값(name) 대입

    # root부터 시작 항상 root값에는 현재 노드의 정보가 들어있다. 그걸 current에 대입
    current = root
    # sort순
    while True:
        cnt += 1
        if name < current.data: # 레드벨벳 < 블핑
            # 왼쪽노드가 비어있으면 값을 넣고
            if current.left == None:
                current.left = node    # 레드벨벳
                break
            # 비어있지 않으면 current를 다시 대입 -> 값이 있는 노드를 기준으로 다시 트리생성
            current = current.left
        # 오른쪽 트리 구성
        else:
            if current.right == None:
                current.right = node
                break
            # 비어있지 않으면 current를 다시 대입
            current = current.right
        

    memory.append(node)
for i in range(len(memory)):
    print(memory[i].data, end=' ')
print('이진 탐색 트리 구성 완료')

# 이진탐색트리의 활용(검색)
findName = '마마무'
current = root
while True:
    if findName == current.data:
        print(findName, '찾음!!')
        break
    elif findName < current.data:   # 왼쪽방향
        if current.left == None:    # 검색 실패
            print(findName, '없음')
            break
        current = current.left
    else:                           # 오른쪽 방향
        if current.right == None:   # 검색 실패
            print(findName, '없음')
            break
        current = current.right

print('종료')