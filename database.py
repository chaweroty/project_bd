import sqlite3

class EntrenadorPersonalDB:
    def __init__(self, db_path='entrenador_personal.db'):
        self.db_path = db_path

    def crear_tabla_usuarios(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                     (id INTEGER PRIMARY KEY,
                     nombre TEXT,
                     edad INTEGER,
                     genero TEXT,
                     peso REAL,
                     objetivo TEXT,
                     frecuencia_entrenamiento INTEGER)''')
        conn.commit()
        conn.close()

    def crear_tabla_rutinas(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS rutinas
                     (id INTEGER PRIMARY KEY,
                     objetivo TEXT,
                     dias_semana INTEGER,
                     descripcion TEXT)''')
        conn.commit()
        conn.close()

    def agregar_usuario(self, usuario):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''INSERT INTO usuarios (nombre, edad, genero, peso, objetivo, frecuencia_entrenamiento)
                     VALUES (?, ?, ?, ?, ?, ?)''', (usuario.nombre, usuario.edad, usuario.genero, usuario.peso, usuario.objetivo, usuario.frecuencia_entrenamiento))
        conn.commit()
        conn.close()

    def agregar_rutina(self, objetivo, dias_semana, descripcion):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''INSERT INTO rutinas (objetivo, dias_semana, descripcion)
                     VALUES (?, ?, ?)''', (objetivo, dias_semana, descripcion))
        conn.commit()
        conn.close()

    def obtener_rutina_por_objetivo(self, objetivo):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT * FROM rutinas WHERE objetivo=?", (objetivo,))
        rutina = c.fetchone()
        conn.close()
        return rutina
