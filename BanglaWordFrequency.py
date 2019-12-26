from collections import Counter
import re, string

brokenLines = []
with open("BanglaPara.txt",'r',encoding='utf-8') as file:
    readLineFromFile = file.read()

#    print(readLineFromFile)
    lines = readLineFromFile.split("\n")
    for line in lines:
        if len(line) > 0 and line[0] != '#':
            line = re.sub('[%s]' % re.escape(string.punctuation), '', line)
            if line not in brokenLines:
                brokenLines.append(line)


print(brokenLines)
s = " "
s = s.join(brokenLines)
counter = Counter(s.split())

#for x in counter:
#    print(x + " = " + str(counter[x]))

for k in sorted(counter, key=counter.get, reverse=True):
    print(k + " = " + str(counter[k]))

