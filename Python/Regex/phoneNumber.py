import re
PhoneNum = re.compile(r'[789]\d{9}$')
N = int(input())
for i in range(N):
    if PhoneNum.match(input()):
        print("YES")
    else:
        print("NO")
