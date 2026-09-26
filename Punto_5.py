"""
Clasificación de objetos electrónicos
- Crea una clase `Electrodomestico` con atributos: nombre, marca, consumo (en
watts).
- Implemente un método que clasifique los objetos como “bajo consumo” (<500W) o
“alto consumo” (>=500W).
- Guarda el inventario en `electrodomesticos.txt`.

"""

class Electrodomestico:
    def __init__(self, nombre, marca, consumo):
            self.nombre = nombre
            self.marca = marca
            self.consumo = consumo

    def clasify_consumption(self):
        if self.consumo < 500:
            return "bajo consumo"
        else:
            return "alto consumo"

    def save_to_file(self):
        with open("electrodomesticos.txt", "a") as file:
            file.write(f"{self.nombre},{self.marca},{self.consumo},{self.clasify_consumption()}\n")
            
user_inputs = []
while True:
    user_nombre = input("Ingrese el nombre del electrodoméstico (o '0' para terminar): ")
    if user_nombre == '0':
        break
    user_marca = input("Ingrese la marca del electrodoméstico: ")
    user_consumo = float(input("Ingrese el consumo en Watts del electrodoméstico: "))

    electrodomestico = Electrodomestico(user_nombre, user_marca, user_consumo)
    electrodomestico.save_to_file()
    user_inputs.append(electrodomestico)
    
print(f"\nSe han registrado {len(user_inputs)} electrodomésticos en 'electrodomesticos.txt'.\n")
print("\nClasificación de los electrodomésticos:\n")
for electrodomestico in user_inputs:
    print(f"Nombre: {electrodomestico.nombre}  |  Marca: {electrodomestico.marca}  |  Consumo: {electrodomestico.consumo}W  |  Clasificación: {electrodomestico.clasify_consumption()}\n")