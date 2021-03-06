#!/usr/bin/env python3

import time
from util import connect, connectMongo
from typing import List
import unittest

db = connectMongo()
listings_collection = db["listings"]


def main():
    # This main function sets up the mongodb database and populates it
    print("Creating mongod collection, this will take around 1 minute...")
    populate_database()


def setup():
    # delete all previous entries in the listings collection
    print("Deleting all previous entries")
    listings_collection.delete_many({})


def getSQLiteData(query: str, params: dict = None,) -> List[tuple]:
    if params is None:
        params = {}
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query, params)
    data = cursor.fetchall()
    connection.close()
    return data


def populate_database():

    listings = []

    listings_data = getListingsTable()
    reviews_table = getReviewsTable()
    t_start = time.process_time()
    for listing in listings_data:
        reviews = []
        for review in reviews_table:
            if(review[0] == listing[0]):
                reviews.append({"listing_id": review[0],
                                "id": review[1],
                                "date": review[2],
                                "reviewer_id": review[3],
                                "reviewer_name": review[4],
                                "comments": review[5]})
        listings.append({
            "id": listing[0],
            "name": listing[1],
            "host_id": listing[2],
            "host_name": listing[3],
            "neighbourhood": listing[4],
            "room_type": listing[5],
            "price": listing[6],
            "minimum_nights": listing[7],
            "availability_365": listing[8],
            "reviews": reviews
        })
    t_taken = time.process_time()-t_start
    print("Print total time taken {}s".format(t_taken))
    setup()
    ret = listings_collection.insert_many(listings)
    # Print list of the _id values of the inserted documents
    listings_ids = ret.inserted_ids
    print("Print done adding {} documents".format(len(listings_ids)))


def getListingsTable() -> List[tuple]:
    query = "SELECT * FROM listings;"
    data = getSQLiteData(query)
    return data


def getReviewsTable() -> List[tuple]:
    query = "SELECT * FROM reviews;"
    data = getSQLiteData(query)
    return data


class DatabaseTest(unittest.TestCase):
    def test_listings_table(self):
        cursor = listings_collection.aggregate(
            [
                {"$group": {"_id": "null", "min": {"$min": "$host_id"},
                            "max": {
                    "$max": "$host_id"}, "avg": {"$avg": "$host_id"},
                    "count": {"$sum": 1}}}
            ]
        )
        result = list(cursor)
        print(result)

        self.assertListEqual([{'_id': 'null', 'min': 6033, 'max': 387534175,
                               'avg': 115176061.85829493,
                               'count': 4340}], result)

    def test_reviews_table(self):
        cursor = listings_collection.aggregate([

            {"$unwind": "$reviews"},

            {"$group": {"_id": "null", "min": {"$min": "$reviews.id"}, "max": {
                "$max": "$reviews.id"}, "avg": {"$avg": "$reviews.id"},
                "count": {"$sum": 1}}}

        ])

        result = list(cursor)
        print(result)
        self.assertListEqual([{'_id': 'null', 'min': 26444, 'max': 730124064,
                               'avg': 370354766.84915775,
                               'count': 147936}], result)


if __name__ == "__main__":
    # Uncomment the below line to repopulate the database
    main()
    unittest.main()
