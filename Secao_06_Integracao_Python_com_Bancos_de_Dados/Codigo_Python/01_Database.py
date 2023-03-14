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


def getDbConnection(dbName):
    conn = None

    try:
        conn = sqlite3.connect(dbName)
        print("Conectado ao SQLite com sucesso!")
        return conn
    except Error as e:
        print(e)

    return conn


def createTable(conn, tblName):
    connection = None

    try:
        connection = conn.cursor()
        connection.execute(tblName)
        print("Tabela criada com sucesso!")
    except Error as e:
        print(e)


if __name__ == "__main__":
    dbPath = ""

    #createDataBase(dbPath)

    conn = getDbConnection(dbPath)

    dbTableCreate = """CREATE TABLE IF NOT EXISTS usario (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT,
        curso TEXT
    );"""

    createTable(conn, dbTableCreate)
