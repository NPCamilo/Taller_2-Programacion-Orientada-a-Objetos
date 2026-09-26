"""
Inventario de almacén
- Crea una clase `Producto` con atributos: código, nombre, cantidad, precio y
categoría.
- Implemente un método que permita guardar el inventario en `almacen.txt`.
- Otro método que lea el archivo y muestre el valor total en stock de cada categoría.

"""

class Producto:
    def __init__(self, codigo, nombre, cantidad, precio, categoria):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.categoria = categoria

    def save_to_file(self):
        with open("almacen.txt", "a") as file:
            file.write(f"{self.codigo},{self.nombre},{self.cantidad},{self.precio},{self.categoria}\n")

    @staticmethod
    def show_total_value_by_category():
        try:
            with open("almacen.txt", "r") as file:
                categorias = {}
                for line in file:
                    codigo, nombre, cantidad, precio, categoria = line.strip().split(",")
                    valor_total = int(cantidad) * float(precio)
                    if categoria in categorias:
                        categorias[categoria] += valor_total
                    else:
                        categorias[categoria] = valor_total
                
                print("\nValor total en stock por categoría:\n")
                for categoria, valor_total in categorias.items():
                    print(f"Categoría: {categoria}  |  Valor total en stock: ${valor_total:.2f}\n")
        except FileNotFoundError:
            print("El archivo 'almacen.txt' no existe. No hay productos registrados.")
            
user_inputs = []
while True:
    user_codigo = input("Ingrese el código del producto (o '0' para terminar): ")
    if user_codigo == '0':
        break
    user_nombre = input("Ingrese el nombre del producto: ")
    user_cantidad = int(input("Ingrese la cantidad en stock del producto: "))
    user_precio = float(input("Ingrese el precio del producto: "))
    user_categoria = input("Ingrese la categoría del producto: ")

    producto = Producto(user_codigo, user_nombre, user_cantidad, user_precio, user_categoria)
    producto.save_to_file()
    user_inputs.append(producto)
    
print(f"\nSe han registrado {len(user_inputs)} productos en 'almacen.txt'.\n")
print("\nMostrando valor total en stock por categoría:\n")
Producto.show_total_value_by_category()