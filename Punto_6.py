"""
Animales y edades
- Crea una clase `Animal` con atributos: especie, nombre, edad.
- Genere una lista de animales.
- Implementa un método que calcule el promedio de edades.
- Guarda y lee el archivo `animales.txt` mostrando los animales que superan la edad
promedio.

"""

class Animal:
    def __init__(self, especie, nombre, edad):
        self.especie = especie
        self.nombre = nombre
        self.edad = edad

    def save_to_file(self):
        with open("animales.txt", "a") as file:
            file.write(f"{self.especie},{self.nombre},{self.edad}\n")

    @staticmethod
    def show_animals_above_average():
        try:
            with open("animales.txt", "r") as file:
                edades = []
                animales = []
                for line in file:
                    especie, nombre, edad = line.strip().split(",")
                    edades.append(int(edad))
                    animales.append((especie, nombre, int(edad)))
                
                if edades:
                    promedio_edad = sum(edades) / len(edades)
                    print(f"\nPromedio de edades: {promedio_edad:.2f}\n")
                    print("Animales que superan la edad promedio:\n")
                    for especie, nombre, edad in animales:
                        if edad > promedio_edad:
                            print(f"Especie: {especie}  |  Nombre: {nombre}  |  Edad: {edad}\n")
                else:
                    print("No hay animales registrados.")
        except FileNotFoundError:
            print("El archivo 'animales.txt' no existe. No hay animales registrados.")
            
user_inputs = []
while True:
    user_especie = input("Ingrese la especie del animal (o '0' para terminar): ")
    if user_especie == '0':
        break
    user_nombre = input("Ingrese el nombre del animal: ")
    user_edad = int(input("Ingrese la edad del animal: "))

    animal = Animal(user_especie, user_nombre, user_edad)
    animal.save_to_file()
    user_inputs.append(animal)
    
print(f"\nSe han registrado {len(user_inputs)} animales en 'animales.txt'.\n")
print("\nMostrando animales que superan la edad promedio:\n")
Animal.show_animals_above_average()