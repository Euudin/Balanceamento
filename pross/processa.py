import re

def processaTermo(eq):
# Retira os parenteses da Equação Química
	if '(' in eq:
		# Tudo que não for: parentes, espaços em branco e sinal de mais
		compostostEntreParenteses = re.findall('[^\(\\)+\s]+\([A-Za-z\\d]+\)\d{1,2}',eq)
		processados = list()

		for i in compostostEntreParenteses:
			começo = i.find('(')
			fim = i.find(')')
			# Número que vem depois dos parenteses
			fator = i[fim+1:]
			
			# Termo antes dos parenteses
			anterior = i[:começo]
			composto = i[começo+1:fim] # Item dentro dos parenteses
			elementos = re.findall('[A-z][a-z]?\d{0,2}',composto)
			compostoNovo = anterior

			for i in elementos:

			# Ultimo caracter não for um número
				if i[-1].isnumeric() == False:
					compostoNovo += i + fator

				else:
				# Retorna lista com um elemento
					numero = re.findall('\d{1,2}',i)[0]
					elemento = re.findall('[A-Z][a-z]?',i)[0]
					compostoNovo += elemento + str(int(numero)*int(fator))
			processados.append(compostoNovo)

		sub = [eq]

		cont = 0
		
		while cont < len(processados):
			# Subistitui os compostos entre parenteses pelos processados
			substituto = sub[-1].replace(compostostEntreParenteses[cont],processados[cont])

			sub.append(substituto)
			cont += 1
		return sub[-1]
		
	else:
		return eq
		
		