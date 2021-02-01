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
9- 
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

print(junta(d1, d2)) '''

'''
10-

class fila_2_p:

	def __init__(self):
		self.normal = []
		self.urgente = []

	def inicio(self):
		if self.normal == [] and self.urgente == []:
			raise ValueError('inicio : listas vazias')
		elif self.urgente != []:
			return self.urgente[0]
		else:
			return self.normal[0]

	def comprimento(self, tipo):
		if tipo == 'normal':
			return len(self.normal)
		elif tipo == 'urgente':
			return len(self.urgente)
		else:
			raise ValueError('comprimento: tipo invalido')

	def coloca(self, tipo, elem):
		if tipo == 'normal':
			self.normal += [elem]
		elif tipo == 'urgente':
			self.urgente += [elem]
		else:
			raise ValueError('coloca: tipo invalido')

	def retira(self):
		if self.urgente != []:
			del(self.urgente[0])
			return self
		elif self.normal != []:
			del(self.normal[0])
			return self
		else:
			raise ValueError('retira: listas vazias')

	def aumenta_prioridade(self):
		if self.normal == []:
			return self
		else:
			priority = self.normal[0]
			del(self.normal[0])
			self.urgente += [priority]
			return self

	def fila_vazia(self, tipo):
		if tipo == 'normal':
			return self.normal == []
		elif tipo == 'urgente':
			return self.urgente == []
		else:
			raise ValueError('fila_vazia: tipo invalido')

	def fila_para_listas(self):
		return (self.urgente, self.normal)

	def filas_iguais(self, other):
		fo = other.fila_para_listas
		return self.urgente == fo[0] and self.normal == fo[1]

	def __repr__(self):
		def rep_fila(f):
			r = '<'
			for elem in f:
				r += str(elem) + ','
			r += '>'
			return r
		return 'urgente :' + rep_fila(self.urgente) + ';' + 'normal :' + rep_fila(self.normal) '''

'''
-------------------------------- Exame 2018 / 31 Jan -----------------------------------------
'''

'''
2-

def inverte(num):
	res, dig = 0, 0
	while num != 0:
		dig = num % 10
		res = res * 10 + dig
		num //= 10
	return res 

print(inverte(12345))'''

'''
3-
def remove_repetidos(lst):
	newlst = []
	for l in lst:
		if l not in newlst:
			newlst += [l]
	return newlst

print(remove_repetidos([2,4,3,2,2,2,3]))'''

'''
4- 
def num_occ_lista(lst, num):
	if lst == []:
		return 0
	elif type(lst[0]) == list:
		return num_occ_lista(lst[0], num) + num_occ_lista(lst[1:], num)
	elif lst[0] == num:
		return 1 + num_occ_lista(lst[1:], num)
	else:
		return num_occ_lista(lst[1:], num)

print(num_occ_lista([1, [[[1]], 2], [[[2]]], 2], 2))'''

'''
5-

a)
def soma_fn_il(n, fn):
	soma = 0
	for x in range(1, n + 1):
		soma += fn(x)
	return soma

def soma_fn_ropa(n, fn):
	if n == 0:
		return 0 # a funcao conta entre 1 e n 
	else:
		return fn(n) + soma_fn(n - 1, fn)

def soma_fn_rc(n, fn):
	def soma_fn_aux(n, res):
		if n == 0:
			return res
		else:
			return soma_fn_aux(n - 1, fn(n) + res)
	return soma_fn_aux(n, 0)


print(soma_fn(4, lambda x: x * x))'''

'''
6-
def conta_pares(lst):
	return len(filter(lambda x: x % 2== 0, lst))

print(conta_pares([1, 2, 3, 4, 5, 6]))'''

'''
7-
def reconhece(cad):
	simb = ['+', '-', '*', '/']
	nums = ['0','1','2','3','4','5','6','7','8','9']
	count_si, count_sp = 0, 0


	if cad[0] != '(' or cad[-1] != ')':
		return False
	for s in range(1, len(cad) - 1):
		if cad[s] in (simb + nums) or cad[s] == ' ':
			if cad[s] in simb:
				count_si += 1
			elif cad[s] == ' ':
				count_sp += 1
		else:
			return False

	return count_si == 1 and count_sp == 2

