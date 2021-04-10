from util import connectMongo
import time
db = connectMongo()

def main():
    task3()


def task3():
    
    t_start = time.process_time()
    cursor = db.listings.aggregate([
            {
            "$group": {

                "_id": "$host_id",
                "owned listings": {"$sum": 1},
            }},
            {"$sort": {"_id":-1}},
            {"$limit":10}
        ])
    t_taken = time.process_time()-t_start
    
    for result in cursor:
        print(result)
    print("Total time taken: {}s".format(t_taken))    


if __name__ == "__main__":
    main()
