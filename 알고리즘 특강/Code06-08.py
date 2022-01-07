# 함수
def isStackFull():  # is로 시작하는 함수는 boolean형태로 return 된다.
    global SIZE, stack, top
    if top >= SIZE-1:
        return True
    else:
        return False

def isStackEmpty():
    global SIZE, stack, top
    if top <= -1:
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if isStackFull():
        print('스택이 꽉!')
        return
    top += 1
    stack[top] = data

def pop():
    global SIZE, stack, top
    if isStackEmpty():
        print('스택 텅~')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top
    if isStackEmpty():
        print('스택 텅~')
        return None
    return stack[top]



# 전역 
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1

# 메인
# stack = ['커피', '녹차', '꿀물', '콜라', '환타']
# top = 4

# stack = ['커피', '녹차', '꿀물', '콜라', None]
# top = 3

# push('보리차')
# print(stack)
# push('사이다')
# print(stack)

stack = ['커피', None, None, None, None]
top = 0

print('다음 나올 예정', peek())
print(pop())
print(pop())