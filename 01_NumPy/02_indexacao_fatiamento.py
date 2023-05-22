import numpy as np


arrayNp = np.arange(10)
print(arrayNp) 

# Fatiamentos simples

print(arrayNp[5])
print(arrayNp[:5])
print(arrayNp[5:])
print(arrayNp[1:9:2])
print(arrayNp[:])

# Quandoa tribui uma fatia a outro array, não copia os dados, apenas tira uma fatia do array original 
arrSlice = arrayNp[5:8]
print(arrSlice)
arrSlice[1] = 9999
print(arrSlice)
print(arrayNp)

'''Para copiar o array, precisa ser explicito'''

arrCopy = arrayNp[5:9].copy()
print(arrCopy)

''' ARAAY DE DIFERENTES DIMENSÕES '''

arr2d = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(arr2d)
print(arr2d[1])

arr3d = np.array([[[1,2,3], [4,5,6]],[[7,8,9], [10,11,12]]])
print(f"\nNúmero de dimensões {arr3d.ndim}")
print(arr3d)
print(arr3d.shape)
print(arr3d[0,1,2])

''' INDEXAÇÃO COM FATIAS '''

#fatiamento array bidimensional e tridimensonal

print(f"\n{arr2d[:2]}")
print(f"\n{arr2d[:2,0:]}")
print(f"\n{arr2d[1,:2]}")
print(f"\n{arr2d[:,:1]}")

'''Fazendo a tribuições com fatiamento'''
arr2d[:2,1:] = 0
print(arr2d)


''' Indesxação Boleana '''
print("\nIndexação Booleana\n")

names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
data = np.array([[4,7],[0,2], [-5,6], [0,0], [1,2], [-12,-4], [4,3]])
print(names)
print(data)

print(names == "Bob")
#Passando o array Booleano para o array data

print(data[names == "Bob"])

print(~(names == "Bob")) #Isso inverte um array booleano
print(data[~(names == "Bob")])

print("\nMáscara - mask")
mask1 = (names == "Bob") | (names == "Will")
print(mask1)
print(data[mask1])

data[data<0] = 0 
print(data)

data[names != "Joe"] = 8
print(data)




''' INDEXAÇÃO SOFISTICADA '''

arrayS = np.zeros((8,4))
print(arrayS)

for i in range(8):
    arrayS[i] = i

print(arrayS)

# Selecionando subconjuntos

print(arrayS[[4,6,0,3]])

array2 = np.arange(32).reshape((8,4))
print(array2)
print(array2.ndim)


'''Trasnposição de arrays'''

arrayT = np.arange(15).reshape(3,5)
print(f"\nTransposição de arrays e troca de eixos: \
      \n{arrayT}")

print(arrayT.T) #Transformando linhas em colunas e vice-versa


''' MULTIPLICAÇÃO DE MATRIZES '''

#Multiplicação interna: 
print("\nMultiplica matriz\n")
matriz1 = np.arange(18).reshape((3,6))
print(matriz1)
print(matriz1.T)
print(f"Resultado da múltiplicação interna da matriz1:\
      \n{np.dot(matriz1.T, matriz1)}")

matriz2 = np.array([[7,5,1,3,6,9], [89,47,12,63,63,6], [0,9,8,7,1,20]])

print(f"Resultado da múltiplica matriz1 * matriz2:\
      \n{np.dot(matriz1,matriz2.T)}")

print(matriz1 @ matriz2.T) #Utilizando operador in fixo
