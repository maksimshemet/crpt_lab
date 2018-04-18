from collections import Counter 
import math
import re
from textwrap import wrap
import operator

char_list = []
char_listB = []
days_file = re.sub(r'[!@#$%^&*(),.-_~"0-9 ]','',(open('file.txt','r')).read().lower())
#days_file = re.sub(r'[!@#$%^&*(),.-_~"0-9]','',(open('file.txt','r')).read())    #без пробела

for l in days_file:
	char_list.append(l)

char_listB = wrap(days_file,2)

def getSecond(b):
    return b[1]

freq = Counter(char_list)
freqB = Counter(char_listB)
freq = dict(sorted(freq.items(), key=getSecond,reverse = True))
freqB = dict(sorted(freqB.items(), key=getSecond,reverse = True))
lfreqV = [ v for v in freq.values() ]
lfreqK = [ k for k in freq.keys() ]

lfreqVB = [ v for v in freqB.values() ]
lfreqKB = [ k for k in freqB.keys() ]
res1 = 0
res2 =0

for i in range(len(lfreqV)):
	print(lfreqK[i]+" = "+str(int(lfreqV[i])/len(char_list)))
	res1 = res1 + (-(int(lfreqV[i])/len(char_list)*math.log(int(lfreqV[i])/len(char_list),2)))
for i in range(len(lfreqVB)):
	print(lfreqKB[i]+" = "+str(int(lfreqVB[i])/len(char_listB)))
	res2 = res2 + (-(int(lfreqVB[i])/len(char_listB)*math.log(int(lfreqVB[i])/len(char_listB),2)))

print("H1 = "+str(res1))
print("H2 = "+str(res2/2))