import cmath
a = int(input())/2
b = int(input())/2

print(str(round(cmath.phase(complex(b, a)) * 180/3.14)) + "˚")

#https://www.hackerrank.com/challenges/find-angle/problem