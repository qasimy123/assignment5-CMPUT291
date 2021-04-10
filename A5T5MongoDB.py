from util import connectMongo


def main():
    task5()


def task5():
    
    db = connectMongo()
    entry = input("Specify the neighbourhood: ")
    
    cursor = db.listings.aggregate([
    { "$match": { "neighbourhood": entry } },
    { "$group": { "_id": "null", "avg": {"$avg":"$price" } }}

    ])
    # cursor2 = db.listings.aggregate([{
    #     "$project":{
    #         "neighbourhood":1,
    #         "price":{"$sum":1}
    #     },
    # },
    # {
    #     "$match":{
    #         "neighbourhood":entry
    #     }
    # }
    # ])    
    

    # for result in cursor:
    #     print(result)

    for result in cursor:
        print(result)

if __name__ == "__main__":
    main()
