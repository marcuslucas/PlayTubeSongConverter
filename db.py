import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def read_from_db(conn):
    c = conn.cursor()
    c.execute('SELECT id, title, position FROM videos')
    data = c.fetchall()
    return data

def get_files(db_file):
    return read_from_db(create_connection(db_file))


if __name__ == '__main__':
    db_file = "data/playTube.db"
    print(get_files(db_file))

