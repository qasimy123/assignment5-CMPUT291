from util import connect
import time

# Inner join reviews and listings table,
# filter for matching listing id and order by date.
FIND_RECENT_REVIEW = \
    '''
        select
            r.comments
        from
            reviews r
        where
            r.listing_id = :listing_id
        order by
            date(r.date) desc;
    '''

FIND_LISTING_HOST_AND_PRICE = \
    '''
        select
            l.host_name,
            l.price
        from
            listings l
        where l.id = :listing_id;
    '''


def main():
    listing_id = input("Enter the listing_id: ")
    review_data = find_recent_review(listing_id)
    if review_data is None:
        review_data = [None]
    listing_data = find_listing(listing_id)
    if listing_data is None:
        print("Listing not found")
    else:
        print("\nHost Name: {}\nPrice: {}\nComment: {}".format(
            listing_data[0], listing_data[1], review_data[0]))


def find_recent_review(listing_id: str):
    connection = connect()
    cursor = connection.cursor()
    t_start = time.process_time()
    cursor.execute(FIND_RECENT_REVIEW, {"listing_id": listing_id})
    t_taken = time.process_time()-t_start
    print("Total time taken to find the review: {}s".format(t_taken))
    return cursor.fetchone()


def find_listing(listing_id: str):
    connection = connect()
    cursor = connection.cursor()
    t_start = time.process_time()
    cursor.execute(FIND_LISTING_HOST_AND_PRICE, {"listing_id": listing_id})
    t_taken = time.process_time()-t_start
    print("Total time taken to find listing: {}s".format(t_taken))
    return cursor.fetchone()


if __name__ == "__main__":
    main()
