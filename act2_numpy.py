import numpy as np

matrix = np.random.rand(3,3)
print("Matriz:\n", matrix)

max_val = np.max(matrix)
min_val = np.min(matrix)

print("Valor maximo: ", round(max_val,2))
print("Valor minimo: ", round(min_val,2))


mean_val = np.mean(matrix)
print("Media de los elementos: ", round(mean_val,2))
