'''
T = testcase
N = 수열의 길이
M = 추가 횟수
L = 출력할 인덱스 번호

'''
# 풀이1(링크드리스트 어렵다..)
# T = int(input())

# #함수
# # 노드 구조 생성
# class Node():
#     def __init__(self):
#         # 노드는 데이터와 링크로 구성되어있다.
#         self.data = None
#         self.link = None

# def printNodes(start, index):
#     current = start
#     cnt = 0
#     if index == 0:
#         print(current.data)
#     else:
#         while current.link != None:
#             current = current.link
#             if cnt == index:
#                 print(current.data)
#                 break
#             cnt += 1
    

# def insertNum(array, index, insertNum):
#     global head, current, pre
#     # 삽입하고자 하는 숫자가 맨앞에 index일 때
#     if head.data == array[index]:
#         node = Node()
#         node.data = insertNum
#         node.link = head
#         head = node
#         return
#     # 중간 index에 삽입
#     current = head
#     while current.link != None:
#         pre = current
#         current = current.link
#         if current.data == array[index]:
#             node = Node()
#             node.data = insertNum
#             node.link = current
#             pre.link = node
#             return
#     # 마지막에 삽입
#     node = Node()
#     node.data = insertNum
#     current.link = node

# for t in range(T):
#     N, M, L = map(int, input().split())
#     # 수열 입력
#     array = list(map(int, input().split()))
#     for _ in range(M):
#         index, insertNum = map(int, input().split())

#         # 연결 리스트 구조를 위한 변수 선언
#         head, current, pre = None, None, None
#         # 첫 노드 생성 후 head에 node 삽입
#         node = Node()
#         node.data = array[0]
#         head = node

#         # 연결 리스트 생성
#         for data in array[1:]:
#             pre = node
#             node = Node()
#             node.data = data
#             pre.link = node

#         insertNum(array, index, insertNum)
#     printNodes(head, L)




# 풀이2(스택)
T = int(input())

for t in range(T):
    N, M, L = map(int, input().split())
    # 수열 입력
    array = list(map(int, input().split()))
    # 추가 횟수
    for _ in range(M):
        # 인덱스, 삽입 숫자
        index, insertNum = map(int, input().split())
        stack = []
        for _ in range(len(array) - index):
            stack.append(array.pop())
        array.append(insertNum)
        for i in stack[::-1]:
            array.append(i)
    # 결과 출력
    print('#{} {}'.format(t+1, array[L]))