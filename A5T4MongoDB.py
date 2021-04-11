from typing import List
from util import connectMongo
import time
db = connectMongo()


def main():
    task4()


def task4() -> List:

    t_start = time.process_time()
    cursor = db.listings.find(
        {"reviews": []}, projection={"_id": 0, "id": 1}
    ).sort("id", -1).limit(10)

    data = list(cursor)
    print("Ten listed properties that have not recieved any review, ordered by listing_id: ")
    for result in data:
        print(result["id"])

    t_taken = time.process_time()-t_start
    print("Total time taken: {}s".format(t_taken))
    return data


if __name__ == "__main__":
    main()
