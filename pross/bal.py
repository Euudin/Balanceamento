from equacao.coeficiente import *
import re
from pross.processa import processaTermo
from metAlgebre.Algebre import solucao
import numpy as np


def componentes(eq):
# separa todos os elementos que compõem a equação
    compounds = re.findall('[^+=\s]+', eq)
    processed_components = [processaTermo(compound) for compound in compounds]
    return processed_components



def calculate_coefficients(eq):
    solution_matrix = solucao(eq)
    solution = np.linalg.solve(solution_matrix[0], solution_matrix[1])
  # solucao(eq)[0] - matriz dos coef
  # solucao(eq)[1] - termos independentes

    coefficients = [1] + [abs(coef) for coef in solution]

  # Multiplica cada coeficiente por um número inteiro
    factor = 1
    while True:
        if all(abs(factor * coef - round(factor * coef)) < 0.1 for coef in coefficients):
          # Se todos os números forem inteiros
            break
        factor += 1

  # Elementos da lista coefs2 * fator arredondado
    rounded_coefficients = [int(round(coef * factor)) for coef in coefficients]
    return rounded_coefficients



def Balance(eq):
    
    ''' -> Gera a equação devidamente balanceada
    :param eq: Recebe a equação química a ser balanceada
    :return: Retorna a equação devidamente balanceada'''

    components = componentes(eq)
    coefficients = calculate_coefficients(eq)

    balanced_reaction = ''

    ordem = 0

    while ordem < len(components):
      # Se o termo for o último não adiciona sinal
        if ordem == len(components)-1:
      # primero coeficiente da soluão + componente
          balanced_reaction += str(coefficients[ordem]) + ' ' + componentes(eq)[ordem] + ' '
          
        elif ordem == len(reagentes(eq))-1:
        # Adiciona um sinal de igual no último termo dos reagentes
          balanced_reaction += str(coefficients[ordem]) + ' ' + componentes(eq)[ordem] + ' = '
          
        else:
        # Adiciona um sinal de mais no final dos componentes
          balanced_reaction += str(coefficients[ordem]) + ' ' + componentes(eq)[ordem] + ' + ' 
          
        ordem += 1
        
    return balanced_reaction


