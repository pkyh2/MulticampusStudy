'''
초기화 상태 0000 에서
원래 상태 0011 : 00'0'0 -> 0011 1번
         100 : 0'0'00 -> 0111 -> 01'1'1 -> 0100 2번
'''

T = int(input())

for t in range(T):
    bit = input()
    init = '0'
    cnt = 0

    for i in range(len(bit)):
        if bit[i] != init:
            init = bit[i]
            cnt += 1

    print('#{} {}'.format(t+1, cnt))