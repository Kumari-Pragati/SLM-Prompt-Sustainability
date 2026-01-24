import unittest
from mbpp_159_code import month_season

class TestMonthSeason(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(month_season('January', 31), 'winter')
        self.assertEqual(month_season('June', 20), 'spring')
        self.assertEqual(month_season('September', 22), 'summer')
        self.assertEqual(month_season('October', 30), 'autumn')
        self.assertEqual(month_season('December', 25), 'winter')

    def test_edge_cases(self):
        self.assertEqual(month_season('March', 20), 'winter')
        self.assertEqual(month_season('March', 19), 'winter')
        self.assertEqual(month_season('June', 21), 'summer')
        self.assertEqual(month_season('June', 22), 'summer')
        self.assertEqual(month_season('September', 20), 'summer')
        self.assertEqual(month_season('September', 21), 'summer')
        self.assertEqual(month_season('October', 20), 'autumn')
        self.assertEqual(month_season('October', 21), 'autumn')
        self.assertEqual(month_season('November', 20), 'autumn')
        self.assertEqual(month_season('November', 21), 'autumn')
        self.assertEqual(month_season('December', 21), 'winter')
        self.assertEqual(month_season('December', 22), 'winter')

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, month_season, 'Invalid Month', 30)
        self.assertRaises(ValueError, month_season, 'January', 32)
        self.assertRaises(ValueError, month_season, None, 30)
