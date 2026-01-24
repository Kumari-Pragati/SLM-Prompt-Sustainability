import unittest
from mbpp_159_code import month_season

class TestMonthSeason(unittest.TestCase):

    def test_winter_start(self):
        self.assertEqual(month_season('December', 1), 'winter')
        self.assertEqual(month_season('January', 31), 'winter')

    def test_winter_end(self):
        self.assertEqual(month_season('February', 28), 'winter')
        self.assertEqual(month_season('March', 19), 'winter')

    def test_spring_start(self):
        self.assertEqual(month_season('March', 20), 'spring')
        self.assertEqual(month_season('April', 1), 'spring')

    def test_spring_end(self):
        self.assertEqual(month_season('June', 20), 'spring')
        self.assertEqual(month_season('May', 31), 'spring')

    def test_summer_start(self):
        self.assertEqual(month_season('July', 1), 'summer')
        self.assertEqual(month_season('June', 21), 'summer')

    def test_summer_end(self):
        self.assertEqual(month_season('September', 30), 'summer')
        self.assertEqual(month_season('August', 31), 'summer')

    def test_autumn_start(self):
        self.assertEqual(month_season('September', 1), 'autumn')
        self.assertEqual(month_season('October', 1), 'autumn')

    def test_autumn_end(self):
        self.assertEqual(month_season('November', 30), 'autumn')
        self.assertEqual(month_season('December', 20), 'autumn')

    def test_invalid_month(self):
        self.assertNotEqual(month_season('Invalid', 1), 'winter')
        self.assertNotEqual(month_season('Invalid', 1), 'spring')
        self.assertNotEqual(month_season('Invalid', 1), 'summer')
        self.assertNotEqual(month_season('Invalid', 1), 'autumn')

    def test_invalid_days(self):
        self.assertNotEqual(month_season('January', -1), 'winter')
        self.assertNotEqual(month_season('January', 32), 'winter')
        self.assertNotEqual(month_season('January', 0), 'winter')
