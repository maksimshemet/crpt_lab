from collections import Counter
import operator
import re

alph = {'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4, 'е': 5, 'ж': 6, 'з': 7, 'и': 8, 'й': 9, 'к': 10, 'л': 11, 'м': 12, 'н': 13, 'о': 14, 'п': 15, 'р': 16, 'с': 17, 'т': 18, 'у': 19, 'ф': 20, 'х': 21, 'ц': 22, 'ч': 23, 'ш': 24, 'щ': 25, 'ъ': 26, 'ы': 27, 'ь': 28, 'э': 29, 'ю': 30, 'я': 31, 0:'а',  1:'б', 2:'в', 3:'г', 4:'д' , 5:'е' , 6:'ж', 7:'з', 8:'и', 9:'й', 10:'к', 11:'л', 12:'м', 13:'н', 14:'о', 15:'п', 16:'р', 17:'с', 18:'т', 19:'у', 20:'ф', 21:'х', 22:'ц', 23:'ч', 24:'ш', 25:'щ', 26:'ъ', 27:'ы', 28:'ь', 29:'э', 30:'ю', 31:'я'}
 
inputF = re.sub(r'\n','',open('file','r').read())

arr = []

passlen = input("Введите длину ключа: ")


for i in range(-1,int(passlen)):
	arrText = inputF[i::int(passlen)]
	arr.append(arrText)
	arrText = ''


while True:	
	key = input("Введите число: \nо=14 \nе=5 \nи=8 \n")
	
	if(key=='q'):break
	i=0
	pas = ''
	for x in range(1,int(passlen)+1):
		stats = dict(Counter(arr[x]))
		#print(stats)
		res = max(stats.items(), key=operator.itemgetter(1))[0]
		pas += alph.get((alph.get(res)-int(key))%32)
	print(pas)
	print("____________________________________________")


