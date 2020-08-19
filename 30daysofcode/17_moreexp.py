class Calculator:
    def power(self, a, b):
        if b < 0 or a < 0:
            raise Exception('n and p should be non-negative')
        return a**b

myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)

# https://www.hackerrank.com/challenges/30-more-exceptions/problem