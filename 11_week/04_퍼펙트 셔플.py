T = int(input())

for t in range(T):
    N = input()
    card = input().split()
    if len(card) % 2 == 0:      # 덱의 절반이 짝수인경우
        deck1 = card[:len(card)//2]
        deck2 = card[len(card)//2:]
    else:
        deck1 = card[:len(card)//2+1]   # 3장
        deck2 = card[len(card)//2+1:]   # 2장
    for i in range(len(deck2)):
        deck1.insert(1+i*2, deck2[i])

    print('#{} {}'.format(t+1, ' '.join(deck1)))