from util import connect
import time

# Inner join reviews and listings table,
# filter for matching listing id and order by date.
FIND_RECENT_REVIEW = \
    '''
        select
            l.host_name,
            l.price,
            r.comments
        from
            reviews r,
            listings l
        where
            r.listing_id = :listing_id
            and r.listing_id = l.id
        order by
            date(r.date) desc;
    '''


def main():
    listing_id = input("Enter the listing_id: ")
    data = find_recent_review(listing_id)
    if data is None:
        print("No reviews found")
    else:
        print("\nHost Name: {}\nPrice: {}\nComment: {}".format(
            data[0], data[1], data[2]))


def find_recent_review(listing_id: str):
    connection = connect()
    cursor = connection.cursor()
    t_start = time.process_time()
    cursor.execute(FIND_RECENT_REVIEW, {"listing_id": listing_id})
    t_taken = time.process_time()-t_start
    print("Total time taken: {}s".format(t_taken))
    return cursor.fetchone()


if __name__ == "__main__":
    main()
