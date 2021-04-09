from util import connect

QUERY_5 = ''' 
    select
        round(avg(price), 2)
    from
        listings
    where
        neighbourhood = :entry;
'''

def main():
    task5()

def task5():
    connection = connect()
    cursor = connection.cursor()

    entry = input("Specify the neighbourhood: ")
    
    cursor.execute(QUERY_5,{
        "entry":entry
    })
    rows = cursor.fetchall()

    if len(rows):
        print("Average rental cost per night for",entry+" is:")
        for row in rows:
            print("$"+"".join(map(str, row)))
    else:
        print(entry+" Does not exist in database")
    
    connection.commit()
    connection.close()

if __name__ == "__main__":
    main()