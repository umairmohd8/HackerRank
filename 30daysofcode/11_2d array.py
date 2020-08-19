arr = []
for i in range(6):
    arr.append(list(map(int, input().split())))
val = []
for i in range(4):
    for j in range(4):
        total = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        val.append(total)
        j += 1
    i += 1
    j = 0
print(max(val))

# https://www.hackerrank.com/challenges/30-2d-arrays/problem