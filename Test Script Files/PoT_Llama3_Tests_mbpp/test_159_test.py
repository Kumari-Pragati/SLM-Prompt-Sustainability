import unittest
from mbpp_159_code import month_season

class TestMonthSeason(unittest.TestCase):

    def test_winter(self):
        self.assertEqual(month_season('January', 1), 'winter')

    def test_spring(self):
        self.assertEqual(month_season('April', 1),'spring')

    def test_summer(self):
        self.assertEqual(month_season('July', 1),'summer')

    def test_autumn(self):
        self.assertEqual(month_season('October', 1), 'autumn')

    def test_winter_long(self):
        self.assertEqual(month_season('December', 20), 'winter')

    def test_spring_long(self):
        self.assertEqual(month_season('March', 20),'spring')

    def test_summer_long(self):
        self.assertEqual(month_season('September', 20), 'autumn')

    def test_autumn_long(self):
        self.assertEqual(month_season('October', 20), 'autumn')

    def test_mixed(self):
        self.assertEqual(month_season('March', 22),'spring')

    def test_invalid_month(self):
        with self.assertRaises(TypeError):
            month_season('Invalid', 1)

    def test_invalid_days(self):
        with self.assertRaises(TypeError):
            month_season('January', 'Invalid')
