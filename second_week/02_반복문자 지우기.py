'''
입력한 문자열에서 반복되는 문자열을 지운다.
남은 문자열의 길이를 출력하시오. 남은 문자열이 없으면 0을 출력한다.
'''

# 풀이1(스택)
# 스택에 문자열에서 문자를 하나씩 넣고
# 스택에 있는 문자와 스택에 들어올 문자가 같으면 .pop()을 해준다.
T = int(input())

def removeRepeat(str):
    stack = [None]
    for i in str:
        if stack[len(stack)-1] == i:
            stack.pop()
        else:
            stack.append(i)
    return stack[1:]

for t in range(T):
    string = input()
    result = len(removeRepeat(string))
    print('#{} {}'.format(t+1, result))


# 풀이2(다른방법)
for t in range(int(input())):
    str1 = input()
    
    def solution(str1):
        stack_list = []
        for i in range(len(str1)):
            if not stack_list or stack_list[-1] != str1[i]:
                stack_list.append(str1[i])
            elif stack_list or stack_list[-1] == str1[i]:
                stack_list.pop()
            
        return len(stack_list)

    print("#{} {}".format(t+1, solution(str1)))