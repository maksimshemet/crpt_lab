﻿import re

dekrDikt = {'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4, 'е': 5, 'ж': 6, 'з': 7, 'и': 8, 'й': 9, 'к': 10, 'л': 11, 'м': 12, 'н': 13, 'о': 14, 'п': 15, 'р': 16, 'с': 17, 'т': 18, 'у': 19, 'ф': 20, 'х': 21, 'ц': 22, 'ч': 23, 'ш': 24, 'щ': 25, 'ъ': 26, 'ы': 27, 'ь': 28, 'э': 29, 'ю': 30, 'я': 31,
			 0: 'а', 1: 'б', 2: 'в', 3: 'г', 4: 'д', 5: 'е', 6: 'ж', 7: 'з', 8: 'и', 9: 'й', 10: 'к', 11: 'л', 12: 'м', 13: 'н', 14: 'о', 15: 'п', 16: 'р', 17: 'с', 18: 'т', 19: 'у', 20: 'ф', 21: 'х', 22: 'ц', 23: 'ч', 24: 'ш', 25: 'щ', 26: 'ъ', 27: 'ы', 28: 'ь', 29: 'э', 30: 'ю', 31: 'я'}

def loadfile(name):
	file = re.sub(r'[ ,-]','',(open(name,'r')).read().lower())
	return file



def crypt():
	file = loadfile("file")
	print(file[6])
	password=input("Введите пароль: ")
	password*=len(file)//len(password)+1 
	sypher=""
	i=0
	for f in file: 
		sypher+=dekrDikt.get((int(dekrDikt.get(f)) + int(dekrDikt.get(password[i])))%32) 
		i+=1
		if i==len(file)-1: break
	print("Encrypted message: "+str(sypher))
	return(str(sypher)) 

def decr():
	ciferText=input("Введите шифр: ")
	password= input("Введите пароль: ")
	password*=len(ciferText)//len(password)+1
	sypher=""
	i=0
	for f in ciferText: 
		sypher+=dekrDikt.get((int(dekrDikt.get(f)) - int(dekrDikt.get(password[i])))%32) 
		i+=1
	print("Encrypted message: "+str(sypher))

     


def main():
	crypt()
	decr()


if __name__ == '__main__':
    main()





