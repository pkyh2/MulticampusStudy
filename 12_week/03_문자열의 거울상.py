'''
거꾸로 출력하면서
b <-> d
p <-> q
'''

T = int(input())

for t in range(T):
    str = input()
    mirror = []
    for i in str[::-1]:
        if i == 'b':
            mirror.append('d')
        elif i == 'd':
            mirror.append('b')
        elif i == 'p':
            mirror.append('q')
        elif i == 'q':
            mirror.append('p')
    print('#{} {}'.format(t+1, ''.join(mirror)))
