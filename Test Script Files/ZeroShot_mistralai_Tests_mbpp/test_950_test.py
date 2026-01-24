import unittest
from mbpp_950_code import date
from datetime import timedelta
from 950_code import chinese_zodiac

class TestChineseZodiac(unittest.TestCase):

    def test_chinese_zodiac_valid_years(self):
        test_cases = [
            (2000, 'Rat'),
            (2001, 'Ox'),
            (2002, 'Tiger'),
            (2003, 'Rabbit'),
            (2004, 'Dragon'),
            (2005, 'Snake'),
            (2006, 'Horse'),
            (2007, 'Sheep'),
            (2008, 'Monkey'),
            (2009, 'Rooster'),
            (2010, 'Dog'),
            (2011, 'Pig'),
            (2012, 'Rat'),
            (2013, 'Ox'),
            (2014, 'Tiger'),
            (2015, 'Rabbit'),
            (2016, 'Dragon'),
            (2017, 'Snake'),
            (2018, 'Horse'),
            (2019, 'Sheep'),
            (2020, 'Monkey'),
            (2021, 'Rooster'),
            (2022, 'Dog'),
            (2023, 'Pig'),
            (2024, 'Rat'),
        ]

        for year, sign in test_cases:
            self.assertEqual(chinese_zodiac(year), sign)

    def test_chinese_zodiac_invalid_years(self):
        invalid_years = [
            -1000,
            1900,
            20010,
            2000.5,
            '2000',
            True,
            None,
        ]

        for year in invalid_years:
            with self.subTest(year=year):
                self.assertNotEqual(chinese_zodiac(year), None)
                self.assertNotEqual(chinese_zodiac(year), '')
                self.assertNotEqual(chinese_zodiac(year), 'Hare')

    def test_chinese_zodiac_edge_cases(self):
        edge_cases = [
            (1999, 'Rat'),
            (2000 - timedelta(days=1), 'Rat'),
            (2000 + timedelta(days=1), 'Rat'),
            (2001 - timedelta(days=364), 'Ox'),
            (2001 + timedelta(days=1), 'Ox'),
        ]

        for year, sign in edge_cases:
            self.assertEqual(chinese_zodiac(year), sign)
