x, y, z, n = (int(input()) for _ in range(4))
fin = []
for a in range(0, x + 1):
    for b in range(0, y + 1):
        for c in range(0, z + 1):
            if (a + b + c) != n:
                fin.append([a, b, c])
print(fin)


# https://www.hackerrank.com/challenges/list-comprehensions/problem