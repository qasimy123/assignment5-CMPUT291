from util import connectMongo
import time
db = connectMongo()

def main():
    task5()


def task5():
    
    entry = input("Specify the neighbourhood: ")
    t_start = time.process_time()

    # Task 5:
    # Given a neighbourhood at run-time (e.g., using command line prompt or via an application parameter) 
    # find the average rental cost/night?
    cursor = db.listings.aggregate([
    { "$match": { "neighbourhood": entry } },
    { "$group": { "_id": "null", "avg": {"$avg":"$price" } }}
    ])
    t_taken = time.process_time()-t_start
    
    for result in cursor:
         print("{:.2f}".format(result['avg']))
    print("Total time taken: {}s".format(t_taken))


if __name__ == "__main__":
    main()
