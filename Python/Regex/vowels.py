import re
vowels = re.compile(r'\w[aeiouAEIOU]{2,}\w')
for i in (vowels.findall(input())):
    print(i)
