import unittest
from A5T8MongoDB import find_recent_review as find_recent_review_mongo
from A5T8SQLite import find_recent_review as find_recent_review_sqlite

COMPARE = [{'host_name': 'Chris', 'price': 150, 'reviews': {'comments': 'Am Tag unserer Abreise nach Vancouver erhielten wir von Chris die Nachricht, dass sie uns das von uns gemietete Apartment nicht überlassen kann aufgrund eines Wasserschadens.\nEine sehr unglückliche Situation, die aber eintreten kann. Chris hat sich mit unglaublichem Einsatz innerhalt von 24 Stunden darum bemüht, eine Ersatzunterkunft zu finden, was sehr schwierig war. So kamen wir in Vancouver an und hatten eine Unterkunft auch wenn es nicht wie erwartet war. Aber wir haben uns einigen können und anerkennen sehr, wie Chris sich für uns eingesetzt hat. Das war sicherlich nicht selbstverständlich.\nTrotz aller Unannehmlichkeiten am Anfang haben wir einen positiven Eindruck erhalten.'}}]


class A5T8MongoTest(unittest.TestCase):
    def test_find_recent_review(self):
        data = find_recent_review_mongo(22128)
        self.assertListEqual(COMPARE, data)


class A5T8SQLiteTest(unittest.TestCase):
    def test_find_recent_review(self):
        data = find_recent_review_sqlite(22128)
        self.assertTupleEqual(('Chris', 150, 'Am Tag unserer Abreise nach Vancouver erhielten wir von Chris die Nachricht, dass sie uns das von uns gemietete Apartment nicht überlassen kann aufgrund eines Wasserschadens.\nEine sehr unglückliche Situation, die aber eintreten kann. Chris hat sich mit unglaublichem Einsatz innerhalt von 24 Stunden darum bemüht, eine Ersatzunterkunft zu finden, was sehr schwierig war. So kamen wir in Vancouver an und hatten eine Unterkunft auch wenn es nicht wie erwartet war. Aber wir haben uns einigen können und anerkennen sehr, wie Chris sich für uns eingesetzt hat. Das war sicherlich nicht selbstverständlich.\nTrotz aller Unannehmlichkeiten am Anfang haben wir einen positiven Eindruck erhalten.'), data)


if __name__ == "__main__":
    unittest.main()
