import numpy as np

"""CRIAÇÃO DE NDARRAYS"""

arrayTeste = np.array([1,2,3,4,5,6])
print(arrayTeste)


data = np.array([[1.5, -0.1, 3], [0, -3, 6.5]])
print(data)

# Operações matemáticas em "data"

print(f"\nOperações com array {data * 10}")
print(f"\nOperações com array {data + data}")
print(data.shape)
print(data.dtype)

# Conversão de dados
data1 = [20, 30, 40, 50, 60, 70]
print(type(data1))

arr1 = np.array(data1)
print(type(arr1))

data2 = [[2,3,4], [5,6,7]]
arr2 = np.array(data2)
print(arr2)
print(f"\nDimensões: {arr2.ndim}")
print(f"\nShape: {arr2.shape}")

arrayZero = np.zeros(5)
arrayZero2 = np.zeros((3, 5))

print(arrayZero)
print(arrayZero2)

#

# Mudando tipo de arry 

arrInt = np.array([1,2,3,4,5,6,7,8,9,10])

arrFloat = arrInt.astype(np.float64)

print(f"\n array com o tipo modificado {arrFloat}")







