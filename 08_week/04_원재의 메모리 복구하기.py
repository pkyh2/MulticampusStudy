'''
초기화 상태 0000 에서
원래 상태 0011 : 00'0'0 -> 0011 1번
         100 : '0'00 -> 111 -> 1'1'1 -> 0100 2번

init 값이랑 bit[i]값이 다르면 cnt += 1
'''

T = int(input())

for t in range(T):
    bit = input()
    init = '0'
    cnt = 0

    for i in range(len(bit)):
        if bit[i] != init:      # '0011' '100'
            init = bit[i]
            cnt += 1

    print('#{} {}'.format(t+1, cnt))