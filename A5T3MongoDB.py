from util import connectMongo


def main():
    task3()


def task3():
    
    db = connectMongo()
    cursor = db.listings.aggregate([
            {
            "$group": {

                "_id": "$host_id",
                "owned listings": {"$sum": 1},
            }},
            {"$sort": {"_id":-1}},
            {"$limit":10}
        ])

    for result in cursor:
        print(result)


if __name__ == "__main__":
    main()
