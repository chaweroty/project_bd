from assistant import Assistant
from database import EntrenadorPersonalDB

class Usuario:
    def __init__(self, nombre, edad, genero, peso, objetivo, frecuencia_entrenamiento):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.peso = peso
        self.objetivo = objetivo
        self.frecuencia_entrenamiento = frecuencia_entrenamiento

def main():
    assistant = Assistant()
    db = EntrenadorPersonalDB()

    db.crear_tabla_usuarios()

    assistant.speak("Bienvenido en este mundo apasionante como lo es el fitness")
    assistant.speak("Dime un nombre")
    nombre = assistant.listen()

    assistant.speak("Dime una edad")
    edad = int(assistant.listen())

    assistant.speak("Dime un género")
    genero = assistant.listen()

    assistant.speak("Dime un peso")
    peso = float(assistant.listen())

    assistant.speak("Dime un objetivo")
    objetivo = assistant.listen()

    assistant.speak("Dime la frecuencia de entrenamiento en días")
    frecuencia_entrenamiento = int(assistant.listen())

    usuario = Usuario(nombre, edad, genero, peso, objetivo, frecuencia_entrenamiento)
    db.agregar_usuario(usuario)

    # Obtener la rutina correspondiente al objetivo del usuario
    rutina = db.obtener_rutina_por_objetivo(objetivo)
    if rutina:
        # Mostrar la descripción de la rutina al usuario
        assistant.speak(f"A continuación, te presento la rutina para tu objetivo {objetivo}: {rutina[3]}")
    else:
        assistant.speak("Lo siento, no hay una rutina disponible para ese objetivo")

    assistant.speak("Usuario creado exitosamente")

if __name__ == "__main__":
    main()
