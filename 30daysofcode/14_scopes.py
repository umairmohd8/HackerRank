class Difference:
    def __init__(self, a):
        self.__elements = a
        self.__elements.sort()

    def computeDifference(self):
        self.maximumDifference = self.__elements[-1] - self.__elements[0]


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

# https://www.hackerrank.com/challenges/30-scope/problem?h_r=next-challenge&h_v=zen