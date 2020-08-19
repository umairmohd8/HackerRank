class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstname, lastname, idnumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNum
        self.scores = scores

    def calculate(self):
        val = {'O': 90, 'E': 80, 'A': 70, 'P': 55, 'D': 40, 'T': 0}
        avg = sum(self.scores) // len(self.scores)
        for y, p in val.items():
            if avg >= p:
                return y


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
# numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

# https://www.hackerrank.com/challenges/30-inheritance/problem
