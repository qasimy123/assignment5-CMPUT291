# Referenced answer from user zero323 to understand how to unwind an empty list with a default
# Link to author's profile:
# https://stackoverflow.com/users/1560062/zero323
# Link to original source:
# https://stackoverflow.com/questions/31058374/mongodb-aggregation-with-unwind-on-empty-array
# Licence:  CC BY-SA 4.0
# Date posted: Jun 25 2015
# Website: Stack Overflow

from util import connectMongo
from typing import List
import time


def main():
    listing_id = input("Enter the listing_id: ")
    data = find_recent_review(listing_id)
    if data is None or len(data) == 0:
        print("Listing not found")
    else:
        print("The host_name, rental_price and most recent review for given listing_id")
        for review in data:
            print("\nHost Name: {}\nPrice: {}\nComment: {}".format(
                review['host_name'], review['price'], review['reviews']['comments']))


def find_recent_review(listing_id: str) -> List:
    db = connectMongo()
    listings_collection = db["listings"]
    try:
        t_start = time.process_time()
        cursor = listings_collection.aggregate([
            {"$match": {"id": int(listing_id)}},  # Find the matching listing
            # This projection is in the case that the listing does not have a review
            {"$project": {"host_name": 1, "price": 1, "reviews": {
                "$cond": {
                    "if": {"$eq": [{"$size": "$reviews"}, 0]},
                    "then": [{"comments": "None"}],
                    "else": "$reviews"
                }
            }}},
            {"$unwind": "$reviews"},  # Unwind the reviews list to access attr
            {"$sort": {"reviews.date": -1, "_id": 1}}, {"$limit": 1},
            {"$project": {
                "host_name": 1, "price": 1,  "_id": 0, "reviews.comments": 1}}
        ])
        t_taken = time.process_time()-t_start
        data = list(cursor)
        print("Total time taken: {}s".format(t_taken))
        return data
    except ValueError:
        print("Invalid input")
        return None


if __name__ == "__main__":
    main()
