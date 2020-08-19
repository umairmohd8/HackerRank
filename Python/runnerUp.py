if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse= True)
    i = 1
    runup = arr[1]
    while runup == arr[0]:
        i += 1
        runup = arr[i]
    print(runup)

# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?h_r=internal-search