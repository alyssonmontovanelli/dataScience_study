import numpy as np

rng = np.random.default_rng(seed = 12345)


arr1 = np.arange(10)
print(arr1)

print(np.sqrt(arr1)) #raiz quadrada - unfunc unaria
print(np.exp(arr1)) #raiz quadrada - unfunc unaria

print("\nFunções binárias - 2 arrays\n")

x = rng.standard_normal(8)
y = rng.standard_normal(8)

print(x,y)
print(np.maximum(x,y)) #valor máximmo

''' Retornando partes inteiras e fracionárias de arrays '''

arrayTeste = np.array([4.236, 8.987, 10.296, 4.963, 5.147, 6.471, 7.299])

fracionado, inteiro = np.modf(arrayTeste)

print(fracionado)
print(inteiro)
print(np.rint(arrayTeste)) # Valor inteiro mais próximo




