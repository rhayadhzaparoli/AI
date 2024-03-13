# -*- coding: utf-8 -*-

"""from collection import counter
from functools import partial
import matplotlib
import matplotlib.pyplot as """
from linear_algebra import dot


def degrau(x):
    return 1 if x >= 0 else 0

def saida_perceptrom(pesos, entradas):
    y = dot(pesos, entradas)
    return degrau(y)

def ajustes(sinapses, entradas, saida):
    
    taxa_aprendizagem = 0.1
    
    saida_parcial = saida_perceptrom(sinapses, entradas)
    
    for j in range(3):
        sinapses[j] = sinapses[j] + taxa_aprendizagem * (saida[0] - saida_parcial) * entradas[j]
        
    saida = saida_parcial
    return sinapses, saida


neuronio = [0.5441, -0.5562, 0.4074] 
entrada2 = [-1, 2, 2]
entrada4 = [-1, 4, 4]
saida2 = [1]
saida4 = [0]

for _ in range(23):
    neuronio, saida_2 = ajustes(neuronio, entrada2, saida2)
    print (neuronio, "saida2 = ", saida_2)
    neuronio, saida_4 = ajustes(neuronio, entrada4, saida4)
    print (neuronio, "saida4 = ", saida_4)
    