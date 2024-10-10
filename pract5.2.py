import pandas as pdy

df_ventas = pdy.read_csv('ventasAnalisis.csv')

df_ventas['Ingreso Total'] = df_ventas['Cantidad Vendida'] * df_ventas['Precio Unitario']

print("Datos de ventas: ")
print(df_ventas)

ingreso_por_producto= df_ventas.groupby('Producto')['Ingreso Total'].sum()
print("\nIngreso total por producto: ")
print(ingreso_por_producto)

ingreo_por_dia = df_ventas.groupby('Fecha')['Ingreso Total'].sum()
print("\nIngreso total por dia: ")
print(ingreo_por_dia)

producto_mas_vendido = df_ventas.groupby('Producto')['Cantidad Vendida'].sum().idxmax()
print("\nProducto mas vendido en términos de cantidad: ")
print(producto_mas_vendido)
