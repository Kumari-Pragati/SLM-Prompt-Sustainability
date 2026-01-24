import unittest
from mbpp_638_code import wind_chill

class TestWindChill(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(wind_chill(20, 0), 13)

    def test_edge_case_low_temp(self):
        self.assertEqual(wind_chill(20, -20), -45)

    def test_edge_case_high_temp(self):
        self.assertEqual(wind_chill(20, 50), 13)

    def test_edge_case_low_wind(self):
        self.assertEqual(wind_chill(5, 0), 13)

    def test_edge_case_high_wind(self):
        self.assertEqual(wind_chill(50, 0), -45)

    def test_edge_case_zero_wind(self):
        self.assertEqual(wind_chill(0, 0), 13)

    def test_edge_case_zero_temp(self):
        self.assertEqual(wind_chill(20, 0), 13)

    def test_edge_case_negative_wind(self):
        with self.assertRaises(TypeError):
            wind_chill(-20, 0)

    def test_edge_case_negative_temp(self):
        with self.assertRaises(TypeError):
            wind_chill(20, -20)

    def test_edge_case_non_numeric_input(self):
        with self.assertRaises(TypeError):
            wind_chill('20', 0)

    def test_edge_case_non_numeric_input2(self):
        with self.assertRaises(TypeError):
            wind_chill(20, '0')
