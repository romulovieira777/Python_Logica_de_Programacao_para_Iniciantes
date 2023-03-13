import sqlite3
from sqlite3 import Error


def createDataBase(dbName):
    print(f"Criando DB SQLite em, {dbName}")

    conn = None

    try:
        conn = sqlite3.connect(dbName)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    dbPath = ""

    createDataBase(dbPath)
