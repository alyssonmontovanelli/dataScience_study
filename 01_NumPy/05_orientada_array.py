import numpy as np
rng = np.random.default_rng(seed = 12345)


''' EXPRESSÃO LÓGICA CONDICIONAL COM ARRAYS '''

x = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
y = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
condicional = np.array([False, True, True, False, False])

result = np.where(condicional, x, y) #Where coloca 1 array como condicional para os outros arrays

print(result)


arr = rng.standard_normal((4,4))*10
print(arr)

result2 = np.where(arr>0, 2, -2) 
print(result2)

result3 = np.where(arr>0, 2, arr)
print(f"Substituindo apenas os pares por 2: \
      \n{result3}")



'''MÉTODOS MATEMÁTICOS E ESTATÍSTICOS'''

arr2 = np.rint(rng.random((5,4))*100)
print(f"\nMétodos matemáticos e estatísticos\
      \n {arr2}")

print(arr2.mean()) #média
print(np.mean(arr2)) 
print(arr2.sum()) #soma

print(arr.mean(axis=0)) #Média entre as colunas
print(arr.sum(axis=1)) #Média entre as colunas

''' UNICIDADE DE CONJUNTOS '''

names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
print(np.unique(names))