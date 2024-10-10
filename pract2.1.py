import numpy as np

array_1d = np.array([1,2,3,4,5])
print("Array 1D: ",array_1d)

array_2d = np.array([[1,2,3],[4,5,6]])
print("Array 2D:\n",array_2d)

suma = array_1d + 10
print("Array 1D + 10: ",suma)

multiplicacion = array_1d * 2
print("Array 1D * 2: ", multiplicacion)

suma_arrays = array_1d + np.array([5,4,3,2,1])
print("Suma de arrays: ",suma_arrays)

raiz_cuadrada = np.sqrt(array_1d)
print("Raiz cuadrada del Array 1D: ",raiz_cuadrada)

