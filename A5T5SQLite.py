from util import connect
import time
QUERY_5 = '''
    select
        round(avg(price), 2)
    from
        listings
    where
        neighbourhood = :entry;
'''


def main():
    neighbourhood = input("Specify the neighbourhood: ")
    task5(neighbourhood)


def task5(neighbourhood: str):
    connection = connect()
    cursor = connection.cursor()

    t_start = time.process_time()
    cursor.execute(QUERY_5, {
        "entry": neighbourhood
    })
    t_taken = time.process_time()-t_start
    rows = cursor.fetchall()

    if len(rows):
        print("Average rental cost per night for", neighbourhood+" is:")
        for row in rows:
            print("$"+"".join(map(str, row)))
    else:
        print(neighbourhood+" Does not exist in database")

    connection.commit()
    connection.close()

    print("Total time taken: {}s".format(t_taken))
    return rows


if __name__ == "__main__":
    main()
