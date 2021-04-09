from pymongo.command_cursor import CommandCursor
from util import connectMongo
from typing import List


def main():
    listing_id = input("Enter the listing_id: ")
    data = find_recent_review(listing_id)
    print(data)


def find_recent_review(listing_id: str) -> List:
    db = connectMongo()
    listings_collection = db["listings"]
    try:
        cursor: CommandCursor = listings_collection.aggregate([
            {"$match": {"id": int(listing_id)}},  # Find the matching listing
            {"$unwind": "$reviews"},  # Unwind the reviews list to access attr
            {"$sort": {"reviews.date": -1, "_id": 1}}, {"$limit": 1},
            {"$project": {
                "host_name": 1, "price": 1,  "_id": 0, "reviews.comments": 1}}
        ])
        data = list(cursor)
        return data
    except ValueError:
        print("Invalid input")


if __name__ == "__main__":
    main()
