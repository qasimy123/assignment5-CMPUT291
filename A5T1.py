# Task 1

# main.py is adapted from the SQLite-in-Python-1-Example1.py File from a lab
# File name: SQLite-in-Python-1-Example1.py
# Lab Title: Lab (Python & SQLite - Part 1)
# Link to Source: https://drive.google.com/file/d/11ukUPkVpdjjNPhocDZin5cdZUlHvELFZ/view
# Date Posted: 10:03 AM Feb 25, 2021
# Author: Professor Mario Nascimento

# Referenced the official python documentation to read csv
# https://docs.python.org/3/library/csv.html

import unittest
from util import connect, load_data

LISTINGS_DATA = "YVR_Airbnb_listings_summary.csv"
REVIEWS_DATA = "YVR_Airbnb_reviews.csv"

CREATE_LISTINGS_TABLE = '''
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

CREATE_REVIEWS_TABLE = '''
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


def main() -> None:
    listings_data = load_data(LISTINGS_DATA)
    review_data = load_data(REVIEWS_DATA)
    make_main()
    populate_listings_table(listings_data)
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
    connection.cursor().execute(CREATE_LISTINGS_TABLE)
    connection.cursor().execute(CREATE_REVIEWS_TABLE)
    connection.close()


def populate_review_table(review_data) -> None:
    connection = connect()
    query = '''
        INSERT INTO
            reviews
        VALUES(
                :listing_id,
                :id,
                :date,
                :reviewer_id,
                :reviewer_name,
                :comments
            );
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


def populate_listings_table(listings_data) -> None:
    connection = connect()
    query = '''
    INSERT INTO
        listings
    VALUES(
            :id,
            :name,
            :host_id,
            :host_name,
            :neighbourhood,
            :room_type,
            :price,
            :minimum_nights,
            :availability_365
        );
    '''

    insertions = []
    for i in range(0, len(listings_data)):
        pass_val = False
        for j in range(0, len(listings_data[i])):
            if listings_data[i][j] is None:
                pass_val = True
        if pass_val is not True:
            insertions.append({
                "id": listings_data[i][0],
                "name": listings_data[i][1],
                "host_id": listings_data[i][2],
                "host_name": listings_data[i][3],
                "neighbourhood": listings_data[i][4],
                "room_type": listings_data[i][5],
                "price": listings_data[i][6],
                "minimum_nights": listings_data[i][7],
                "availability_365": listings_data[i][8]
            })
    connection.executemany(query, insertions)

    connection.commit()
    connection.close()


class DatabaseTest(unittest.TestCase):
    # Checksum verification
    def test_listings_table(self):
        connection = connect()
        test_query = '''
            SELECT
                MIN(host_id),
                MAX(host_id),
                AVG(host_id),
                COUNT(host_id)
            FROM
                listings;
        '''
        data = connection.cursor().execute(test_query).fetchone()
        print(data)
        connection.close()
        self.assertTupleEqual(
            data,  (6033, 387534175, 115176061.85829493, 4340))

    def test_reviews_table(self):
        connection = connect()
        test_query = '''
            SELECT
                MIN(id),
                MAX(id),
                AVG(id),
                COUNT(id)
            FROM
                reviews;
        '''
        data = connection.cursor().execute(test_query).fetchone()
        print(data)
        connection.close()
        self.assertTupleEqual(
            data, (26444, 730124064, 370354766.84915775, 147936))


if __name__ == "__main__":
    main()
    unittest.main()
