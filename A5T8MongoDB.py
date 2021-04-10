from util import connectMongo
from typing import List
import time


def main():
    listing_id = input("Enter the listing_id: ")
    data = find_recent_review(listing_id)
    if data is None:
        print("No reviews found")
    else:
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
            {"$unwind": "$reviews"},  # Unwind the reviews list to access attr
            {"$sort": {"reviews.date": -1, "_id": 1}}, {"$limit": 1},
            {"$project": {
                "host_name": 1, "price": 1,  "_id": 0, "reviews.comments": 1}}
        ])
        data = list(cursor)
        t_taken = time.process_time()-t_start
        print("Total time taken: {}s".format(t_taken))
        return data
    except ValueError:
        print("Invalid input")
        return None


if __name__ == "__main__":
    main()
