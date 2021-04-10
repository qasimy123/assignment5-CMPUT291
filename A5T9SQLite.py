from util import connect
import time

# Search on the comments index for list
FIND_SIMILAR_LISTINGS = \
    '''
        SELECT
            name, c.comment
        FROM
            comments c,
            listings l
        WHERE
            l.id = c.listing_id
            AND c.comment MATCH :query
        ORDER BY
            RANK
        LIMIT
            3;
    '''

# Get all comments from reviews table
GET_ALL_COMMENTS = \
    '''
        SELECT comments, listing_id FROM reviews;
    '''

# Create a virtual table using fts5
CREATE_VIRTUAL_TABLE = \
    '''
        CREATE VIRTUAL TABLE comments USING fts5(comment, listing_id);
    '''
# Drop the virtual table if it already exists
DROP_VIRTUAL_TABLE = \
    '''
        DROP TABLE IF EXISTS comments;
    '''
# Insert comments into index
INSERT_VIRTUAL_TABLE = \
    '''
        INSERT INTO comments
        VALUES(?, ?);
    '''


def main():

    keywords = input("Enter comma seperated keywords: ")

    create_virtual_table()
    data = find_similar_listings(keywords)

    print("\nResult:")
    for row in data:
        print(row)


def create_virtual_table():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(DROP_VIRTUAL_TABLE)
    cursor.execute(CREATE_VIRTUAL_TABLE)
    cursor.execute(GET_ALL_COMMENTS)
    reviews_data = cursor.fetchall()
    insertions = []
    for entry in reviews_data:  # Populate with all the comments
        insertions.append(entry)
    connection.executemany(INSERT_VIRTUAL_TABLE, insertions)
    connection.commit()
    connection.close()


def create_query(keywords) -> str:
    list_of_words = keywords.split(',')
    new_list = []
    for keyword in list_of_words:
        new_list.append(keyword.strip())
    return " OR ".join(new_list)


def find_similar_listings(keywords: str):
    connection = connect()
    cursor = connection.cursor()
    query = create_query(keywords)
    print("Searching: {}".format(query))
    t_start = time.process_time()
    cursor.execute(FIND_SIMILAR_LISTINGS, {"query": query})
    t_taken = time.process_time() - t_start
    print("Total time taken: {}s".format(t_taken))
    return cursor.fetchall()


if __name__ == "__main__":
    main()
