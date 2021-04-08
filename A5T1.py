# Task 1

# main.py is adapted from the SQLite-in-Python-1-Example1.py File from a lab
# File name: SQLite-in-Python-1-Example1.py
# Lab Title: Lab (Python & SQLite - Part 1)
# Link to Source: https://drive.google.com/file/d/11ukUPkVpdjjNPhocDZin5cdZUlHvELFZ/view
# Date Posted: 10:03 AM Feb 25, 2021
# Author: Professor Mario Nascimento

# Referenced the official python documentation to read csv
# https://docs.python.org/3/library/csv.html

from typing import List
import sqlite3
import csv
import os
import unittest

Connection = sqlite3.Connection
DB_PATH = "A5.db"
LISTING_SUMMARY_DATA = "YVR_Airbnb_listings_summary.csv"
REVIEW_DATA = "YVR_Airbnb_reviews.csv"

# id	name	host_id	host_name	neighbourhood	room_type	price	minimum_nights	availability_365
CREATE_SUMMARY_TABLE = '''
    CREATE TABLE listings (
        id INTEGER,
        -- ID of the listing
        name TEXT,
        -- Title of the listing
        host_id INTEGER,
        -- ID of the host for the listing
        host_name TEXT,
        -- Name of the host
        neighbourhood TEXT,
        -- Location of the listing
        room_type TEXT,
        -- The type of the room offered
        price INTEGER,
        -- The price of the listing
        minimum_nights INTEGER,
        -- The minimum nights the listing can be booked
        availability_365 INTEGER,
        -- The availability of the listing in a year
        PRIMARY KEY(id)
    );
    '''

# listing_id	id	date	reviewer_id	reviewer_name	comments
CREATE_REVIEW_TABLE = '''
    CREATE TABLE reviews (
        listing_id INTEGER,
        id INTEGER,
        date TEXT,
        reviewer_id INTEGER,
        reviewer_name TEXT,
        comments TEXT,
        PRIMARY KEY(id)
    );
    '''


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


def main() -> None:
    summary_data = load_data(LISTING_SUMMARY_DATA)
    review_data = load_data(REVIEW_DATA)
    make_main()
    populate_summary_table(summary_data)
    populate_review_table(review_data)


def make_main() -> None:
    connection = connect()
    
    delete_listings_table = '''
        DROP TABLE IF EXISTS listings;
    '''

    delete_reviews_table = '''
        DROP TABLE IF EXISTS reviews;
    '''
    connection.cursor().execute(delete_listings_table)
    connection.cursor().execute(delete_reviews_table)
    connection.cursor().execute(CREATE_SUMMARY_TABLE)
    connection.cursor().execute(CREATE_REVIEW_TABLE)
    connection.close()


def populate_review_table(review_data) -> None:
    connection = connect()
    query = '''
        INSERT INTO reviews VALUES(:listing_id, :id, :date, :reviewer_id, :reviewer_name, :comments);
    '''

    insertions = []
    for i in range(0, len(review_data)):
        insertions.append({
            "listing_id": review_data[i][0],
            "id": review_data[i][1],
            "date": review_data[i][2],
            "reviewer_id": review_data[i][3],
            "reviewer_name": review_data[i][4],
            "comments": review_data[i][5]
        })
    connection.executemany(query, insertions)

    connection.commit()
    connection.close()


def populate_summary_table(summary_data) -> None:
    connection = connect()
    query = '''
    INSERT INTO listings
        VALUES(:id, :name, :host_id, :host_name, :neighbourhood, :room_type, :price, :minimum_nights, :availability_365);
    '''

    insertions = []
    for i in range(0, len(summary_data)):
        pass_val = False
        for j in range(0, len(summary_data[i])):
            if(summary_data[i][j] == None):
                pass_val = True
        if(pass_val != True):
            insertions.append({
                "id": summary_data[i][0],
                "name": summary_data[i][1],
                "host_id": summary_data[i][2],
                "host_name": summary_data[i][3],
                "neighbourhood": summary_data[i][4],
                "room_type": summary_data[i][5],
                "price": summary_data[i][6],
                "minimum_nights": summary_data[i][7],
                "availability_365": summary_data[i][8]
            })
    connection.executemany(query, insertions)

    connection.commit()
    connection.close()

class DatabaseTest(unittest.TestCase):
    # Checksum verification
    def test_listings_table(self):
        connection = connect()
        test_query = '''
            SELECT MIN(host_id), MAX(host_id), AVG(host_id), COUNT(host_id) FROM listings;
        '''
        data = connection.cursor().execute(test_query).fetchone()
        print(data)
        connection.close()
        self.assertTupleEqual(data,  (6033, 387534175, 115176061.85829493, 4340))

    def test_reviews_table(self):
        connection = connect()
        test_query = '''
            SELECT MIN(id), MAX(id), AVG(id), COUNT(id) FROM reviews;
        '''
        data = connection.cursor().execute(test_query).fetchone()
        print(data)
        connection.close()
        self.assertTupleEqual(data, (26444, 730124064, 370354766.84915775, 147936))

if __name__ == "__main__":
    main()
    unittest.main()
