'''
A사 1리터당 P원
B사 기본 요금 Q원, 월간 사용량이 R리터 이하인 경우 기본 요금만 청구
    R리터 초과인 경우 1리터당 S원추가

한 달 사용량 W
요금이 더 저렴한 회사를 골라 금액을 출력
P, Q, R, S, W
'''

# 풀이
T = int(input())
for t in range(T):
    P, Q, R, S, W = map(int, input().split())
    companyA = P*W
    if W <= R:
        companyB = Q
    else:
        companyB = Q + (abs(W - R)) * S
    
    if companyA < companyB:
        print('#{} {}'.format(t+1, companyA))
    else:
        print('#{} {}'.format(t+1, companyB))