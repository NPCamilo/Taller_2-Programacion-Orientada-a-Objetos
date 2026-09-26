"""
Cadenas clasificadas por vocales
- Crea una clase `Cadena` con un atributo texto.
- Genere una lista de 15 cadenas.
- Implemente un método que ordene primero las cadenas que empiezan con vocal y
luego las demás.
- Guarde la lista ordenada en `cadenas.txt`.

"""

class Cadena:
    def __init__(self, texto):
        self.text = texto
    
    def starts_with_vowel(self):
        return self.text[0].lower() in 'aeiou'
    
    def save_to_file(self, file):
        file.write(f"{self.text}\n")   
        
user_inputs = []
while len(user_inputs) < 15:
    user_input = input("Ingrese una cadena (o '0' para terminar): ")
    if user_input == '0':
        break
    cadena = Cadena(user_input)
    user_inputs.append(cadena)

# Ordenar las cadenas
vocales = [cadena for cadena in user_inputs if cadena.starts_with_vowel()]
restantes = [cadena for cadena in user_inputs if not cadena.starts_with_vowel()]
cadenas_ordenadas = vocales + restantes

print(f"\nCadenas ingresadas: {len(user_inputs)}\n")
print(f"\nCadenas ordenadas: \n")
for cadena in cadenas_ordenadas:
    print(f"- {cadena.text}")

# Guardar en archivo
with open("cadenas.txt", "w") as file:
    for cadena in cadenas_ordenadas:
        cadena.save_to_file(file)

print(f"\nSe han guardado {len(cadenas_ordenadas)} cadenas en 'cadenas.txt' ordenadas por vocales.\n")