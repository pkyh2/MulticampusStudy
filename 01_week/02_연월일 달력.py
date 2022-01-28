'''
입력받은 문자를 년/월/일 단위로 바꾸고
월/일이 조건에 만족하면 출력 그렇지 않으면 -1을 출력

1, 3, 5, 7, 8, 10, 12월은 31일
4, 6, 9, 11월은 30일
2월은 28일
윤년은 고려하지 않는다.
'''

T = int(input())

month_12 = ['0'+str(x) for x in range(1, 10)]; month_12 += ['10', '11', '12']

for t in range(T):
    calendar = input()
    year, month, days = calendar[0:4], calendar[4:6], calendar[6:8]

    if month in month_12:
        if month == '02':
            if int(days) > 0 and int(days) <= 28:
                print('#{} {}/{}/{}'.format(t+1, year, month, days))
            else:
                print('#{} {}'.format(t+1, -1))
        elif month in ['04', '06', '09', '11']:
            if int(days) > 0 and int(days) <= 30:
                print('#{} {}/{}/{}'.format(t+1, year, month, days))
            else:
                print('#{} {}'.format(t+1, -1))
        else:
            if int(days) > 0 and int(days) <= 31:
                print('#{} {}/{}/{}'.format(t+1, year, month, days))
            else:
                print('#{} {}'.format(t+1, -1))
    else:
        print('#{} {}'.format(t+1, -1))

# T = int(input())

# month = []
# for i in range(1, 13):
#     if i < 10:
#         month.append('0' + str(i))
#     else:
#         month.append(str(i))

# for t in range(T):
#     calendar = input()
#     days_30 = ['04', '06', '09', '11']
#     if calendar[4:6] in month:
#         if calendar[4:6] == '02':
#             if int(calendar[6:8]) > 0 and int(calendar[6:8]) <= 28:
#                 print('#{} {}/{}/{}'.format(t+1, calendar[0:4], calendar[4:6], calendar[6:8]))
#             else:
#                 print('#{} {}'.format(t+1, -1))
#         elif calendar[4:6] in days_30:
#             if int(calendar[6:8]) > 0 and int(calendar[6:8]) <= 30:
#                 print('#{} {}/{}/{}'.format(t+1, calendar[0:4], calendar[4:6], calendar[6:8]))
#             else:
#                 print('#{} {}'.format(t+1, -1))
#         else:
#             if int(calendar[6:8]) > 0 and int(calendar[6:8]) <= 31:
#                 print('#{} {}/{}/{}'.format(t+1, calendar[0:4], calendar[4:6], calendar[6:8]))
#             else:
#                 print('#{} {}'.format(t+1, -1))
#     else:
#         print('#{} {}'.format(t+1, -1))
