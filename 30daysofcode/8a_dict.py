phone = {}
for i in range(int(input())):
    x, y = input().split()
    phone.setdefault(x, y)

while True:
    try:
        k = input()
        if k in phone:
            print(k + "=" + phone[k])
        else:
            print("Not Found")
    except:
        break

# dict1 runs without error ,but this has some problem
# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
