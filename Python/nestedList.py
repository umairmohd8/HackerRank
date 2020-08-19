tab = []
n = int(input())
for _ in range(n):
    name = input()
    score = float(input())
    tab.append([name, score])
tab.sort(key=lambda x: x[1])

for i in range(1, n):
    if tab[0][1] < tab[i][1]:
        second = tab[i][1]
        tab.sort()
        break

for j in tab:
    if second == j[1]:
        print(j[0])

# https://www.hackerrank.com/challenges/nested-list/problem