import unittest
from mbpp_159_code import month_season

class TestMonthSeason(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(month_season('January', 1), 'winter')
        self.assertEqual(month_season('June', 20), 'summer')
        self.assertEqual(month_season('September', 22), 'autumn')

    def test_edge_cases(self):
        self.assertEqual(month_season('March', 20), 'spring')
        self.assertEqual(month_season('June', 19), 'spring')
        self.assertEqual(month_season('September', 20), 'summer')
        self.assertEqual(month_season('October', 21), 'autumn')
        self.assertEqual(month_season('November', 20), 'autumn')
        self.assertEqual(month_season('December', 19), 'winter')

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, month_season, 'Invalid Month', 1)
        self.assertRaises(ValueError, month_season, 'January', 32)
