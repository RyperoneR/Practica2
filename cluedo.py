print ("¡Bienvenidos a una emocionante noche llena de misterio y suspense! Están a punto de sumergirse en el intrigante mundo del Cluedo, un juego de mesa clásico que desafiará sus habilidades deductivas y los transportará a una mansión llena de secretos y conspiraciones.")
print ("En este fascinante juego, se encuentran en la mansión de la familia Blackwood, una familia adinerada con un pasado turbio y oscuro. La noche ha caído, y la atmósfera está cargada de intriga. De repente, un grito rompe el silencio: el Sr. Blackwood, el patriarca de la familia, ha sido asesinado en circunstancias misteriosas.")
print ("Ahora, ustedes, los valientes detectives, deben descubrir quién es el culpable, con qué arma cometieron el crimen y en qué habitación se llevó a cabo el asesinato. La mansión está llena de personajes sospechosos, cada uno con sus propios motivos y secretos ocultos.")
print ("Prepárense para sumergirse en una noche llena de engaños, alianzas cambiantes y giros inesperados. En el Cluedo, cada movimiento cuenta, y cada pista puede ser crucial para resolver el misterio. ¡Buena suerte, detectives! La verdad espera ser descubierta, pero el reloj está en marcha y el asesino podría estar más cerca de lo que imaginan. ¡Que comience la investigación!")
import random

class CluedoGame:
    def __init__(self):
        self.sospechosos = ["Sr. Verde", "Profesor Plum", "Sra. Blanco", "Sr. Amarillo", "Sra. Escarlata", "Col. Mostaza"]
        self.lugares = {"Cocina": "En la cocina, encuentras un cuchillo ensangrentado.",
                        "Sala de Estar": "En la sala de estar, ves huellas de barro en la alfombra.",
                        "Comedor": "En el comedor, encuentras un veneno sospechoso.",
                        "Estudio": "En el estudio, ves un sobre con dinero.",
                        "Biblioteca": "En la biblioteca, encuentras un libro sobre envenenamiento.",
                        "Pasillo": "En el pasillo, ves una sombra que se mueve rápidamente.",
                        "Sala de Billar": "En la sala de billar, encuentras un objeto contundente.",
                        "Salón de Baile": "En el salón de baile, encuentras una joya perdida.",
                        "Invernadero": "En el invernadero, encuentras una cuerda extraña."}
        self.armas = ["Candelabro", "Llave Inglesa", "Cuerda", "Cuchillo", "Llave Inglesa", "Revólver"]

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
            print("\nTe encuentras en la entrada de la mansión. Hay varios lugares para investigar:")
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
