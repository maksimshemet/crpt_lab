from collections import Counter
import random


fileForChInd = "file1" #файл который шифруем разными паролями
fileFdecr = "file" #файл который нужно разшифровать
arr = ['о','е','и']

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def shifrovanie(textFile,parol,c):
	passwordForDecription = parol
	textFile = open(textFile,"r").read()
	passwordForDecription*=len(textFile)//len(parol)+1
	strokaSzashifrovanimSoobsheniem=''
	if c=='s':
		for i,j in enumerate(textFile):
			shifr=(ord(j)+ord(passwordForDecription[i]))
			#print(shifr)
			strokaSzashifrovanimSoobsheniem+=chr(shifr%32+1072)
	else: 
		for i,j in enumerate(textFile):
			shifr=(ord(j)-ord(passwordForDecription[i]))
			#print(shifr)
			strokaSzashifrovanimSoobsheniem+=chr(shifr%32+1072)
	
	return strokaSzashifrovanimSoobsheniem

def indeksSootvrtstvi9Dl9Texta(a):
	ind = 0
	file = a
	lenF = len(file)
	file = (Counter(list(file)).values())
	for x in file:
		ind+= (x*(x-1))/(lenF*(lenF-1))
	print(ind)	

def indeksDl9RaznoiDlinParol(f):	
	i = 0
	while i!=20 :
		ls = list('йцукенгшщзхъфывапролджэячсмитьбю')
		psw = ''.join([random.choice(ls) for x in range(i+2)])
		print(psw)
		indeksSootvrtstvi9Dl9Texta(shifrovanie(f,psw,'s'))
		print()
		i+=1

def poiskDlinParol9():
	file = open('file','r').read()
	for x in range(1,30):
		a = file[::x]
		print(x)
		indeksSootvrtstvi9Dl9Texta(a)

def decr(charForDecr):
	strokaSzashifrovanimSoobsheniem=''
	i=0
	file = open('file','r').read()
	for x in range(1,30):
		a = file[i::20]
		key = max(Counter(list(a)).values())
		a = get_key(Counter(list(a)),key)
		a = chr(((ord(a)-ord(charForDecr))%32) + 1072)
		strokaSzashifrovanimSoobsheniem+=a
		i+=1
	print(strokaSzashifrovanimSoobsheniem)

def main():
	 # Самостійно підібрати текст для шифрування (2-3 кб) та ключі довжини r = 2, 3,
	 # 4, 5, а також довжини 10-20 знаків. Зашифрувати обраний відкритий текст шифром
	 # Віженера з цими ключами.
	 # Підрахувати індекси відповідності для відкритого тексту та всіх одержаних
	 # шифртекстів і порівняти їх значення.
	print("ИС для открытого текста: ") 
	indeksSootvrtstvi9Dl9Texta(open(fileForChInd,'r').read())
	print("___________________________________________________")
	print("ИС для разной длины паролей: ")
	indeksDl9RaznoiDlinParol(fileForChInd)
	print()
	
	#Використовуючи наведені теоретичні відомості, розшифрувати наданий
	#шифртекст (згідно свого номеру варіанта).
	print("Разшифрованый пароль: ")
	for i in arr:
		decr(i)
	print()

	password = input("Введите пароль: ")	
	a = shifrovanie(fileFdecr,password,'')
	print(a)


if __name__ == '__main__':
	main()
	#poiskDlinParol9()