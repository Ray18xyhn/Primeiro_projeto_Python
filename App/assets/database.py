import sqlite3
import os

class DB:
    def __init__(self, name, folder='Dados'):

        os.makedirs(folder, exist_ok=True)
        
        db_path = os.path.join(folder, f"{name}.db")
        
        self.db = sqlite3.connect(db_path, check_same_thread=False)
        self.c = self.db.cursor()
        self.c.execute("PRAGMA journal_mode=OFF;")


    def close_connection(self):
        self.db.close()


    def create_db(self):
        self.c.execute('''
        CREATE TABLE IF NOT EXISTS trabalhos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            hora_inicial INTEGER NOT NULL,
            hora_final INTEGER NOT NULL,
            minutos_trabalhados INTEGER NOT NULL,
            valor_hora INTEGER NOT NULL,
            valor_total INTEGER NOT NULL,
            contratante TEXT NOT NULL
        )
        ''')
        self.c.execute("PRAGMA journal_mode = DELETE;")
        self.db.commit()


    def save_work(self, data, hora_inicial, hora_final, minutos_trabalhados, valor_hora, valor_total, contratante):
        self.c.execute('''
        INSERT INTO trabalhos (data, hora_inicial, hora_final, minutos_trabalhados, valor_hora, valor_total, contratante)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (data, hora_inicial, hora_final, minutos_trabalhados, valor_hora, valor_total, contratante))
        self.db.commit()


    def get_all_works(self):
        self.c.execute('SELECT * FROM trabalhos')
        return self.c.fetchall() 
    
    def dell_work(self, id):
        try:
            self.c.execute(f"DELETE FROM trabalhos WHERE id = ?", (id,))
            self.db.commit()

        except sqlite3.Error as e:
            print("Erro ao deletar linha:", e)
        pass


db = DB(name='Trabalhos')
db.create_db()
