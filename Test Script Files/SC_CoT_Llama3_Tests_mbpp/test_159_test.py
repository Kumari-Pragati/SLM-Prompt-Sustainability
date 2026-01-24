import unittest
from mbpp_159_code import month_season

class TestMonthSeason(unittest.TestCase):

    def test_winter(self):
        self.assertEqual(month_season('January', 1), 'winter')
        self.assertEqual(month_season('February', 28), 'winter')
        self.assertEqual(month_season('March', 1), 'winter')

    def test_spring(self):
        self.assertEqual(month_season('March', 20), 'winter')
        self.assertEqual(month_season('March', 20),'spring')
        self.assertEqual(month_season('April', 1),'spring')
        self.assertEqual(month_season('May', 31),'spring')
        self.assertEqual(month_season('June', 1),'spring')

    def test_summer(self):
        self.assertEqual(month_season('June', 21),'spring')
        self.assertEqual(month_season('June', 21),'summer')
        self.assertEqual(month_season('July', 1),'summer')
        self.assertEqual(month_season('August', 31),'summer')
        self.assertEqual(month_season('September', 1),'summer')

    def test_autumn(self):
        self.assertEqual(month_season('September', 22),'summer')
        self.assertEqual(month_season('September', 22), 'autumn')
        self.assertEqual(month_season('October', 1), 'autumn')
        self.assertEqual(month_season('November', 30), 'autumn')
        self.assertEqual(month_season('December', 1), 'autumn')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            month_season(1, 1)
        with self.assertRaises(TypeError):
            month_season('Invalid', 1)
        with self.assertRaises(TypeError):
            month_season('January', 'Invalid')
