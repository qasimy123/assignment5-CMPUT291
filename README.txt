Requirements:
[X] A .tgz file 
    [X] containing a README.txt file
    [X] all necessary (and commented) source code in python necessary to execute the application.
[X] The README file should have the name(s) of student(s), their ccid(s), 
[X] collaboration statement, 
[X] a list of all included files, plus a .txt file with brief instructions on how to run the application. 
[X] The README file should also include a section with a simple "how to” guide for executing each task. 
[X] The .tgz file (containing 10 files, README.txt plus 11 .py files) should be submitted using this submission page.


Name            |CCID                  |
----------------------------------------
Qasim Khawaja   |khawaja               |
----------------------------------------
Muhammad Haris  |mharis2               |
----------------------------------------

Collaboration Statement: Muhammad Haris and Qasim Khawaja collaborated on this assignment. 
Qasim worked on implementing Task 1, Task 2, Task 8, and Task 9, Muhammad Haris worked on implementing Task 3, Task 4, and Task 5.
We both worked on the application interface collabaratively.

Included files:

1. A5T1.py
2. A5T2.py
3. A5T3MongoDB.py
4. A5T3SQLite.py
5. A5T4MongoDB.py
6. A5T4SQLite.py
7. A5T5MongoDB.py
8. A5T5SQLite.py
9. A5T8MongoDB.py
10. A5T8SQLite.py
11. A5T9MongoDB.py
12. util.py  ** This file must be in the same directory as the application files. **
13. TestA5.py ** Not required but includes tests for all the application files **
14. setup.py ** Installs the pymongo library **
15. YVR_Airbnb_listings_summary.csv ** CSV file required by A5T1.py **
16. YVR_Airbnb_reviews.csv ** CSV file required by A5T1.py **

Instructions: 

1. `cd` to the root directory for this project.
2. run `python3 setup.py` in the terminal. ** This is to install all the required dependencies for the project **
3. run A5T1.py in the terminal to generate the SQLite database  (named: A5.db)
4. run A5T2.py in the terminal to populate the MongoDB database. (Not mandatory as the database is prepopulated and is hosted on the cloud)
5. Ready to run the tasks.

How-to:

Running Task 3.

    For MongoDB 
    1. run `python3 A5T3MongoDB.py` in the terminal
    2. The host_id and their owned listings will be printed to stdout.

    For SQLite 
    1. run `python3 A5T3SQLite.py` in the terminal
    2. The host_id and their owned listings will be printed to stdout.

Running Task 4.

    For MongoDB
    1. run `python3 A5T4MongoDB.py` in the terminal
    2. The listing_id with no reviews will be printed to stdout.

    For SQLite 
    1. run `python3 A5T4SQLite.py` in the terminal
    2. The listing_id with no reviews will be printed to stdout.

Running Task 5.

    For MongoDB
    1. run `python3 A5T5MongoDB.py` in the terminal
    2. You will be prompted to enter the neighborhood. Enter the neighborhood name and press enter.
    3. The average will be printed to stdout.

    For SQLite 
    1. run `python3 A5T5SQLite.py` in the terminal
    2. You will be prompted to enter the neighborhood. Enter the neighborhood name and press enter.
    3. The average will be printed to stdout.

Running Task 8.

    For MongoDB
    1. run `python3 A5T8MongoDB.py` in the terminal
    2. You will be prompted to enter the listing_id. Enter the listing_id and press enter.
    3. The host_name, price, and most recent comments will be printed to stdout.

    For SQLite 
    1. run `python3 A5T8SQLite.py` in the terminal
    2. You will be prompted to enter the listing_id. Enter the listing_id and press enter.
    3. The host_name, price, and most recent comments will be printed to stdout.

Running Task 9.

    For MongoDB
    1. run `python3 A5T9MongoDB.py` in the terminal
    2. You will be prompted to enter the comma separated list of keywords. Enter the keywords and press enter.
    3. The top 3 listing names with the most similar reviews will be printed to stdout.

Citations:

Referenced answer from user zero323 to understand how to unwind an empty list with a default value.
Link to author's profile:
https://stackoverflow.com/users/1560062/zero323
Link to original source:
https://stackoverflow.com/questions/31058374/mongodb-aggregation-with-unwind-on-empty-array
Licence:  CC BY-SA 4.0
Date posted: Jun 25 2015
Website: Stack Overflow