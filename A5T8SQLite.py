from util import connect

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
    print(data)


def find_recent_review(listing_id: str):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(FIND_RECENT_REVIEW, {"listing_id": listing_id})
    return cursor.fetchone()


if __name__ == "__main__":
    main()
