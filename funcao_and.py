# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 20:35:16 2024

@author: lab52
"""

from linear_algebra import dot

def step_function(x):
    return 1 if x >= 1.5 else 0

def perceptrom_output(peso, bias, x):
    calculation = dot(peso, x) + bias
    return step_function(calculation)

x0 = [0,0]
x1 = [0,1]
x2 = [1,0]
x3 = [1,1]

peso = [1,1]
bias = 0

saida0 = perceptrom_output(peso, bias, x0)
saida1 = perceptrom_output(peso, bias, x1)
saida2 = perceptrom_output(peso, bias, x2)
saida3 = perceptrom_output(peso, bias, x3)


print("PERCEPTROM IMPLEMENTANDO FUNÇÃO BOLEANA AND")
print("0 AND 0 = ", saida0 )
print("0 AND 1 = ", saida1 )
print("1 AND 0 = ", saida2 )
print("1 AND 1 = ", saida3 )

