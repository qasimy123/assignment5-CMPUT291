from typing import List
from util import connectMongo
import time
db = connectMongo()


def main():
    task3()


def task3() -> List:

    t_start = time.process_time()
    cursor = db.listings.aggregate([
        {
            "$group": {

                "_id": "$host_id",
                "owned listings": {"$sum": 1},
            }},
        {"$sort": {"_id": -1}},
        {"$limit": 10}
    ])
    t_taken = time.process_time()-t_start
    data = list(cursor)
    print("Top ten host_ids with the amount of listings they own ordered by host_id: ")
    for result in data:
        print(result['_id'],'|',result['owned listings'])
    print("Total time taken: {}s".format(t_taken))
    return data


if __name__ == "__main__":
    main()
