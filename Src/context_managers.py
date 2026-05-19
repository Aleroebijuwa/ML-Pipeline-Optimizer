import sqlite3


class SQLDatabase:
   
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"[DB ERROR] {exc_value}")
            self.connection.rollback()
        else:
            self.connection.commit()

        self.cursor.close()
        self.connection.close()



class FileHandler:
   

    def __init__(self, file_path, mode="r"):
        self.file_path = file_path
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

        if exc_type:
            print(f"[FILE ERROR] {exc_value}")