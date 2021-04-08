from typing import List
import sqlite3
import os
import csv

Connection = sqlite3.Connection


DB_PATH = "A5.db"

def connect() -> Connection:
    # Returns a connection to the database provided at the path.
    db_path = exact_path(DB_PATH)
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    # To enable foreign keys for SQLite
    cursor.execute(' PRAGMA foreign_keys=ON; ')
    connection.commit()
    return connection


def exact_path(path) -> str:
    curr = os.path.dirname(__file__)
    load_path = os.path.join(curr, path)
    return load_path


def load_data(path: str) -> List[str]:
    data_path = exact_path(path)
    data = []
    with open(data_path) as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            data.append(row)
        csvfile.close()
    return data[1:]


def is_valid_row(added, row) -> bool:
    return row[0] not in added
