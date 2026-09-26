"""
Agenda de eventos
- Crea una clase `Evento` con atributos: título, fecha, hora, lugar y responsable.
- Permita registrar varios eventos y guardarlos en `agenda.txt`.
- Implemente un método que lea el archivo y muestre solo los eventos programados
para la próxima semana.

"""

class Evento:
    def __init__(self, titulo, fecha, hora, lugar, responsable):
        self.titulo = titulo
        self.fecha = fecha
        self.hora = hora
        self.lugar = lugar
        self.responsable = responsable

    def save_to_file(self):
        with open("agenda.txt", "a") as file:
            file.write(f"{self.titulo},{self.fecha},{self.hora},{self.lugar},{self.responsable}\n")

    @staticmethod
    def show_next_week_events():
        from datetime import datetime, timedelta

        try:
            with open("agenda.txt", "r") as file:
                print("\nEventos programados para la próxima semana:\n")
                for line in file:
                    titulo, fecha, hora, lugar, responsable = line.strip().split(",")
                    evento_fecha = datetime.strptime(fecha, "%Y-%m-%d")
                    if datetime.now() <= evento_fecha <= datetime.now() + timedelta(days=7):
                        print(f"\nEvento: {titulo}\nFecha: {fecha}  |  Hora: {hora}  |  Lugar: {lugar}  |  Responsable: {responsable}\n")
        except FileNotFoundError:
            print("El archivo 'agenda.txt' no existe. No hay eventos registrados.")
            
user_inputs = []
while True:
    user_titulo = input("Ingrese el título del evento (o '0' para terminar): ")
    if user_titulo == '0':
        break
    user_fecha = input("Ingrese la fecha del evento (YYYY-MM-DD): ")
    user_hora = input("Ingrese la hora del evento (HH:MM): ")
    user_lugar = input("Ingrese el lugar del evento: ")
    user_responsable = input("Ingrese el responsable del evento: ")

    evento = Evento(user_titulo, user_fecha, user_hora, user_lugar, user_responsable)
    evento.save_to_file()
    user_inputs.append(evento)
    
print(f"\nSe han registrado {len(user_inputs)} eventos en 'agenda.txt'.\n")
print("\nMostrando eventos programados para la próxima semana:\n")
Evento.show_next_week_events()