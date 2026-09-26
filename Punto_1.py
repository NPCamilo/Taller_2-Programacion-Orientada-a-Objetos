"""
Números y dígitos invertidos
- Crear una clase `Numero` donde pueda tener un entero de tres cifras.
- Implemente un método que devuelva la suma de sus dígitos.
- Implemente otro método que escriba en `numeros.txt` el número original y su versión
invertida.
- Leer el archivo e imprimir los resultados.

"""

class Numero:
    def __init__(self, numero):
        if 100 <= numero <= 999:
            self.numero = numero
        else:
            return ValueError("El número debe ser un entero de tres cifras.")

    def write_to_file(self):
        inverted_number = int(str(self.numero)[::-1])
        with open("numeros.txt", "w") as file:
            file.write(f"Número original: {self.numero}\n")
            file.write(f"Número invertido: {inverted_number}\n")
    
    def sum_of_digits(self):
        return sum(int(digit) for digit in str(self.numero))
        
user_input = int(input("Ingrese un número de tres cifras: "))
Pivot = False
while Pivot == False:
    if user_input < 100 or user_input > 999:
        print("Error: El número debe ser un entero de tres cifras.")
        user_input = int(input("Vuela a ingresar un número de tres cifras: "))
    else:
        Pivot = True

numero = Numero(user_input)
numero.write_to_file()
print(f"La suma de los dígitos es: {numero.sum_of_digits()}\n")
    
with open("numeros.txt", "r") as file:
    content = file.read()
    print("Contenido del archivo numeros.txt:\n")
    print(f'{content}\n')