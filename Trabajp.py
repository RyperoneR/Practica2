import random

class CluedoGame:
    def __init__(self):
        # Definición de sospechosos, lugares y armas
        self.sospechosos = ["Rodrigo", "Raúl", "Ana", "Juanjo", "Manuel", "Nicola", "David", "Fausto", "Jose Antonio"]
        self.lugares = {
            "Azotea": "En la azotea te encuentras a Rodrigo fumando estresado.",
            "Salida de emergencia": "Sales por la salida de emergencia y te encuentras a Raúl trapicheando con unos chavalines. Estos se asustan con tu presencia y se van.",
            "Aula 404": "Llegas al aula 404, el aula del grado en física. En ella está David explicándole a Victor la relación entre el grafeno las asíntotas.",
            "Baños": "Entras en el baño y te encuentras con Ana con los ojos inyectados en sangre y con la nariz roja por haber llorado.",
            "Recepción": "Cuando llegas a la recepción escuchas una buena bronca entre Nicola y el recepcionista. Parece que las pizarras que pidió Nicola para su clase aún no han llegado.",
            "Cafetería": "Entras en la cafetería, allí está comiendo sentado en una mesa Manuel. No habla, solo sonríe.",
            "Ascensor": "Estás esperando al ascensor, cuando finalmente llega este abre las puertas y de él sale José Antonio arrollándote.",
            "Biblioteca": "Entras en la biblioteca. Todo está vacío y en silencio. Al fondo está Fausto programando en su ordenador.",
            "Cuarto de seguridad": "Llegas a la sala de seguridad. Allí está Juanjo a oscuras echándose una partida de LOL en su portátil, a su lado una pantalla con todas las cámaras de la universidad."
        }
        self.armas = ["HP Prime", "Lápiz", "Máquina Expendedora", "G36", "Impresora 3D", "Cable HDMI"]

        # Seleccionar al azar el asesino, lugar del asesinato y arma utilizada
        self.asesino = random.choice(self.sospechosos)
        self.lugar_asesinato = random.choice(list(self.lugares.keys()))
        self.arma_utilizada = random.choice(self.armas)

        # Variables para controlar el estado del juego
        self.juego_activo = True
        self.iniciar_juego()

    def iniciar_juego(self):
        print("¡Bienvenidos a una emocionante noche llena de misterio y suspense! Están a punto de sumergirse en el intrigante mundo del Cluedo, un juego de mesa clásico que desafiará sus habilidades deductivas y los transportará a una universidad llena de secretos y conspiraciones.")
        print("\nEn este fascinante juego, se encuentran en la Universidad Alfonso X El Sabio, el campus de Chamberí, donde se encuentran unos estudiantes con un pasado turbio y oscuro. La noche ha caído, y la atmósfera está cargada de intriga. De repente, un grito rompe el silencio: Gonzalo, el delegado de clase, ha sido asesinado en circunstancias misteriosas.")
        print("\nAhora, ustedes, los valientes detectives, deben descubrir quién es el culpable, con qué arma cometieron el crimen y en qué habitación se llevó a cabo el asesinato. La universidad está llena de personajes sospechosos, cada uno con sus propios motivos y secretos ocultos.")
        print("\nPrepárense para sumergirse en una noche llena de engaños, alianzas cambiantes y giros inesperados. En el Cluedo, cada movimiento cuenta, y cada pista puede ser crucial para resolver el misterio. ¡Buena suerte, detectives! La verdad espera ser descubierta, pero el reloj está en marcha y el asesino podría estar más cerca de lo que imaginan. ¡Que comience la investigación!")

    def obtener_informacion_lugar(self, lugar):
        lugar = lugar.capitalize()
        if lugar in self.lugares:
            print(self.lugares[lugar])
        else:
            print("Este lugar no es válido. Intenta otro lugar.")

    def realizar_acusacion(self, sospechoso, lugar, arma):
        sospechoso = sospechoso.capitalize()
        lugar = lugar.capitalize()
        arma = arma.capitalize()

        if sospechoso == self.asesino and lugar == self.lugar_asesinato and arma == self.arma_utilizada:
            print("¡Felicidades! Has resuelto el caso. El asesino era {} en {} con un(a) {}.".format(
                self.asesino, self.lugar_asesinato, self.arma_utilizada))
            self.juego_activo = False
        else:
            print("Incorrecto. El asesino no era {} en {} con un(a) {}. Inténtalo de nuevo.".format(
                sospechoso, lugar, arma))

    def realizar_pregunta(self, tipo_pregunta):
        if tipo_pregunta == "sospechoso":
            pregunta = "¿Sobre qué sospechoso quieres preguntar? "
            opciones = self.sospechosos
        elif tipo_pregunta == "lugar":
            pregunta = "¿Sobre qué lugar quieres preguntar? "
            opciones = list(self.lugares.keys())
        elif tipo_pregunta == "arma":
            pregunta = "¿Sobre qué arma quieres preguntar? "
            opciones = self.armas
        else:
            print("Tipo de pregunta no válido.")
            return

        while True:
            print(f"\nOpciones disponibles: {opciones}")
            eleccion = input(pregunta).capitalize()

            if eleccion in opciones:
                if tipo_pregunta == "sospechoso":
                    if eleccion == self.asesino:
                        print(f"\n{eleccion} es el principal sospechoso. ¡Cuidado!")
                        # Agregar pistas relacionadas con el hecho de que es el asesino
                        pistas_asesino = [
                            f"{eleccion} ha estado actuando de manera nerviosa últimamente.",
                            f"Se rumorea que {eleccion} tenía una disputa con la víctima, Gonzalo.",
                            f"Hay pruebas que vinculan a {eleccion} con el lugar del crimen."
                        ]
                        pista_aleatoria = random.choice(pistas_asesino)
                    else:
                        print(f"\nInvestigando a {eleccion}...")
                        # Agregar pistas relacionadas con el hecho de que no es el asesino
                        pistas_no_asesino = [
                            f"{eleccion} tiene una coartada sólida para el momento del crimen.",
                            f"Testigos confirman que {eleccion} estaba en otro lugar cuando ocurrió el asesinato.",
                            f"No hay indicios que conecten a {eleccion} con el crimen."
                        ]
                        pista_aleatoria = random.choice(pistas_no_asesino)

                elif tipo_pregunta == "lugar":
                    if eleccion == self.lugar_asesinato:
                        print(f"\nInvestigando el lugar {eleccion}...")
                        # Agregar pistas relacionadas con el hecho de que es el lugar del asesinato
                        pistas_lugar_asesinato = [
                            f"Se encontraron pruebas de la presencia del asesino en {eleccion}.",
                            f"Testigos informaron haber visto a alguien sospechoso cerca de {eleccion}.",
                            f"Hay indicios que apuntan a que el crimen ocurrió en {eleccion}."
                        ]
                        pista_aleatoria = random.choice(pistas_lugar_asesinato)
                    else:
                        print(f"\nInvestigando el lugar {eleccion}...")
                        # Agregar pistas relacionadas con el hecho de que no es el lugar del asesinato
                        pistas_no_lugar_asesinato = [
                            f"No hay pruebas que indiquen que el crimen ocurrió en {eleccion}.",
                            f"Testigos confirman que {eleccion} estaba vacío en el momento del asesinato.",
                            f"Ninguna pista conecta a {eleccion} con el lugar del crimen."
                        ]
                        pista_aleatoria = random.choice(pistas_no_lugar_asesinato)

                elif tipo_pregunta == "arma":
                    if eleccion == self.arma_utilizada:
                        print(f"\nInvestigando el arma {eleccion}...")
                        # Agregar pistas relacionadas con el hecho de que es el arma utilizada
                        pistas_arma_utilizada = [
                            f"{eleccion} es el arma que se utilizó para cometer el crimen.",
                            f"Huellas del asesino fueron encontradas en {eleccion}.",
                            f"Hay testigos que vieron a alguien con {eleccion} cerca del lugar del asesinato."
                        ]
                        pista_aleatoria = random.choice(pistas_arma_utilizada)
                    else:
                        print(f"\nInvestigando el arma {eleccion}...")
                        # Agregar pistas relacionadas con el hecho de que no es el arma utilizada
                        pistas_no_arma_utilizada = [
                            f"No hay pruebas que conecten a {eleccion} con el crimen.",
                            f"{eleccion} parece no haber sido manipulado recientemente.",
                            f"Testigos informaron haber visto a alguien con un arma diferente cerca del lugar del crimen."
                        ]
                        pista_aleatoria = random.choice(pistas_no_arma_utilizada)

                print(f"Pista adicional: {pista_aleatoria}")
                break
            else:
                print("Elección no válida. Inténtalo de nuevo.")

    def explorar_lugares(self):
        print("\nTe encuentras en la entrada del campus de la universidad Alfonso X el sabio de Arapiles. Hay varios lugares para investigar:")
        print(list(self.lugares.keys()))

        pregunta_realizada = False

        while self.juego_activo:
            lugar_elegido = input("\nElige un lugar para investigar (o escribe 'salir' para terminar): ").capitalize()

            if lugar_elegido.lower() == 'salir':
                print("Gracias por jugar. ¡Hasta la próxima!")
                self.juego_activo = False
            elif lugar_elegido in self.lugares:
                self.obtener_informacion_lugar(lugar_elegido)

                if not pregunta_realizada:
                    opcion = input("¿Quieres buscar otra sala (s), realizar una investigación (i) o hacer una pregunta (p)? ").lower()
                    if opcion == 's':
                        print("\nVolvamos a la lista de lugares disponibles:")
                        print(list(self.lugares.keys()))
                    elif opcion == 'i':
                        sospechoso = input("Ingresa el nombre del sospechoso: ").capitalize()
                        lugar = input("Ingresa el nombre del lugar: ").capitalize()
                        arma = input("Ingresa el arma utilizada: ").capitalize()
                        self.realizar_acusacion(sospechoso, lugar, arma)
                    elif opcion == 'p':
                        tipo_pregunta = input("¿Quieres preguntar sobre un sospechoso (s), un lugar (l) o un arma (a)? ").lower()
                        self.realizar_pregunta(tipo_pregunta)
                        pregunta_realizada = True
                    else:
                        print("Opción no válida. Volviendo al menú principal.")
                    pregunta_realizada = False  # Restablecer la variable después de cada pregunta
                else:
                    print("No puedes hacer otra pregunta hasta que investigues otra sala.")
            else:
                print("Lugar no válido. Intenta de nuevo.")

# Ejemplo de uso
juego = CluedoGame()
juego.explorar_lugares()