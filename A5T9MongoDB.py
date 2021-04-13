import pymongo
from pymongo.command_cursor import CommandCursor
from util import connectMongo
import time

db = connectMongo()
listings_collection = db["listings"]


def main():

    keywords = input("Enter comma seperated keywords: ")
    create_text_index()
    data = find_similar_listings(keywords)

    print("\nResult:")
    for row in data:
        print("Listing ID: {}, Listing Name: {}".format(
            row.get("id"), row.get("name")))


def create_text_index():
    # Create a text index on all the reviews for the listings
    try:
        print("Dropping old index")
        listings_collection.drop_index('reviews_index')
    except Exception:
        print("Failed to drop index")
    print("Creating new index")
    listings_collection.create_index([
        (
            "reviews.comments", pymongo.TEXT,
        )], name="reviews_index"
    )
    print("Done creating new index")


def create_query(keywords: str) -> str:
    list_of_words = keywords.split(',')
    new_list = []
    for keyword in list_of_words:
        new_list.append(keyword.strip())
    return " ".join(new_list)  # Space behaves as an OR operator


def find_similar_listings(keywords: str) -> CommandCursor:
    query = create_query(keywords)
    print("Searching: {}".format(query))

    t_start = time.process_time()
    # Find listings with the reviews most similar to the keywords
    cursor = listings_collection.find(
        {"$text": {"$search": query}},
        {"score": {"$meta": "textScore"}, "_id": False, "name": True,
         "id": True}
    ).sort([('score', {'$meta': 'textScore'})]).limit(3)
    t_taken = time.process_time() - t_start

    print("Total time taken: {}s".format(t_taken))
    return list(cursor)


if __name__ == "__main__":
    main()
