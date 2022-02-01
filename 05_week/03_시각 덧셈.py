T = int(input())

for t in range(T):
    hour1, min1, hour2, min2 = map(int, input().split())
    total_hour = hour1 + hour2
    total_min = min1 + min2
    
    if total_min > 60:
        total_min -= 60
        total_hour += 1

    if total_hour > 12:
        total_hour -= 12

    print('#{} {} {}'.format(t+1, total_hour, total_min))