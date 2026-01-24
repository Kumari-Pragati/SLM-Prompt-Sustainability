import unittest
from mbpp_159_code import month_season

class TestMonthSeason(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(month_season('January', 30), 'winter')
        self.assertEqual(month_season('February', 28), 'winter')
        self.assertEqual(month_season('March', 20), 'winter')
        self.assertEqual(month_season('April', 30), 'spring')
        self.assertEqual(month_season('May', 31), 'spring')
        self.assertEqual(month_season('June', 20), 'spring')
        self.assertEqual(month_season('July', 31), 'summer')
        self.assertEqual(month_season('August', 31), 'summer')
        self.assertEqual(month_season('September', 20), 'summer')
        self.assertEqual(month_season('October', 31), 'autumn')
        self.assertEqual(month_season('November', 30), 'autumn')
        self.assertEqual(month_season('December', 29), 'autumn')

    def test_edge_cases(self):
        self.assertEqual(month_season('January', 0), 'winter')
        self.assertEqual(month_season('February', 30), 'winter')
        self.assertEqual(month_season('March', 19), 'winter')
        self.assertEqual(month_season('March', 20), 'spring')
        self.assertEqual(month_season('June', 21), 'summer')
        self.assertEqual(month_season('June', 22), 'summer')
        self.assertEqual(month_season('September', 21), 'autumn')
        self.assertEqual(month_season('September', 22), 'autumn')
        self.assertEqual(month_season('October', 22), 'winter')
        self.assertEqual(month_season('November', 31), 'winter')
        self.assertEqual(month_season('December', 21), 'winter')
        self.assertEqual(month_season('December', 22), 'winter')

    def test_complex_cases(self):
        self.assertEqual(month_season('March', 21), 'spring')
        self.assertEqual(month_season('June', 22), 'summer')
        self.assertEqual(month_season('September', 22), 'autumn')
        self.assertEqual(month_season('October', 21), 'autumn')
        self.assertEqual(month_season('November', 21), 'autumn')
        self.assertEqual(month_season('December', 20), 'winter')
