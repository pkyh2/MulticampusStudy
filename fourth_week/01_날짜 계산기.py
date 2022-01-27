'''
두 번째 날짜가 첫 번째 날짜의 며칠째인지?
1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31
1, 3, 5, 7, 8, 10, 12 - 31
4, 6, 9, 11 - 30
2 - 28
'''

# 5 5 8 15
T = int(input())
for t in range(T):
    month1, day1, month2, day2 = map(int, input().split())

    cnt = 0
    if month1 == month2:
        cnt += (day2 - day1 + 1)
    else:
        if month1 == 2:
            cnt = 28 - day1
        elif month1 in [4, 6, 9, 11]:
            cnt = 30 - day1
        elif month1 in [1, 3, 5, 7, 8, 10, 12]:
            cnt = 31 - day1

        month1 += 1
        while month1 <= month2:     # 5 5 8 15
            if month1 == month2:
                cnt += day2 + 1
            else:
                if month1 == 2:
                    cnt += 28
                elif month1 in [4, 6, 9, 11]:
                    cnt += 30
                elif month1 in [1, 3, 5, 7, 8, 10, 12]:
                    cnt += 31
            month1 += 1
    print('#{} {}'.format(t+1, cnt))


