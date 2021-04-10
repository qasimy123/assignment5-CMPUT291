from util import connectMongo


def main():
    task4()

def task4():
    
    db = connectMongo()
    no_reviews=[]

    no_review_cursor = db.listings.find(
        {"reviews":[]}
    ).sort("reviews",-1).limit(10)
    
    # Here I'm appending the the id's that have not recieved reviews
    # i.e the array is empty
    for result in no_review_cursor:
        no_reviews.append(result["id"])

    # Here I check through that 
    cursor = db.listings.find({
    "id":{"$nin":no_reviews}},
    ).sort("id",-1).limit(10)
    
    if result:
        print("Ten listed properties that have not recieved any review, ordered by listing_id:")
        for result in cursor:
            print(result["id"])
    else:
        print('Error finding result')
        


if __name__ == "__main__":
    main()
