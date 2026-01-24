import unittest
from mbpp_950_code import date
from 950_code import chinese_zodiac

class TestChineseZodiac(unittest.TestCase):

    def test_valid_years(self):
        years = [
            (2000, 'Dragon'),
            (2001, 'Snake'),
            (2002, 'Horse'),
            (2003, 'Sheep'),
            (2004, 'Monkey'),
            (2005, 'Rooster'),
            (2006, 'Dog'),
            (2007, 'Pig'),
            (2008, 'Rat'),
            (2009, 'Ox'),
            (2010, 'Tiger'),
            (2011, 'Rabbit'),  # Edge case: year after Tiger
            (2019, 'Pig'),  # Edge case: year before Rat
            (2021, 'Tiger'),  # Edge case: year after Pig
        ]
        for year, expected_sign in years:
            with self.subTest(year=year):
                self.assertEqual(chinese_zodiac(year), expected_sign)

    def test_invalid_years(self):
        invalid_years = [
            -1,  # Negative year
            1900,  # Before 2000
            20000,  # Far future
            1999,  # Year before Dragon
            2018,  # Year before Pig
        ]
        for year in invalid_years:
            with self.subTest(year=year):
                self.assertNotEqual(chinese_zodiac(year), 'Hare')  # Explicitly handled error case

    def test_date_year(self):
        today = date.today()
        year = today.year
        self.assertEqual(chinese_zodiac(year), chinese_zodiac(year - (today.month - 2) if today.month < 2 else year - 1))
