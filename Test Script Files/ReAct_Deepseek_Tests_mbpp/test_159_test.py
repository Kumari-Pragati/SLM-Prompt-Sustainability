import unittest
from mbpp_159_code import month_season

class TestMonthSeason(unittest.TestCase):

    def test_winter_months(self):
        self.assertEqual(month_season('December', 21), 'winter')
        self.assertEqual(month_season('January', 20), 'winter')
        self.assertEqual(month_season('February', 20), 'winter')
        self.assertEqual(month_season('March', 20), 'winter')

    def test_spring_months(self):
        self.assertEqual(month_season('March', 20), 'spring')
        self.assertEqual(month_season('March', 21), 'spring')
        self.assertEqual(month_season('April', 20), 'spring')
        self.assertEqual(month_season('May', 20), 'spring')
        self.assertEqual(month_season('June', 21), 'spring')

    def test_summer_months(self):
        self.assertEqual(month_season('June', 21), 'summer')
        self.assertEqual(month_season('July', 20), 'summer')
        self.assertEqual(month_season('August', 20), 'summer')
        self.assertEqual(month_season('September', 21), 'summer')

    def test_autumn_months(self):
        self.assertEqual(month_season('September', 21), 'autumn')
        self.assertEqual(month_season('October', 21), 'autumn')
        self.assertEqual(month_season('November', 21), 'autumn')
        self.assertEqual(month_season('December', 20), 'autumn')

    def test_invalid_month(self):
        with self.assertRaises(AssertionError):
            month_season('InvalidMonth', 20)

    def test_invalid_day(self):
        with self.assertRaises(AssertionError):
            month_season('March', -1)
        with self.assertRaises(AssertionError):
            month_season('March', 32)
