'''
무늬 카드 번호로 정보가 주어지고
전체 덱에서 무늬별로 부족한 카드의 개수를 출력
'''

T = int(input())
for t in range(T):
    cardInfo = input()
    deck = [[] for _ in range(4)]
    flag = 0
    for i in range(0, len(cardInfo), 3):
        cardNum = cardInfo[i+1:i+3]
        if cardInfo[i] == 'S':
            if cardNum in deck[0]:
                print('#{} {}'.format(t+1, "ERROR"))
                flag = 1
                break
            else:
                deck[0].append(cardNum)
        elif cardInfo[i] == 'D':
            if cardNum in deck[1]:
                print('#{} {}'.format(t+1, "ERROR"))
                flag = 1
                break
            else:
                deck[1].append(cardNum)
        elif cardInfo[i] == 'H':
            if cardNum in deck[2]:
                print('#{} {}'.format(t+1, "ERROR"))
                flag = 1
                break
            else:
                deck[2].append(cardNum)
        elif cardInfo[i] == 'C':
            if cardNum in deck[3]:
                print('#{} {}'.format(t+1, "ERROR"))
                flag = 1
                break
            else:
                deck[3].append(cardNum)

    cardCount = []
    for i in deck:
        cardCount.append(13-len(i))
    
    if flag == 0:
        print('#{}'.format(t+1), *cardCount)