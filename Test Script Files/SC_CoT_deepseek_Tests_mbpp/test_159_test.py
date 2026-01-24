import unittest
from mbpp_159_code import month_season

class TestMonthSeason(unittest.TestCase):

    def test_winter(self):
        self.assertEqual(month_season('December', 21), 'winter')
        self.assertEqual(month_season('December', 22), 'winter')
        self.assertEqual(month_season('December', 31), 'winter')
        self.assertEqual(month_season('January', 1), 'winter')
        self.assertEqual(month_season('January', 31), 'winter')
        self.assertEqual(month_season('February', 28), 'winter')
        self.assertEqual(month_season('February', 29), 'winter')

    def test_spring(self):
        self.assertEqual(month_season('March', 20), 'spring')
        self.assertEqual(month_season('March', 21), 'spring')
        self.assertEqual(month_season('March', 31), 'spring')
        self.assertEqual(month_season('April', 1), 'spring')
        self.assertEqual(month_season('April', 30), 'spring')
        self.assertEqual(month_season('May', 31), 'spring')
        self.assertEqual(month_season('June', 21), 'spring')
        self.assertEqual(month_season('June', 22), 'spring')

    def test_summer(self):
        self.assertEqual(month_season('July', 21), 'summer')
        self.assertEqual(month_season('July', 22), 'summer')
        self.assertEqual(month_season('July', 31), 'summer')
        self.assertEqual(month_season('August', 1), 'summer')
        self.assertEqual(month_season('August', 31), 'summer')
        self.assertEqual(month_season('September', 21), 'summer')
        self.assertEqual(month_season('September', 22), 'summer')

    def test_autumn(self):
        self.assertEqual(month_season('October', 22), 'autumn')
        self.assertEqual(month_season('October', 31), 'autumn')
        self.assertEqual(month_season('November', 1), 'autumn')
        self.assertEqual(month_season('November', 30), 'autumn')
        self.assertEqual(month_season('December', 20), 'autumn')
        self.assertEqual(month_season('December', 21), 'autumn')

    def test_invalid_month(self):
        with self.assertRaises(Exception):
            month_season('InvalidMonth', 1)

    def test_invalid_day(self):
        with self.assertRaises(Exception):
            month_season('January', 0)
        with self.assertRaises(Exception):
            month_season('January', 32)
