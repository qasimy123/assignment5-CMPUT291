import unittest
from A5T8MongoDB import find_recent_review as find_recent_review_mongo
from A5T8SQLite import find_recent_review as find_recent_review_sqlite, find_listing
from A5T9MongoDB import find_similar_listings as find_similar_listings_mongo
from A5T3MongoDB import task3 as task3Mongo
from A5T4MongoDB import task4 as task4Mongo
from A5T5MongoDB import task5 as task5Mongo
from A5T3SQLite import task3 as task3SQLite
from A5T4SQLite import task4 as task4SQLite
from A5T5SQLite import task5 as task5SQLite

COMPARE = [{'host_name': 'Chris', 'price': 150, 'reviews': {'comments': 'Am Tag unserer Abreise nach Vancouver erhielten wir von Chris die Nachricht, dass sie uns das von uns gemietete Apartment nicht überlassen kann aufgrund eines Wasserschadens.\nEine sehr unglückliche Situation, die aber eintreten kann. Chris hat sich mit unglaublichem Einsatz innerhalt von 24 Stunden darum bemüht, eine Ersatzunterkunft zu finden, was sehr schwierig war. So kamen wir in Vancouver an und hatten eine Unterkunft auch wenn es nicht wie erwartet war. Aber wir haben uns einigen können und anerkennen sehr, wie Chris sich für uns eingesetzt hat. Das war sicherlich nicht selbstverständlich.\nTrotz aller Unannehmlichkeiten am Anfang haben wir einen positiven Eindruck erhalten.'}}]
COMPARE_T4 = [{'id': 48098921}, {'id': 48098117}, {'id': 48097994}, {'id': 48097843}, {'id': 48097732}, {
    'id': 48097059}, {'id': 48096556}, {'id': 48096018}, {'id': 48094016}, {'id': 48093848}]


class A5T3MongoTest(unittest.TestCase):
    def test_task3(self):
        data = task3Mongo()

        self.assertListEqual([{'_id': 387534175, 'owned listings': 1}, {'_id': 387479643, 'owned listings': 1}, {'_id': 387417330, 'owned listings': 1}, {'_id': 387174737, 'owned listings': 1}, {'_id': 387085697, 'owned listings': 1}, {
                             '_id': 386957559, 'owned listings': 1}, {'_id': 386771273, 'owned listings': 1}, {'_id': 385285505, 'owned listings': 1}, {'_id': 385119280, 'owned listings': 9}, {'_id': 384900596, 'owned listings': 2}], data)


class A5T3SQLiteTest(unittest.TestCase):
    def test_task3(self):
        data = task3SQLite()

        self.assertListEqual([(387534175, 1), (387479643, 1), (387417330, 1), (387174737, 1), (
            387085697, 1), (386957559, 1), (386771273, 1), (385285505, 1), (385119280, 9), (384900596, 2)], data)


class A5T4MongoTest(unittest.TestCase):
    def test_task4(self):
        data = task4Mongo()
        self.assertListEqual(COMPARE_T4, list(data))


class A5T4SQLiteTest(unittest.TestCase):
    def test_task4(self):
        data = task4SQLite()

        self.assertListEqual([(48098921,), (48098117,), (48097994,), (48097843,), (
            48097732,), (48097059,), (48096556,), (48096018,), (48094016,), (48093848,)], data)


class A5T5MongoTest(unittest.TestCase):
    def test_task5(self):
        data = task5Mongo("Downtown")

        self.assertListEqual(
            [{'_id': 'null', 'avg': 160.59687228496958}], data)


class A5T5QLiteTest(unittest.TestCase):
    def test_task5(self):
        data = task5SQLite("Downtown")
        self.assertListEqual([(160.6,)], data)


class A5T8MongoTest(unittest.TestCase):
    def test_find_recent_review(self):
        data = find_recent_review_mongo(22128)
        self.assertListEqual(COMPARE, data)


class A5T8SQLiteTest(unittest.TestCase):
    def test_find_recent_review(self):
        data = find_recent_review_sqlite(22128)
        self.assertTupleEqual(('Am Tag unserer Abreise nach Vancouver erhielten wir von Chris die Nachricht, dass sie uns das von uns gemietete Apartment nicht überlassen kann aufgrund eines Wasserschadens.\nEine sehr unglückliche Situation, die aber eintreten kann. Chris hat sich mit unglaublichem Einsatz innerhalt von 24 Stunden darum bemüht, eine Ersatzunterkunft zu finden, was sehr schwierig war. So kamen wir in Vancouver an und hatten eine Unterkunft auch wenn es nicht wie erwartet war. Aber wir haben uns einigen können und anerkennen sehr, wie Chris sich für uns eingesetzt hat. Das war sicherlich nicht selbstverständlich.\nTrotz aller Unannehmlichkeiten am Anfang haben wir einen positiven Eindruck erhalten.',), data)

    def test_find_listing_host_and_price(self):
        data = find_listing(22128)
        self.assertTupleEqual(('Chris', 150), data)


class A5T9MongoDBTest(unittest.TestCase):
    def test_find_similar_listings(self):
        data = find_similar_listings_mongo("gross, disgusting, ugly")
        self.assertListEqual(data, [{'id': 42755867, 'name': 'AMAZING Downtown Suite w/ HOT TUB,GYM,SAUNA, POOL', 'score': 1.520878721859114}, {'id': 23949937,
                                                                                                                                                'name': '开心果家庭旅馆', 'score': 1.0275362318840582}, {'id': 5347437, 'name': 'Modern 1 bedroom 1 Den Parking Tinseltown Gastown', 'score': 1.0213260135135136}])


if __name__ == "__main__":
    unittest.main()
