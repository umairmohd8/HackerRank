# https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem

num = input()

try:
    print(int(num))
except ValueError:
    print('Bad String')
