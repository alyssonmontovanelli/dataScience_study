import numpy as np

print("Geração Pseudoaleatória\n")

arraySimple = np.random.standard_normal(size = (4,4))
print(arraySimple)

rng = np.random.default_rng(seed = 12345)
print(type(rng))

data = rng.standard_normal((2,3))
print(data)