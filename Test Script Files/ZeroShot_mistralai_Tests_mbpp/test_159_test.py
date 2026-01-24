import unittest
from mbpp_159_code import month_season

class TestMonthSeason(unittest.TestCase):

    def test_winter_months(self):
        self.assertEqual(month_season('January', 1), 'winter')
        self.assertEqual(month_season('February', 28), 'winter')
        self.assertEqual(month_season('March', 1), 'winter')

    def test_spring_months(self):
        self.assertEqual(month_season('April', 1), 'spring')
        self.assertEqual(month_season('May', 31), 'spring')
        self.assertEqual(month_season('June', 20), 'spring')

    def test_summer_months(self):
        self.assertEqual(month_season('July', 1), 'summer')
        self.assertEqual(month_season('August', 31), 'summer')
        self.assertEqual(month_season('September', 22), 'summer')
        self.assertEqual(month_season('September', 23), 'summer')
        self.assertEqual(month_season('September', 30), 'summer')
        self.assertEqual(month_season('September', 31), 'summer')
        self.assertEqual(month_season('August', 21), 'summer')

    def test_autumn_months(self):
        self.assertEqual(month_season('October', 1), 'autumn')
        self.assertEqual(month_season('October', 22), 'autumn')
        self.assertEqual(month_season('October', 31), 'autumn')
        self.assertEqual(month_season('November', 1), 'autumn')
        self.assertEqual(month_season('November', 21), 'autumn')
        self.assertEqual(month_season('November', 30), 'autumn')
        self.assertEqual(month_season('December', 1), 'autumn')
        self.assertEqual(month_season('December', 20), 'autumn')
