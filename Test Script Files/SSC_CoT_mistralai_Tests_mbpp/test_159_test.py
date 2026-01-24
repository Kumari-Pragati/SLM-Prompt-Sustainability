import unittest
from mbpp_159_code import datetime, timedelta
from 159_code import month_season

class TestMonthSeason(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(month_season('January', 31), 'winter')
        self.assertEqual(month_season('June', 20), 'spring')
        self.assertEqual(month_season('September', 22), 'summer')
        self.assertEqual(month_season('December', 29), 'winter')

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(month_season('March', 20), 'winter')
        self.assertEqual(month_season('March', 19), 'winter')
        self.assertEqual(month_season('March', 21), 'spring')
        self.assertEqual(month_season('June', 19), 'spring')
        self.assertEqual(month_season('June', 21), 'summer')
        self.assertEqual(month_season('September', 20), 'summer')
        self.assertEqual(month_season('September', 22), 'autumn')
        self.assertEqual(month_season('September', 23), 'autumn')
        self.assertEqual(month_season('October', 20), 'autumn')
        self.assertEqual(month_season('October', 22), 'autumn')
        self.assertEqual(month_season('October', 23), 'autumn')
        self.assertEqual(month_season('November', 20), 'autumn')
        self.assertEqual(month_season('November', 21), 'autumn')
        self.assertEqual(month_season('November', 22), 'autumn')
        self.assertEqual(month_season('November', 23), 'autumn')
        self.assertEqual(month_season('December', 20), 'winter')
        self.assertEqual(month_season('December', 21), 'winter')
        self.assertEqual(month_season('December', 19), 'winter')

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, lambda: month_season('invalid_month', 30))
        self.assertRaises(ValueError, lambda: month_season('January', 32))
        self.assertRaises(ValueError, lambda: month_season('February', 29))
        self.assertRaises(TypeError, lambda: month_season(123, 30))
        self.assertRaises(TypeError, lambda: month_season('January', 3.14))
