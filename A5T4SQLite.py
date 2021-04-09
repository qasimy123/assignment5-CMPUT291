from util import connect

QUERY_4 = ''' 
    select
        id
    from
        listings
    where
        id not in (
            select
                listing_id
            from
                reviews
        )
    order by
        id desc
    limit
        10;
'''


def main():
    task4()


def task4():
    connection = connect()
    cursor = connection.cursor()

    cursor.execute(QUERY_4)
    rows = cursor.fetchall()

    if len(rows):
        print("Ten properties that have not recieved any review, ordered by listing_id: ")
        for row in rows:
            print("".join(map(str, row)))
    else:
        print('Error finding result ')

    connection.commit()
    connection.close()


if __name__ == "__main__":
    main()
