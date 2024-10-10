import pandas as pd

ventas_diarias = [200,150,300,250,400,500,450]
dias_semana = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']

serie_ventas = pd.Series(ventas_diarias, index=dias_semana)

print("Ventas diarias: ")
print(serie_ventas)

print("\nVentas del miercoles: ")
print(serie_ventas['Miercoles'])

total_ventas_semana = serie_ventas.sum()
print("\nTotal de ventas a la semana")
print(total_ventas_semana)

print("\nPromedio de ventas diario")
promedio_ventas = serie_ventas.mean()
print(round(promedio_ventas,2))



