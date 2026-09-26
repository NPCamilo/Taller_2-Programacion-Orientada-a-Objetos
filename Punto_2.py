"""
Conteo de palabras en frases
- Diseñe una clase `Frase` con atributos: texto y autor.
- Crea una lista de frases (una lista de objetos, cada objeto va a ser una instancia de
la clase Frase).
- Implemente un método que cuente cuántas veces aparece una palabra clave en
todas las frases.
- Guarde los resultados en `frases.txt`.

"""

class Frase:
    def __init__(self, texto, autor):
        self.text = texto
        self.author = autor

    def count_word(self, palabra_clave):
        return self.text.lower().split().count(palabra_clave.lower())
    
    def save_to_file(self, palabra_clave, conteo):
        with open("frases.txt", "a") as file:
            file.write(f"Frase: {self.text}\n")
            file.write(f"Autor: {self.author}\n")
            file.write(f"La palabra '{palabra_clave}' aparece {conteo} veces.\n\n")
            
user_inputs = []
while True:
    user_phrase = input("Ingrese una frase (o 'salir' para terminar): ")
    if user_phrase.lower() == 'salir' or user_phrase.upper() == 'SALIR' or user_phrase.strip() == "" or user_phrase.strip() == " " or user_phrase.strip() == "\n":
        break
    user_author = input("Ingrese el autor de la frase: ")
    phrase = Frase(user_phrase, user_author)
    user_inputs.append(phrase) 


key_word = input("\nIngrese la palabra clave a buscar: \n")
print(f'\n Frase(s) ingresada(s): {len(user_inputs)}\n')
count = 0
for frase in user_inputs:
    print(f"Frase: {frase.text}")
    print(f"Autor: {frase.author}\n")
    count += frase.count_word(key_word)
    frase.save_to_file(key_word, count)

print(f"\nLa palabra '{key_word}' aparece {count} veces en las frases ingresadas.\n")
