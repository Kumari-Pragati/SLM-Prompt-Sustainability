import unittest
from mbpp_159_code import month_season

class TestMonthSeason(unittest.TestCase):
    def test_winter_months(self):
        self.assertEqual(month_season('January', 31), 'winter')
        self.assertEqual(month_season('February', 28), 'winter')
        self.assertEqual(month_season('March', 19), 'winter')

    def test_spring_months(self):
        self.assertEqual(month_season('April', 30), 'spring')
        self.assertEqual(month_season('May', 31), 'spring')
        self.assertEqual(month_season('June', 20), 'spring')
        self.assertEqual(month_season('June', 21), 'summer')

    def test_summer_months(self):
        self.assertEqual(month_season('July', 31), 'summer')
        self.assertEqual(month_season('August', 31), 'summer')
        self.assertEqual(month_season('September', 21), 'summer')
        self.assertEqual(month_season('September', 22), 'autumn')

    def test_autumn_months(self):
        self.assertEqual(month_season('October', 22), 'autumn')
        self.assertEqual(month_season('November', 21), 'autumn')
        self.assertEqual(month_season('December', 20), 'autumn')
        self.assertEqual(month_season('December', 21), 'winter')

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, lambda: month_season('Invalid Month', 30))
        self.assertRaises(ValueError, lambda: month_season('January', -1))
        self.assertRaises(ValueError, lambda: month_season('January', 32))
