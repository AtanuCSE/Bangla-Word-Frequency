from collections import Counter
import re, string

#Read From File
brokenLines = []
with open("BanglaPara.txt",'r',encoding='utf-8') as file:
    readLineFromFile = file.read()

#    print(readLineFromFile)
    lines = readLineFromFile.split("\n")
    for line in lines:
        if len(line) > 0:
#           Punctuation Removal 
            line = re.sub('[%s]' % re.escape(string.punctuation), '', line)
            line = line.replace("।", "")
            if line not in brokenLines:
                brokenLines.append(line)


print(brokenLines)
#Count Frequency
s = " "
s = s.join(brokenLines)
counter = Counter(s.split())

#Sort the dictionary
for k in sorted(counter, key=counter.get, reverse=True):
    print(k + " = " + str(counter[k]))

