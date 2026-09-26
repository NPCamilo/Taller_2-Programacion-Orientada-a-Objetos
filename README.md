# Taller 2 · Programación Orientada a Objetos (Python)

> **Asignatura:** Programación IV · Universidad Tecnológica de Pereira
> **Tema:** Clases, objetos, atributos y métodos (persistencia en archivos de texto)

Ejercicios de práctica con **programación orientada a objetos en Python**: definición de clases, el método constructor `__init__`, atributos de instancia, métodos de instancia y **métodos estáticos** (`@staticmethod`). Cada punto construye una clase, registra objetos de esa clase y persiste la información en archivos `.txt` usando el modo `with open(...)`.

Este taller da el salto formal de los talleres anteriores: aquí los datos dejan de ser simples listas sueltas y pasan a ser **objetos con comportamiento propio**.

---

## 📋 Requisitos

- Python 3.10 o superior.
- No se requieren librerías externas. Solo se usa la biblioteca estándar (`datetime` en el punto 8).

---

## 🗂️ Estructura del proyecto

| Archivo      | Clase      | Descripción |
|--------------|------------|-------------|
| `Punto_1.py` | `Numero`   | Valida un entero de tres cifras, invierte sus dígitos y calcula la suma de estos. |
| `Punto_2.py` | `Frase`    | Cuenta cuántas veces aparece una palabra clave en varias frases y guarda los resultados. |
| `Punto_3.py` | `Cadena`   | Clasifica 15 cadenas según empiecen o no con vocal y las guarda ordenadas. |
| `Punto_4.py` | `Cliente`  | Registra clientes de 5 atributos y muestra solo los que tienen saldo negativo. |
| `Punto_5.py` | `Electrodomestico` | Clasifica electrodomésticos como “bajo consumo” (<500W) o “alto consumo” (≥500W). |
| `Punto_6.py` | `Animal`   | Registra animales y muestra los que superan la edad promedio. |
| `Punto_7.py` | `Producto` | Registra un inventario y calcula el valor total en stock por categoría. |
| `Punto_8.py` | `Evento`   | Registra eventos en una agenda y filtra los de la próxima semana. |

### Archivos generados en tiempo de ejecución

Estos archivos los crea cada programa al ejecutarse:

| Archivo                   | Generado por |
|---------------------------|--------------|
| `numeros.txt`             | `Punto_1.py` |
| `frases.txt`              | `Punto_2.py` |
| `cadenas.txt`             | `Punto_3.py` |
| `clientes.txt`            | `Punto_4.py` |
| `electrodomesticos.txt`   | `Punto_5.py` |
| `animales.txt`            | `Punto_6.py` |
| `almacen.txt`             | `Punto_7.py` |
| `agenda.txt`              | `Punto_8.py` |

> Los archivos que terminan con `0` (o que repiten ejecución) se sobrescriben con modo `"w"`. Los que registran varios elementos usan modo `"a"` (append), por lo que los datos se acumulan entre ejecuciones. **Bórralos si quieres empezar de cero.**

---

## 🚀 Cómo ejecutar

Cada punto es independiente y **todos son interactivos**. Ejecuta uno a la vez desde dentro de la carpeta del taller:

```bash
python Punto_1.py
python Punto_4.py
python Punto_8.py
```

En la mayoría de puntos se registra información en un bucle `while True` y se termina escribiendo `0` (en el punto 1 se escribe un número de tres cifras; en el punto 2 se escribe `salir`).

---

## 📝 Explicación de cada punto

### Punto 1 — Números y dígitos invertidos
La clase `Numero` recibe un entero de tres cifras. El constructor valida el rango (`100 <= numero <= 999`), `sum_of_digits()` recorre el número con `sum()` y `write_to_file()` invierte los dígitos usando `str()[::-1]` y los guarda en `numeros.txt`. Finalmente el programa **vuelve a leer el archivo** e imprime su contenido.

**Conceptos:** clase, `__init__`, validación, métodos de instancia, `open()` en modo escritura y lectura.

```python
class Numero:
    def __init__(self, numero):
        if 100 <= numero <= 999:
            self.numero = numero
        else:
            return ValueError("El número debe ser un entero de tres cifras.")

    def sum_of_digits(self):
        return sum(int(digit) for digit in str(self.numero))
```

### Punto 2 — Conteo de palabras en frases
La clase `Frase` guarda `text` y `author`. El programa crea una **lista de objetos** (varias instancias de `Frase`) y `count_word()` normaliza el texto con `.lower().split()` para buscar la palabra clave. Los resultados se anexan a `frases.txt`.

**Conceptos:** lista de instancias, `str.lower()`, `str.split()`, `list.count()`, modo append.

```python
class Frase:
    def count_word(self, palabra_clave):
        return self.text.lower().split().count(palabra_clave.lower())
```

