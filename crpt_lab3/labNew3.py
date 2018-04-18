from textwrap import wrap
from collections import Counter
from itertools import *

file  = '05.txt'   #это файл который брутим
alphSh={}
alphD={}
arr = ["а","б","в","г","д","е","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ь","ы","э","ю","я"]
i=0
z=0
for a in arr:	
	alphSh.update({a:i})
	i=i+1
for a in arr:	
	alphD.update({z:a})
	z=z+1
#print(alphSh)
#print(alphD) 
def filter(text):
	chek = dict(Counter(text)).get('о')
	chek = chek/len(text)
	if (chek >= 0.09 and chek <= 0.13):
		print(chek)
		return 1
	else: return 0

def gcd(a, b):
    # Return the GCD of a and b using Euclid's Algorithm
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    # Returns the modular inverse of a % m, which is
    # the number x such that a*x % m = 1

    if gcd(a, m) != 1:
        return None # no mod inverse if a & m aren't relatively prime

    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def findModSolution(first,second,module):
	if gcd(first,module) == 1: return ((findModInverse(first,module) * second)%module)
	if ((gcd(first,module) > 1) and (second%gcd(first,module) != 0)) : return "no solution"
	if ((gcd(first,module) > 1) and (second%gcd(first,module) == 0)) : 
			for argument in range(0,gcd(first,second)):
				print(((second/gcd(first,second)) * findModInverse((first/gcd(first,second)),(module/gcd(first,second))))%(module/gcd(first,second))+argument*(module/gcd(first,second)))

def findArgsForDecr(bigrForX1,bigrForX2,bigrForY1,bigrForY2):
	a = list(bigrForX1) #X1
	b = list(bigrForX2) #X2
	c = list(bigrForY1) #Y1
	d = list(bigrForY2) #Y2

	a = alphSh.get(a[0]) * 31 + alphSh.get(a[1])
	b = alphSh.get(b[0]) * 31 + alphSh.get(b[1])
	c = alphSh.get(c[0]) * 31 + alphSh.get(c[1])
	d = alphSh.get(d[0]) * 31 + alphSh.get(d[1])
	#print(a,b,c,d)
	#print((c-d)%31**2, (a-b)%31**2,findModInverse((a-b)%31**2,31 ** 2 ))
	if(findModInverse((a-b)%31**2,31 ** 2 ) == None):return 0
	else:	
		l = (((c-d)%31**2)*findModInverse((a-b) % 31**2, 31 ** 2))%31**2
		b = (c-(l*a))%31**2
		return l,b

def decypher(l,b,nameOfFileForDecypher):
	if (findModInverse(l,31**2) == None):
		return 0
	c = '1251'
	file = wrap(open(nameOfFileForDecypher,'r',encoding=c).read(),2)
	decypherText = ''
	for i in file:
		Y = alphSh.get(i[0]) * 31 + alphSh.get(i[1])	
		result = (findModInverse(l,31**2) * (Y-b)) % (31 **2)
		decypherText += alphD.get(result // 31)
		decypherText += alphD.get(result - (31*(result // 31)))
	return decypherText


def keyGen(file):
	def ts(s):
		return s[1]
	dBigrFile=[]
	c = '1251'
	bigramList = list(dict(sorted(Counter(wrap(open(file,'r',encoding=c).read(),2)).items(),key=ts,reverse = True)).keys())
	i=0
	while i<10:
		dBigrFile.append(bigramList[i])
		i+=1
	print(dBigrFile)
	print()
	dBigrFile = ["ст","но","то","на","ен","по"] + dBigrFile 
	dBigrFile = combinations(dBigrFile,4)
	KEY = []
	for i in dBigrFile:
		KEY.append(findArgsForDecr(i[0],i[1],i[2],i[3]))
	return KEY

def main():
	
	wordlist = keyGen(file)	
	for i in wordlist:	
		 try:
		 	wordlist.remove(0)
		 except ValueError:
		 	pass

	for i in wordlist:
		res = decypher(i[0],i[1],file)
		if res == 0:
			pass
		elif (filter(res) == 1):
			print(i)
			print(res)
			print()
			print("====================================================================")
	

if __name__ == '__main__':
		main()	