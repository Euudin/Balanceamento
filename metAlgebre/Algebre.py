import numpy as np
from equacao.coeficiente import coeficienteNumericos

def ajuste(eq):
	matriz = coeficienteNumericos(eq)
	linhas = len(matriz)
	colunas = len(matriz[0])
	
	if colunas == (linhas+1):
	# Condição onde não é necessario processar a matriz
		matriz2 = matriz

	else:
		num = colunas -1
		
		if linhas > num: 
			matriz2 = list()
			cont = 0
			
			while cont < num:
			# Adiciona a quantidade de linhas equivalente a num 
				matriz2.append(matriz[cont])
				cont += 1
	return matriz2


def solucao(eq):
# Transforma em matriz quadrada
	matriz = ajuste(eq)
	A = list() # Matriz dos coeficientes
	X = list() # Matriz dos termos independentes
	
	for i in matriz: # Cada Linha na matriz
		A2 = list()
		cont = 0 
		
		for j in i: # Cada elemento na linha
			if cont == 0:
			# se j for o primeiro elemento do i
				X.append(-j) # Remove e adiciona em X com sinal trocado
				
			else:
			# j não é o primeiro
				A2.append(j) # Adiciona nos coeficientes A2
			cont += 1
		A.append(A2)

	return A,X

	