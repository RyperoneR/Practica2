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