print(reconhece('(24 * 00006)'))'''

'''
9-
def cria_produto(nome, preco):
	if type(nome) != str or preco <= 0 or type(preco) != float:
		raise ValueError('cria_produto: dados invalidos')
	return {'nome': nome, 'valor': preco}

def nome(produto):
	return produto['nome']

def preco(produto):
	return produto['valor']

def eh_produto(arg):
	return type(arg) == dict and len(arg) == 2 and type(arg['nome']) == str \
	and type(arg['valor']) == float and arg['valor'] > 0 and 'nome' in arg and \
	'valor' in arg

def produtos_iguais(p1, p2):
	return p1['nome'] == p2['nome'] and p1['valor'] == p2['valor']

def mais_caro(p1, p2):
	return p1['valor'] > p2['valor']

def preco_produtos(lst):
	tot = 0
	for prod in lst:
		tot += preco(prod[0]) * prod[1]
	return tot'''

'''
10-
def resumo_fp(notas_d):
	n_pos, n_neg, tot_notas_p, len_notas = 0, 0, 1, 0

	for nota in notas_d:
		len_notas = len(notas_d[nota])
		if nota < 10:
			n_neg += len_notas
		else:
			n_pos += len_notas
			tot_notas_p += (nota * len_notas)

	return (tot_notas_p / n_pos, n_neg)

notas_d = {1 : [96592, 99212, 90300, 99312], 15 : [92592, 99212], 20 : [98323]}
print(resumo_fp(notas_d)) '''

'''
-------------------------------- Exame 2018 / 18 Jan ----------------------------------------
'''
'''
2-
def h_m_s(num):
	h = int(num // 3600)
	num -= 3600 * h
	m = int(num // 60)
	num -= 60 * m
	return (h, m, num) 

print(h_m_s(62))'''

'''
3-
def codifica(num):
	cod, i = 0, 0
	while num != 0:
		dig = num % 10
		if dig % 2 == 0:
			cod += ((dig + 2) % 10) * 10 ** i
		else:
			cod += ((dig - 2) % 10) * 10 ** i
		num //= 10
		i += 1
	return cod

print(codifica(181))'''









'''
-------------------------------- Exame 2020 / 9 Jan -----------------------------------------
'''
'''
5-

def junta_ordenados(t1, t2):

	def inversor(t):
		t_inv = ()
		for n in range(len(t) - 1, -1, -1):
			t_inv += (t[n],)
		return t_inv

	t2_cres = inversor(t2) #ordem crescente

	i1, i2 = 0, 0
	junta = ()
	
	while i1 < len(t1) and i2 < len(t2_cres):
		if t1[i1] < t2_cres[i2]:
			junta += (t1[i1],)
			i1 += 1
		elif t2_cres[i2] < t1[i1]:
			junta += (t2_cres[i2],)
			i2 += 1
		else:
			junta += (t1[i1],)
			i1 += 1
			i2 += 2

	if i1 == len(t1) and i2 != len(t2_cres):
		while i2 < len(t2_cres):
			junta += (t2_cres[i2],)
			i2 += 1
	elif i2 == len(t2) and i1 != len(t1_cres):
		while i1 < len(t1):
			junta += (t1[i1],)
			i1 += 1
	else:
		return junta

	return junta

print(junta_ordenados((5, 6, 23, 45), (90, 67, 56, 34, 24, 6, 1)))'''
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
'''
9-
def val_serie(x):
	total, termo, i_termo = 0, 1, 0
	while termo >= 0.001:
		total += termo
		i_termo += 1
		termo  *= (x / i_termo)'''

'''
-------------------------------- Random Tasks -----------------------------------------
'''
'''
def parte(lst, num):
	def parte_aux(lst, lst_1, lst_2, num):
		if len(lst) == 0:
			return lst_1, lst_2
		elif lst[0] < num:
			return parte_aux(lst[1:], lst_1 + [lst[0]], lst_2, num)
		else:
			return parte_aux(lst[1:], lst_1, lst_2 + [lst[0]], num) 
	return list(parte_aux(lst, [], [], num))

print(parte([3,5,1,4,5,8,9], 4))'''