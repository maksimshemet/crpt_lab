from collections import Counter
from textwrap import wrap
import math
import re

def takeSecond(elem):
    return elem[1]

def frequency():
	print("Частоты букв:")
	print("==========================================")
	my_text = open("text.txt", "r")
	listWithLitr = list(my_text.read())
	#listWithLitr = list(re.sub(r'\s+','',my_text.read()))
	litCount = len(listWithLitr)
	freq = Counter(listWithLitr)
	Lfreq = dict(sorted(freq.items(),key=takeSecond,reverse = True))

	a = list(Lfreq.values())
	i = 0
	for val in a:
		val = val / litCount
		print(list(Lfreq.keys())[i]," = ",val)
		i = i + 1
	print("==========================================")
#print(list(Lfreq.values()))

def bigrams():
	print("Частоты биграм:")
	print("==========================================")
	my_text = open("text.txt", "r")
	listWithLitr = wrap(my_text.read(),2)
	#listWithLitr = wrap(re.sub(r'\s+','',my_text.read()),2)
	litCount = len(listWithLitr)
	freq = Counter(listWithLitr)
	Lfreq = dict(sorted(freq.items(),key=takeSecond,reverse = True))
	a = list(Lfreq.values())
	i = 0
	for val in a:
		val = val / litCount
		print(list(Lfreq.keys())[i]," = ",val)
		i = i + 1
	print("==========================================")




def H1():
	print("H1:")
	print("==========================================")
	my_text = open("text.txt", "r")
	listWithLitr = list(my_text.read())
	#listWithLitr = list(re.sub(r'\s+','',my_text.read()))
	litCount = len(listWithLitr)
	freq = Counter(listWithLitr)
	Lfreq = dict(sorted(freq.items(),key=takeSecond,reverse = True))
	a = list(Lfreq.values())
	i = 0
	res = 0
	for val in a:
		val = val / litCount
		res = res + (-(val*math.log(val,2)))
	print(res)	
	print("==========================================")


def H2():
	print("H2:")
	print("==========================================")
	my_text = open("text.txt", "r")
	#listWithLitr = wrap(my_text.read(),2)
	listWithLitr = wrap(re.sub(r'\s+','',my_text.read()),2)
	litCount = len(listWithLitr)
	freq = Counter(listWithLitr)
	Lfreq = dict(sorted(freq.items()))
	a = list(Lfreq.values())
	i = 0
	res = 0
	for val in a:
		val = val / litCount
		res = res + (-(val*math.log(val,2)))
	print(res/2)	
	print("==========================================")


def main():
	H1()
	H2()
	frequency()
	bigrams()




if __name__ == '__main__':
	main()


