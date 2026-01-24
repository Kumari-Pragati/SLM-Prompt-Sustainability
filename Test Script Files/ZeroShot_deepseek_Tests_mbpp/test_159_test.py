import unittest
from mbpp_159_code import month_season

class TestMonthSeason(unittest.TestCase):

    def test_winter(self):
        self.assertEqual(month_season('December', 21), 'winter')
        self.assertEqual(month_season('January', 20), 'winter')
        self.assertEqual(month_season('February', 19), 'winter')

    def test_spring(self):
        self.assertEqual(month_season('March', 20), 'spring')
        self.assertEqual(month_season('April', 21), 'spring')
        self.assertEqual(month_season('May', 22), 'spring')

    def test_summer(self):
        self.assertEqual(month_season('June', 21), 'summer')
        self.assertEqual(month_season('July', 22), 'summer')
        self.assertEqual(month_season('August', 23), 'summer')

    def test_autumn(self):
        self.assertEqual(month_season('September', 22), 'autumn')
        self.assertEqual(month_season('October', 23), 'autumn')
        self.assertEqual(month_season('November', 24), 'autumn')

    def test_invalid_month(self):
        with self.assertRaises(ValueError):
            month_season('InvalidMonth', 15)

    def test_invalid_day(self):
        with self.assertRaises(ValueError):
            month_season('March', -5)
