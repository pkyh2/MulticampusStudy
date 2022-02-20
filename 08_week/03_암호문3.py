'''
I(삽입) x위치, y개, s숫자들 ex) I 3위치 2개 삽입 123152 487651
D(삭제) x위치, 다음 y개 숫자 삭제 D 4위치 4개 삭제
A(추가) 암호문 맨 뒤에 y개의 숫자를 덧붙인다. A 2개 421257 796818
'''
def process(tp):
    global pw
    if tp[0] == 'I':                            # I 3186 6 111702 108909 437791 460849 808743 573893
        for i in range(0, len(tp[3:])):
            pw.insert(int(tp[1])+i, tp[3+i])
    elif tp[0] == 'D':                          # D 2199 8
        for _ in range(int(tp[2])):             # tp[2]가 반복
            del pw[int(tp[1])]
            if len(pw) == int(tp[1]):
                break
    elif tp[0] == 'A':                          # A 6 902149 801457 885061 112389 207283 358796
        for i in range(int(tp[1])):
            pw.append(tp[2+i])

for t in range(10):
    N = int(input())            # 암호문 길이
    pw = list(input().split())  # 암호문
    cmdCnt = int(input())       # 명령어 개수
    cmd = list(input().split()) # 명령어

    temp = []
    cnt = 0
    for i in cmd:
        if i in ['I', 'A', 'D'] and len(temp) > 1:
            process(temp)       # i == 'A' 일때 temp = ['I', '3186', '6', '111702', '108909', '437791', '460849', '808743', '573893']
            temp = []
            temp.append(i)      # temp = ['A']
        else:
            temp.append(i)

    print('#{} {}'.format(t+1, ' '.join(pw[:10])))