import re

check = re.compile(r'(\d)\1?(\w)\1?')
print(check.search(input()).group())

# https://www.hackerrank.com/challenges/re-group-groups/problem
