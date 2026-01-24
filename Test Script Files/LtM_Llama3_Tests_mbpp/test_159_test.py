import unittest
from mbpp_159_code import month_season

class TestMonthSeason(unittest.TestCase):
    def test_simple_winter(self):
        self.assertEqual(month_season('January', 1), 'winter')

    def test_simple_spring(self):
        self.assertEqual(month_season('April', 1),'spring')

    def test_simple_summer(self):
        self.assertEqual(month_season('July', 1),'summer')

    def test_simple_autumn(self):
        self.assertEqual(month_season('October', 1), 'autumn')

    def test_edge_case_march(self):
        self.assertEqual(month_season('March', 20),'spring')

    def test_edge_case_june(self):
        self.assertEqual(month_season('June', 21),'summer')

    def test_edge_case_september(self):
        self.assertEqual(month_season('September', 22), 'autumn')

    def test_edge_case_october(self):
        self.assertEqual(month_season('October', 22), 'autumn')

    def test_edge_case_november(self):
        self.assertEqual(month_season('November', 22), 'autumn')

    def test_edge_case_december(self):
        self.assertEqual(month_season('December', 20), 'winter')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            month_season(123, 1)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            month_season('January', 'abc')
