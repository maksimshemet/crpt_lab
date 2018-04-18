from collections import Counter
from textwrap import wrap
import math
import re
from itertools import *

#coding = 'UTF-8'
coding = '1251'
file = '006.txt'
module = 31

dekrDikt = {'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4, 'е': 5, 'ж': 6, 'з': 7, 'и': 8, 'й': 9, 'к': 10, 'л': 11, 'м': 12, 'н': 13, 'о': 14, 'п': 15, 'р': 16, 'с': 17, 'т': 18, 'у': 19, 'ф': 20, 'х': 21, 'ц': 22, 'ч': 23, 'ш': 24, 'щ': 25, 'ь': 26, 'ы': 27, 'э': 28, 'ю': 29, 'я': 30,
			 0: 'а', 1: 'б', 2: 'в', 3: 'г', 4: 'д', 5: 'е', 6: 'ж', 7: 'з', 8: 'и', 9: 'й', 10: 'к', 11: 'л', 12: 'м', 13: 'н', 14: 'о', 15: 'п', 16: 'р', 17: 'с', 18: 'т', 19: 'у', 20: 'ф', 21: 'х', 22: 'ц', 23: 'ч', 24: 'ш', 25: 'щ', 26: 'ь', 27: 'ы', 28: 'э', 29: 'ю', 30: 'я'}

def takeSecond(elem):
    return elem[1]

def chek(l):
	return l.find('утро')

def bigrams(l):
	b = ''
	my_text = open(l, "r",encoding=coding)
	listWithLitr = wrap(my_text.read(),2)
	#listWithLitr = wrap(re.sub(r'\s+','',my_text.read()),2)
	litCount = len(listWithLitr)
	freq = Counter(listWithLitr)
	Lfreq = dict(sorted(freq.items(),key=takeSecond,reverse = True))
	a = list(Lfreq.values())
	i = 0
	for val in a:
		val = val / litCount
		b+=list(Lfreq.keys())[i]
		i = i + 1
		if i == 10 : break
	return wrap(b,2)
def evklid(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = evklid(b, a % b)
        return d, y, x - y * (a // b)

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


def eq(a,b,n):
	gc = gcd(a,b)
	gm = gcd(a,n)
	if(gm == 1):
		print((evklid(a,n)[1] * b)%n)
	elif(gm > 1):
		if(b%gm != 0):
			print("no resalt")
		else:
			b1 = b/gc
			a1 = a/gc
			n1 = n/gc
			res = (b1 * int(evklid(a1,n1)[1]))%n1
			for i in range(0,gc):
				print("x"+str(i)+" = "+str(int(res+i*n1)))
def initial():
	print("Введите значения:\nax=b(mod n)\n")
	a=int(input("a = "))
	b=int(input("b = "))
	n=int(input("n = "))
	print("\nРешение:\n")
	eq(a,b,n)




def prepBigrams(firstL,secondL):
	return firstL * module + secondL

def findAlphaAndBeta(FForX1,SForX1,FForX2,SForX2,FForY1,SForY1,FForY2,SForY2):
	X1 = prepBigrams(FForX1,SForX1)
	X2 = prepBigrams(FForX2,SForX2)
	Y1 = prepBigrams(FForY1,SForY1)
	Y2 = prepBigrams(FForY2,SForY2)

	alpha = ((Y1 - Y2) * int(evklid(X1-X2,module ** 2)[1])) % module ** 2
	beta = (Y1 - (alpha * X1)) % module ** 2
	return alpha,beta


def cript(a,b,X):
	Y = ( a*X + b ) % module ** 2
	firstLiteral = Y // module
	secondLiteral = Y - (31*(Y // module))
	return firstLiteral,secondLiteral



def deCript(a,b,Y):
	X = (evklid(a,module ** 2)[1] * (Y - b)) % module ** 2
	firstLiteral = X // module
	secondLiteral = X - (31*(X // module))	
	return firstLiteral,secondLiteral


#print(findAlphaAndBeta(17,18,13,14,17,3,6,28))
def main():
	
	freqBigr = ["ст","но","то","на","ен","по"] + bigrams(file)
	
	freqBigr = list(combinations(freqBigr,4))
	print(len(freqBigr))
	str = wrap(open(file,'r',encoding=coding).read(),2)
	
	keyList = []
	for i in freqBigr:
		key = findAlphaAndBeta(dekrDikt.get(i[0][0]),dekrDikt.get(i[0][1]),dekrDikt.get(i[1][0]),dekrDikt.get(i[1][1]),dekrDikt.get(i[2][0]),dekrDikt.get(i[2][1]),dekrDikt.get(i[3][0]),dekrDikt.get(i[3][1]))
		keyList.append(key)
	coun = 0
	c = ''
	for y in keyList:
		c = ''
		for x in str:
			Y = deCript(y[0],y[1],prepBigrams(int(dekrDikt.get(x[0])),int(dekrDikt.get(x[1]))))
			c += dekrDikt.get(Y[0])
			c += dekrDikt.get(Y[1])
		if chek(c) != -1:
			coun += 1
			print(c)
			print(y)
			print(Y[0]// module,Y[0]- (31*(Y[0] // module)),Y[1]// module,Y[1]- (31*(Y[1] // module)))
			print()			
			c = ''
		
	print(coun)


if __name__ == '__main__':
	main()
