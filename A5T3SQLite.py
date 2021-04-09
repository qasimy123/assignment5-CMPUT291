from util import connect

QUERY_3 = ''' 
    select
        host_id,
        count(id)
    from
        listings
    group by
        host_id
    order by
        host_id desc
    limit
        10;
'''


def main():
    task3()


def task3():
    connection = connect()
    cursor = connection.cursor()

    cursor.execute(QUERY_3)
    rows = cursor.fetchall()

    if len(rows):
        print("How many listings the top ten hosts owns, ordered by host_id")
        for row in rows:
            print(("| ".join(map(str, row))))
    else:
        print('Error finding result ')

    connection.commit()
    connection.close()


if __name__ == "__main__":
    main()
