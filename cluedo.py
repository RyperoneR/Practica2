print ("¡Bienvenidos a una emocionante noche llena de misterio y suspense! Están a punto de sumergirse en el intrigante mundo del Cluedo, un juego de mesa clásico que desafiará sus habilidades deductivas y los transportará a una mansión llena de secretos y conspiraciones.")
print ("En este fascinante juego, se encuentran en la mansión de la familia Blackwood, una familia adinerada con un pasado turbio y oscuro. La noche ha caído, y la atmósfera está cargada de intriga. De repente, un grito rompe el silencio: el Sr. Blackwood, el patriarca de la familia, ha sido asesinado en circunstancias misteriosas.")
print ("Ahora, ustedes, los valientes detectives, deben descubrir quién es el culpable, con qué arma cometieron el crimen y en qué habitación se llevó a cabo el asesinato. La mansión está llena de personajes sospechosos, cada uno con sus propios motivos y secretos ocultos.")
print ("Prepárense para sumergirse en una noche llena de engaños, alianzas cambiantes y giros inesperados. En el Cluedo, cada movimiento cuenta, y cada pista puede ser crucial para resolver el misterio. ¡Buena suerte, detectives! La verdad espera ser descubierta, pero el reloj está en marcha y el asesino podría estar más cerca de lo que imaginan. ¡Que comience la investigación!")

import random

class CluedoGame:
    def __init__(self):
        self.sospechosos = ["Rodrigo", "Raúl", "Ana", "Juanjo", "Manuel", "Nicola","David", "Fausto","Jose Antonio"]
        self.lugares = {"Azotea": "En la azotea te encuentras a Rodrigo fumando estresado.",
                        "Salida de emergencia": "Sales por la salida de emergencia y te encuentras a Raúl trapicheando con unos chavalines. Estos se asustan con tu presencia y se van.",
                        "Aula 404": "Llegas al aula 404, ela aula del grado en física. En ella está David explicandole a Victor la relación entre el grafeno las asíntotas.",
                        "Baños": "Entras en el baño y te encuentras con Ana con los ojos inyectados en sangre y con la nariz roja por haber llorado.",
                        "Recepción": "Cuando llegas a la recepción escuchas una buena bronca entre Nicola y el recepcionista. Parece que las pizarras que pidió Nicola para su clase aún no han llegado.",
                        "Cafetería": "Entras en la cafetería, allí esta comiendo sentado en una mesa Manuel. No habla, solo sonrríe.",
                        "Ascensor": "Estás esperando al ascensor, cuando finalmente llega este abre las puertas y de él sale José Antonio arrollandote.",
                        "Biblioteca": "Entras en la biblioteca. Todo esta vacío y en silencio. Al fondo está Fausto programando en su ordenador.",
                        "Cuarto de seguridad": "Llegas a la sala de seguridad. Allí esta Juanjo a oscuras echándose una partida de LOL en su portatil, a su lado una pantalla con todas las camaras de la universidad."}
        self.armas = ["HP Prime", "Lápiz", "Máquina Expendedora", "G36", "Impresora 3D", "Cable HDMI"]

        self.asesino = None
        self.lugar_asesinato = None
        self.arma_utilizada = None

        self.juego_activo = True
        self.iniciar_juego()

    def iniciar_juego(self):
        self.asesino = random.choice(self.sospechosos)
        self.lugar_asesinato = random.choice(list(self.lugares.keys()))
        self.arma_utilizada = random.choice(self.armas)

        print("¡Bienvenido a Cluedo! Has sido convocado para resolver un asesinato.")
        print("Hay un sospechoso, un lugar y un arma. ¡Adivina cuáles son!")

    def obtener_informacion_lugar(self, lugar):
        if lugar in self.lugares:
            print(self.lugares[lugar])
        else:
            print("Este lugar no es válido. Intenta otro lugar.")

    def realizar_acusacion(self, sospechoso, lugar, arma):
        if sospechoso == self.asesino and lugar == self.lugar_asesinato and arma == self.arma_utilizada:
            print("¡Felicidades! Has resuelto el caso. El asesino era {} en {} con un(a) {}.".format(self.asesino, self.lugar_asesinato, self.arma_utilizada))
            self.juego_activo = False
        else:
            print("Incorrecto. El asesino no era {} en {} con un(a) {}. Inténtalo de nuevo.".format(sospechoso, lugar, arma))

    def explorar_lugares(self):
        while self.juego_activo:
            print("\nTe encuentras en la entrada del campus de la universidad Alfonso X el sabio de Arapiles. Hay varios lugares para investigar:")
            print(list(self.lugares.keys()))

            lugar_elegido = input("\nElige un lugar para investigar (o escribe 'salir' para terminar): ").capitalize()

            if lugar_elegido == 'Salir':
                print("Gracias por jugar. ¡Hasta la próxima!")
                self.juego_activo = False
            elif lugar_elegido in self.lugares:
                self.obtener_informacion_lugar(lugar_elegido)
            else:
                print("Lugar no válido. Intenta de nuevo.")

# Ejemplo de uso
juego = CluedoGame()
juego.explorar_lugares()
