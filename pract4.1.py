import pandas as pd
productos = ['Manzanas','Naranjas','Platanos','Peras']
precios = [1.2, 0.8,1.0,1.5]
stock = [100, 150,200,80]

df_productos = pd.DataFrame({
    'Producto': productos,
    'Precio': precios,
    'Stock': stock
})
print("Datos de productos: ")
print(df_productos)

print("\nColumna de precios: ")
print(df_productos['Precio'])

df_productos['Valor total'] = df_productos['Precio'] * df_productos['Stock']
print("\nDataFrame con columna de valor total: ")
print(df_productos)

productos_stock_alto = df_productos[df_productos['Stock']>100]
print("\nProductos con stock mayor a 100: ")
print(productos_stock_alto)

