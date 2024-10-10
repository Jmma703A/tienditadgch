import pandas as pdy

data = {
    'Producto':['Manzanas', 'Naranjas', 'Platanos', 'Peras','Manzanas', 'Naranjas', 'Platanos', 'Peras'],
    'Fecha':['2024-05-01','2024-05-01','2024-05-01','2024-05-01','2024-05-02','2024-05-02','2024-05-02','2024-05-02'],
    'Cantidad vendida':[30, 45, 50, 20, 25, 40, 55, 30],
    'Precio Unitario ':[1.2, 0.8, 1.0, 1.5, 1.2, 0.8, 1.0, 1.5]
}
df_ventas = pdy.DataFrame(data)

df_ventas['Ingreso Total'] = df_ventas['Cantidad vendida'] * df_ventas['Precio Unitario ']
print("Datos de ventas: ")
print(df_ventas)

ingreso_por_producto= df_ventas.groupby('Producto')['Ingreso Total'].sum()
print("\nIngreso total por producto: ")
print(ingreso_por_producto)

ingreso_por_dia = df_ventas.groupby('Fecha')['Ingreso Total'].sum()
print("\nIngreso total por día: ")
print(ingreso_por_dia)

producto_mas_vendido = df_ventas.groupby('Producto')['Cantidad vendida'].sum().idxmax()
print("\nProducto mas vendido en terminos de cantidad: ")
print(producto_mas_vendido)
