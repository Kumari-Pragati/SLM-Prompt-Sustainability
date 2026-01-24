import unittest
from mbpp_950_code import date, timedelta

class TestChineseZodiac(unittest.TestCase):

    def test_typical_cases(self):
        years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012]
        expected_signs = ['Dragon', 'Snake', 'Horse', 'Sheep', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Hare', 'Dragon']
        for year, sign in zip(years, expected_signs):
            self.assertEqual(chinese_zodiac(year), sign)

    def test_edge_and_boundary_cases(self):
        # Edge cases:
        self.assertEqual(chinese_zodiac(1999), 'Dragon')
        self.assertEqual(chinese_zodiac(2013), 'Snake')
        self.assertEqual(chinese_zodiac(2021), 'Tiger')
        self.assertEqual(chinese_zodiac(2022), 'Hare')
        self.assertEqual(chinese_zodiac(2023), 'Dragon')

        # Boundary cases:
        self.assertEqual(chinese_zodiac(2000 - 1), 'Hare')
        self.assertEqual(chinese_zodiac(2000 + 1), 'Dragon')
        self.assertEqual(chinese_zodiac(2012 + 1), 'Dragon')
        self.assertEqual(chinese_zodiac(2012 - 1), 'Tiger')
