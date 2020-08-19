num = int(input())
s = 0
t = 0
while num > 0:
    rem = num % 2
    num //= 2
    if rem == 1:
        s += 1
        if s > t:
            t = s
    else:
        s = 0
print(t)

# https://www.hackerrank.com/challenges/30-2d-arrays/problem?h_r=next-challenge&h_v=zen
