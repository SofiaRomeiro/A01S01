'''
-------------------------------- Exame 2019 / 10 Jan -----------------------------------------
2-

def soma_digitos(n):
	if type(n) != int or n < 0:
		raise ValueError('O argumento deve ser inteiro positivo')
	x, num = 1, 0
	while x != 0:
		x = n % 10
		num += x
		n //= 10
	return num

print(soma_digitos(23.5))'''


'''3- 

def triangular(n):
	if n == 0 or n ==1: return False
	soma = 0
	x = 1
	while soma < n:
		soma += x
		x += 1
	if soma == n:
		return True
	return False

print(triangular(6))

def nesimo(n):
	cont = 0 
	num = 1
	while cont != n:
		if triangular(num):
			cont += 1
		num += 1
	return num - 1

print(nesimo(1))'''

'''
4-

def parte(lst, e):
	maior, menor = [], []
	for x in lst:
		if x < e:
			menor += [x,]
		else:
			maior += [x,]
	return [menor, maior]

print(parte([2, 0, 12, 19, 5], 6))'''

'''
5-

def conversor(frase):
	lst1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
	lst2 = ['n','o','p','q','r','s','t','u','v','w','x','y','z']
	new_sent = ''
	sentence = list(frase)
	for i in range(len(frase)):
		if sentence[i] in lst1:
			n = lst1.index(sentence[i])
			l = lst2[n]
			sentence[i] = l
		elif sentence[i] in lst2:
			n = lst2.index(sentence[i])
			l = lst1[n]
			sentence[i] = l
		else:
			sentence[i] = sentence[i]
	for a in sentence:
		new_sent += a
	return new_sent

print(conversor('Este exercicio nao e tao dificil como parece'))'''

'''
6-
a)
def soma_n_vezes(a,b,n):
	while n > 0:
		b += a
		n -= 1
	return b 

b)
def soma_n_vezes(a,b,n):
	if n == 0:
		return b 
	return a + soma_n_vezes(a,b,n-1)

print(soma_n_vezes(1,10,5))

c)
from functools import reduce

def soma(lst):
	return reduce(map(lst, quadrado), lambda x, y: x + y)

print(soma([1,2,3,4,5]))

9-

def multiplos_filtrados(n, pred):
	dic, keys = {}, []
	i = 1
	while i <= n:
		if pred(i): 
			keys.append(i)
		i += 1
	
	for x in keys:
		values = []
		for i in range(1, n + 1):
			values += [x * i,]
		dic[x] = values
	return dic

print(multiplos_filtrados(4, lambda x: x % 2 == 0))'''

'''
-------------------------------- Exame 2019 / 1 Fev -----------------------------------------

'''
'''
2- 

def apenas_pares(num):
	if type(num) != int or num < 0:
		raise ValueError('o argumento deve ser um inteiro > 0')
	count, newnum = 0, 0
	while num != 0:
		#digit = 0
		digit = num % 10
		if digit % 2 == 0:
			newnum += digit * 10 ** count
			count += 1
		num //= 10
	return newnum 

print(apenas_pares(3.2))'''

'''
3-

a)
def eh_abundante(num):
	divisores = []
	ndiv, soma = 0, 0
	for i in range(1, num):
		if num % i == 0:
			divisores += [i]
	for x in divisores:
		soma += x
	return soma > num

print(eh_abundante(12))

b)

def n_primeiros_abundantes(n):
	start = 12
	lst = []
	while len(lst) != n:
		if eh_abundante(start):
			lst += [start]
		start += 1
	return lst

print(n_primeiros_abundantes(5))'''

'''
8-
c)

def reconhece(cad):
	lst_cad = list(cad)
	mid = int(len(cad) / 2)
	if lst_cad[mid] != 'e':
		return False
	for x in range(mid):
		if not (ord(lst_cad[x]) + 1) == ord(lst_cad[- x - 1]):
			return False 
	for i in range(mid):
		if not ord(lst_cad[i]) in (ord('a'), ord('c')) and not ord(lst_cad[i]) <= ord(lst_cad[i+ 1]):
			return False
	return True

print(reconhece('acedb'))'''

'''
9- '''
def junta(d1, d2):
	d1_d2 = {}
	val = []
	for key in d1:
		if key in d2:
			val = d1[key] + d2[key]
			d1_d2[key] = val
		else:
			d1_d2[key] = d1[key]
	for key in d2:
		if not key in d1_d2:
			d1_d2[key] = d2[key]
	return d1_d2

d1 = {'g': [12, 1], 'z': [5], 'a':[98, 32]}
d2 = {'f':[3], 'g':[33, 44]}

print(junta(d1, d2))




'''
-------------------------------- Exame 2020 / 9 Jan -----------------------------------------
'''
'''
6- 

def reconhece(pred):
	letters = range(ord('A'), ord('D') + 1)
	nums = range(ord('1'), ord('4') + 1)

	def eh_extremo(pred):
		return ord(pred[0]) in letters and ord(pred[-1]) in letters and ord(pred[1]) in nums

	def eh_seq(pred):
		seq = 0
		if eh_extremo(pred):
			for i in range(1, len(pred)):
				if ord(pred[i]) in nums:
					if (i + 1) <= len(pred) and ord(pred[i + 1]) in letters:
						seq += 1
					else:
						seq += 0
			return seq < 2
		return False

	return eh_extremo(pred) and eh_seq(pred)

print(reconhece('A1ABC'))
'''
'''
8-

def conta_palavras(pred):
		
	def keys_maker(pred):
		word = ''
		lst_keys = []


		for n in range(len(pred)):

			if ord(pred[n]) != ord(' '):
				word += pred[n]

				if (n + 1) < (len(pred)) and (ord(pred[n + 1]) == ord(' ') or (n + 1) == len(pred)):
					lst_keys += [word]
					word = '' 


		lst_keys = pred.split()
		return lst_keys	

	def keys_counter(pred): 

		dict_keys = {}

		keys = keys_maker(pred)

		for key in keys:
			if not key in dict_keys:
				dict_keys[key] = keys.count(key)
			else:
				dict_keys = dict_keys

		return dict_keys

	return keys_counter(pred)

cc = 'a aranha arranha a ra a ra arranha a aranha nem a aranha arranha a ra nem a ra arranha a aranha'
print(conta_palavras(cc))
'''







