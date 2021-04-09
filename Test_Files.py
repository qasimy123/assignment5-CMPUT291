import unittest
from A5T8MongoDB import find_recent_review as find_recent_review_mongo
from A5T8SQLite import find_recent_review as find_recent_review_sqlite
from A5T9MongoDB import find_similar_listings as find_similar_listings_mongo
from A5T9SQLite import find_similar_listings as find_similar_listings_sqlite, create_virtual_table


COMPARE = [{'host_name': 'Chris', 'price': 150, 'reviews': {'comments': 'Am Tag unserer Abreise nach Vancouver erhielten wir von Chris die Nachricht, dass sie uns das von uns gemietete Apartment nicht überlassen kann aufgrund eines Wasserschadens.\nEine sehr unglückliche Situation, die aber eintreten kann. Chris hat sich mit unglaublichem Einsatz innerhalt von 24 Stunden darum bemüht, eine Ersatzunterkunft zu finden, was sehr schwierig war. So kamen wir in Vancouver an und hatten eine Unterkunft auch wenn es nicht wie erwartet war. Aber wir haben uns einigen können und anerkennen sehr, wie Chris sich für uns eingesetzt hat. Das war sicherlich nicht selbstverständlich.\nTrotz aller Unannehmlichkeiten am Anfang haben wir einen positiven Eindruck erhalten.'}}]


class A5T8MongoTest(unittest.TestCase):
    def test_find_recent_review(self):
        data = find_recent_review_mongo(22128)
        self.assertListEqual(COMPARE, data)


class A5T8SQLiteTest(unittest.TestCase):
    def test_find_recent_review(self):
        data = find_recent_review_sqlite(22128)
        self.assertTupleEqual(('Chris', 150, 'Am Tag unserer Abreise nach Vancouver erhielten wir von Chris die Nachricht, dass sie uns das von uns gemietete Apartment nicht überlassen kann aufgrund eines Wasserschadens.\nEine sehr unglückliche Situation, die aber eintreten kann. Chris hat sich mit unglaublichem Einsatz innerhalt von 24 Stunden darum bemüht, eine Ersatzunterkunft zu finden, was sehr schwierig war. So kamen wir in Vancouver an und hatten eine Unterkunft auch wenn es nicht wie erwartet war. Aber wir haben uns einigen können und anerkennen sehr, wie Chris sich für uns eingesetzt hat. Das war sicherlich nicht selbstverständlich.\nTrotz aller Unannehmlichkeiten am Anfang haben wir einen positiven Eindruck erhalten.'), data)


class A5T9SQLiteTest(unittest.TestCase):
    def test_find_similar_listings(self):
        create_virtual_table()
        data = find_similar_listings_sqlite("gross, disgusting, ugly")
        print(data)
        self.assertListEqual(data, [('*New Modern Studio in Van, Near Airport &Downtown*', 'das studio ist gut gelegen, nahe skytrain station, sauber, gross und schön. würde wieder buchen.'), ('Beautiful Heritage Home in Kitsilano', 'Great place, terrific location, very homey and well appointed.  Unfortunately the bathroom shower stall was very disgusting with mold and mildew.'), ('Downtown Vancouver Penthouse Private Room 3003', 'Apartment was in a great area and had a great view. The bedding was old and felt disgusting, but had a good time.')])


class A5T9MongoDBTest(unittest.TestCase):
    def test_find_similar_listings(self):
        data = find_similar_listings_mongo("gross, disgusting, ugly")
        print(data)
        self.assertListEqual(data, [{'name': 'AMAZING Downtown Suite w/ HOT TUB,GYM,SAUNA, POOL', 'score': 1.520878721859114}, {'name': '开心果家庭旅馆', 'score': 1.0275362318840582}, {'name': 'Modern 1 bedroom 1 Den Parking Tinseltown Gastown', 'score': 1.0213260135135136}])


if __name__ == "__main__":
    unittest.main()
