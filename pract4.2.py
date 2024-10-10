import pandas as pd
df_productos = pd.read_csv('ventasDataf.csv')

print("Datos de productos")
print(df_productos)

print("\nColumna de precios: ")
print(df_productos['Precio'])

df_productos['Valor total'] = df_productos['Precio'] * df_productos['Stock']
print("\nDataFrame con columna de valor total")
print(df_productos)

productos_stock_alto = df_productos[df_productos['Stock']>100]
print("\nProductos con stock mayor a 100: ")
print(productos_stock_alto)




