"""
This module tests all the functions in the package
"""
import unittest
import checker as c
import adding as a
import pandas as pd
import csv


class TestName(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        db = pd.DataFrame(pd.read_csv('people_birthday.csv'))
        index = db.loc[db["Person"] == "Albi"].index.values[0]
        db.drop(db.index[index], inplace=True)
        db.drop("Unnamed: 0", axis=1, inplace=True)
        db.to_csv("people_birthday.csv")

    def setUp(self):
        self.correct_p = "Valeria"
        self.db = pd.DataFrame(pd.read_csv('people_birthday.csv'))
        self.new_p = "Daniel"

    def test_check_person(self):
        self.assertTrue(c.check_person(self.correct_p))
        self.assertFalse(c.check_person(self.new_p))

    def test_return_birthday(self):
        string = '{}\'s birthday is {}.'
        lower_p = self.db["Person"].str.lower()
        c_lower = self.correct_p.lower()
        b = self.db["Birthday"]
        result1 = print(string.format(self.correct_p, b.loc[lower_p ==
                        c_lower()].values[0]))
        self.assertEqual(c.return_birthday(self.correct_p), result1)
        result2 = print('Sadly, we don\'t' +
                        ' have {}\'s birthday.'.format(self.new_p))
        self.assertEqual(c.return_birthday(self.new_p), result2)

    def test_print_birthdays(self):
        result = print(self.db)
        self.assertEqual(c.print_birthdays(), result)

    def test_add_person(self):
        res1 = print("sorry, but " + self.correct_p +
                     " is already present in the database, thank you anyway")
        self.assertEqual(a.add_person(self.correct_p), res1)
        res2 = print("Thank you for your contribution!")
        self.assertEqual(a.add_person("Albi"), res2)


if __name__ == "__main__":
    unittest.main()
