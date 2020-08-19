global binum


def find(result):
    fin = []
    for i in range(len(result)):
        count = 0
        while result[i] == 1:
            count += 1
            i += 1
        fin.append(count)
    fin.sort()
    print(fin[0])


def bina(num):
    binum = []
    while num > 0:
        rem = num % 2
        num //= 2
        binum.append(rem)
    find(binum)


n = int(input())
bina(n)
