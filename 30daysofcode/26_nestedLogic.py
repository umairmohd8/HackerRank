d1, m1, y1 = map(int, input().split())
d2, m2, y2 = map(int, input().split())
if y1-y2 > 0:
    print("10000")
elif m1-m2 > 0 and y1-y2 == 0:
    print((m1-m2)*500)
elif m1-m2 == 0 and y1 -y2 ==0:
    print((d1-d2)*15)
else: print("0")

# https://www.hackerrank.com/challenges/30-nested-logic/problem