### Punto 3 — Cadenas clasificadas por vocales
La clase `Cadena` tiene un atributo `text` y el método `starts_with_vowel()`, que compara el primer carácter contra `'aeiou'`. Se recolectan 15 cadenas y se separan en dos grupos (vocales y resto) usando **comprensión de listas**; el resultado se guarda en `cadenas.txt`.

**Conceptos:** índice `[0]`, operador `in`, comprensión de listas, concatenación de listas.

```python
vocales    = [c for c in user_inputs if c.starts_with_vowel()]
restantes  = [c for c in user_inputs if not c.starts_with_vowel()]
ordenadas  = vocales + restantes
```

### Punto 4 — Registro de clientes
La clase `Cliente` tiene 5 atributos (`id`, `nombre`, `edad`, `ciudad`, `saldo`). `save_to_file()` escribe una línea CSV por cliente en modo append, y el **método estático** `mostrar_clientes_negativos()` lee el archivo, descompone cada línea con `split(",")` y filtra los saldos negativos.

**Conceptos:** `@staticmethod`, lectura línea por línea, `split(",")`, conversión con `float()`, `try/except FileNotFoundError`.

```python
@staticmethod
def mostrar_clientes_negativos():
    with open("clientes.txt", "r") as file:
        for line in file:
            id, nombre, edad, ciudad, saldo = line.strip().split(",")
            if float(saldo) < 0:
                ...
```

### Punto 5 — Clasificación de electrodomésticos
La clase `Electrodomestico` recibe `nombre`, `marca` y `consumo` (en watts). El método `clasify_consumption()` aplica el umbral de 500W para devolver la categoría, y esa clasificación se escribe directamente en `electrodomesticos.txt` junto con los datos.

**Conceptos:** método que devuelve un valor, condicional `if/else`, `float()`, persistencia con datos derivados.

```python
def clasify_consumption(self):
    if self.consumo < 500:
        return "bajo consumo"
    else:
        return "alto consumo"
```

### Punto 6 — Animales y edades
La clase `Animal` guarda `especie`, `nombre` y `edad`. El método estático `show_animals_above_average()` reconstruye los objetos desde el archivo, calcula la edad promedio con `sum()` / `len()` y muestra únicamente los animales que la superan.

**Conceptos:** cálculo de promedio, comparación `>`, rehidratación de objetos desde un archivo.

```python
promedio_edad = sum(edades) / len(edades)
for especie, nombre, edad in animales:
    if edad > promedio_edad:
        ...
```

### Punto 7 — Inventario de almacén
La clase `Producto` tiene 5 atributos (`codigo`, `nombre`, `cantidad`, `precio`, `categoria`). El método estático `show_total_value_by_category()` usa un **diccionario** como acumulador para sumar `cantidad * precio` por cada categoría y mostrar el valor total del stock.

**Conceptos:** diccionarios como acumuladores, iteración con `.items()`, aritmética mixta (`int` × `float`), formato `:.2f`.

```python
categorias = {}
...
categorias[categoria] += valor_total
```

### Punto 8 — Agenda de eventos
La clase `Evento` guarda `titulo`, `fecha`, `hora`, `lugar` y `responsable`. La fecha se ingresa en formato `YYYY-MM-DD` y el método estático `show_next_week_events()` la convierte con `strptime()` para compararla contra `datetime.now()` y `timedelta(days=7)`, mostrando solo los eventos de la próxima semana.

**Conceptos:** módulo `datetime`, `strptime()`, `timedelta()`, comparación de rangos de fechas.

```python
evento_fecha = datetime.strptime(fecha, "%Y-%m-%d")
if datetime.now() <= evento_fecha <= datetime.now() + timedelta(days=7):
    ...
```

---

## 🧠 Conceptos repasados

- Clases y objetos: definición de `class`, creación de instancias, atributo de instancia (`self`).
- Método constructor `__init__` y validación de datos de entrada.
- Métodos de instancia vs. **métodos estáticos** (`@staticmethod`).
- Listas de objetos y recorrido con `for`.
- Persistencia: `open()` en modo escritura (`"w"`), append (`"a"`) y lectura (`"r"`), y el uso de `with` para cerrar los archivos.
- Formato de datos: escritura CSV manual y descomposición con `split(",")`.
- Manejo de errores: `try / except FileNotFoundError`.
- Diccionarios como acumuladores y comprensiones de listas.
- Módulo estándar `datetime` para trabajar con fechas.

---

## 📚 Fuentes oficiales

- [Programación orientada a objetos en Python](https://docs.python.org/3/tutorial/classes.html)
- [Definición de clases](https://docs.python.org/3/reference/compound_stmts.html#class-definitions)
- [Lectura y escritura de archivos (E/S de archivos)](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Módulo `datetime`](https://docs.python.org/3/library/datetime.html)
