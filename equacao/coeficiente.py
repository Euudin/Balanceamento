import re
from pross.processa import processaTermo


def reagentes(eq):
	''' -> Separa os reagentes da equação
	:param eq: Recebe a equação
	:return: Retorna os reagentes da equação'''
	limite = eq.find('=') #Será descartado tudo apos o '='
	r = eq[:limite] 
	reagentes = re.findall('[^\s+=]+',r) #Extrai todosos reagentes
	reagentesProcessados = list()
	
	for i in reagentes:
		reagentesProcessados.append(processaTermo(i))
		
	return reagentesProcessados

	
	
def produtos(eq):
	''' -> Separa os produtos da equação
	:param eq: Recebe a equação
	:return: Retorna os produtos da equação'''	
	limite = eq.find('=')
	p = eq[limite:]
	produtos = re.findall('[^\s+=]+',p)
	produtosProcessados = list()
	
	for i in produtos:
		produtosProcessados.append(processaTermo(i))
		
	return produtosProcessados
	


def elementos(eq):
	''' -> separa os elementos da equação
	:param eq: Recebe a equação
	:return: retorna todos os elementos da equação'''
	atomos = re.findall('[A-Z][a-z]*',eq)
	return tuple(set(atomos))

	
	
def coeficienteAtomo(atomo,comp):
	'''-> Extrai a idade de átomos em um determinado componente

	:param atomo: Recebe um átomo de entrada
	:param comp: Recebe a componente
	:return: Retorna a quantidade de átomos no componente'''

	#Atomos pre processados
	atomos1 = re.findall(atomo+'[a-z]?\d{0,2}',comp)
	quantidade = 0
	
	for i in atomos1:
		literal = re.findall('[A-Z][a-z]?',i)[0]
		
		if literal == atomo:
			numero = re.findall('\d{1,2}',i)
			
			if len(numero) == 0:
				quantidade += 1
				
			else:
				quantidade += int(numero[0])
				
	return quantidade



def coeficientesAtomos(eq):
	''' -> coeficiente atomico de cada átomo
	:param eq: Recebe a equação
	:return: Uma lista com os coeficientes atomicos dos átomos'''
	coeficienteAtomos = list()
	for elemento in elementos(eq):
		coeficientes = [elemento]
		
		for i in reagentes(eq):
			# verifica quantas vezes o elemnto aparece na componente i
			coeficientes.append(coeficienteAtomo(elemento,i))
			
		for j in produtos(eq):
			coeficientes.append(-1*coeficienteAtomo(elemento,j))
			
		coeficienteAtomos.append(coeficientes)
	return coeficienteAtomos
	
	

def coeficienteNumericos(eq):
	'''-> Extrai apenas os coeficientes númerico
	:param eq: Recebe a equação
	:return: Coloca os coeficientes em arrays
	'''
	coeficientes = list()
	for i in coeficientesAtomos(eq):
		numeros = list()
		
		for j in i:
			if i.index(j) != 0:
				numeros.append(j)
		coeficientes.append(numeros)
	return coeficientes



