"""
Registro de clientes
- Crea una clase `Cliente` con al menos 5 atributos (id, nombre, edad, ciudad, saldo).
- Implemente un método que guarde los clientes en `clientes.txt`.
- Otro método que lea el archivo y muestre solo los clientes con saldo negativo.

"""

class Cliente:
    def __init__(self, id, nombre, edad, ciudad, saldo):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
        self.saldo = saldo

    def save_to_file(self):
        with open("clientes.txt", "a") as file:
            file.write(f"{self.id},{self.nombre},{self.edad},{self.ciudad},{self.saldo}\n")

    @staticmethod
    def mostrar_clientes_negativos():
        try:
            with open("clientes.txt", "r") as file:
                print("\nClientes con saldo negativo:\n")
                for line in file:
                    id, nombre, edad, ciudad, saldo = line.strip().split(",")
                    if float(saldo) < 0:
                        print(f"\nEl siguiente cliente tiene saldo negativo:\n")
                        print(f"\tID: {id}  |  Nombre: {nombre}  | Edad: {edad}  |  Ciudad: {ciudad}  |  Saldo: {saldo}\n")
        except FileNotFoundError:
            print("El archivo 'clientes.txt' no existe. No hay clientes registrados.")
            
user_inputs = []
while True:
    user_id = input("Ingrese el ID del cliente (o '0' para terminar): ")
    if user_id == '0':
        break
    user_nombre = input("Ingrese el nombre del cliente: ")
    user_edad = input("Ingrese la edad del cliente: ")
    user_ciudad = input("Ingrese la ciudad del cliente: ")
    user_saldo = input("Ingrese el saldo del cliente: ")

    cliente = Cliente(user_id, user_nombre, user_edad, user_ciudad, user_saldo)
    cliente.save_to_file()
    user_inputs.append(cliente)
    
print(f"\nSe han registrado {len(user_inputs)} clientes en 'clientes.txt'.\n")
print("\nMostrando clientes con saldo negativo:\n")
Cliente.mostrar_clientes_negativos()
