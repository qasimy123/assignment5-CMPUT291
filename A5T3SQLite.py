from util import connect
import time

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
    
    t_start = time.process_time()

    cursor.execute(QUERY_3)
    t_taken = time.process_time()-t_start
    rows = cursor.fetchall()

    if len(rows):
        print("How many listings the top ten hosts owns, ordered by host_id")
        for row in rows:
            print(("| ".join(map(str, row))))
    else:
        print('Error finding result ')

    connection.commit()
    connection.close()
    print("Total time taken: {}s".format(t_taken))


if __name__ == "__main__":
    main()
