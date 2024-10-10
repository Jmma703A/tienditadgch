import csv

datos = [
    ["Leche", 5 , 28],
    ["Azucar", 15 , 32],
    ["Arroz", 23 , 30],
    ["Queso", 14 , 140],
    ["Jamon", 20 , 50]
]
with open('productos.csv', 'w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["productos","cantidades","precios"])
    writer.writerows(datos)
    
print('Archivo creado...')

