from typing import List
from util import connectMongo
import time
db = connectMongo()


def main():
    neighbourhood = input("Specify the neighbourhood: ")
    task5(neighbourhood)


def task5(neighbourhood: str) -> List:

    t_start = time.process_time()

    # Task 5:
    # Given a neighbourhood at run-time (e.g., using command line prompt or via an application parameter)
    # find the average rental cost/night?
    cursor = db.listings.aggregate([
        {"$match": {"neighbourhood": neighbourhood}},
        {"$group": {"_id": "null", "avg": {"$avg": "$price"}}}
    ])
    t_taken = time.process_time()-t_start
    data = list(cursor)
    if data:
        print("Average rental cost per night for", neighbourhood+" is:")
        for result in data:
            print("{:.2f}".format(result['avg']))
        print("Total time taken: {}s".format(t_taken))
    else:
        print(neighbourhood+" Does not exist in database")
    return data


if __name__ == "__main__":
    main()
