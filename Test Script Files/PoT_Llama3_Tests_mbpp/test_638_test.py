import unittest
from mbpp_638_code import wind_chill

class TestWindChill(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(wind_chill(15, 0), 13)

    def test_edge_case_v_zero(self):
        self.assertEqual(wind_chill(0, 0), 13)

    def test_edge_case_t_zero(self):
        self.assertEqual(wind_chill(15, 0), 13)

    def test_edge_case_v_high(self):
        self.assertEqual(wind_chill(30, 0), 0)

    def test_edge_case_t_high(self):
        self.assertEqual(wind_chill(15, 50), 0)

    def test_edge_case_v_zero_t_high(self):
        self.assertEqual(wind_chill(0, 50), 0)

    def test_edge_case_t_zero_v_high(self):
        self.assertEqual(wind_chill(30, 0), 0)

    def test_edge_case_v_zero_t_zero(self):
        self.assertEqual(wind_chill(0, 0), 13)

    def test_edge_case_t_zero_v_high(self):
        self.assertEqual(wind_chill(30, 0), 0)

    def test_edge_case_v_zero_t_high(self):
        self.assertEqual(wind_chill(0, 50), 0)

    def test_edge_case_t_zero_v_zero(self):
        self.assertEqual(wind_chill(0, 0), 13)

    def test_edge_case_v_high_t_zero(self):
        self.assertEqual(wind_chill(30, 0), 0)

    def test_edge_case_v_high_t_high(self):
        self.assertEqual(wind_chill(30, 50), 0)

    def test_edge_case_t_high_v_zero(self):
        self.assertEqual(wind_chill(0, 50), 0)

    def test_edge_case_t_high_v_high(self):
        self.assertEqual(wind_chill(30, 50), 0)

    def test_edge_case_v_zero_t_high_v_zero(self):
        self.assertEqual(wind_chill(0, 50, 0), 0)

    def test_edge_case_t_zero_v_high_v_zero(self):
        self.assertEqual(wind_chill(0, 0, 0), 13)

    def test_edge_case_t_zero_v_zero_v_zero(self):
        self.assertEqual(wind_chill(0, 0, 0), 13)

    def test_edge_case_v_zero_t_zero_v_zero(self):
        self.assertEqual(wind_chill(0, 0, 0), 13)

    def test_edge_case_v_high_t_zero_v_zero(self):
        self.assertEqual(wind_chill(0, 0, 0), 13)

    def test_edge_case_v_high_t_high_v_zero(self):
        self.assertEqual(wind_chill(0, 50, 0), 0)

    def test_edge_case_t_high_v_zero_v_zero(self):
        self.assertEqual(wind_chill(0, 0, 0), 13)

    def test_edge_case_t_high_v_high_v_zero(self):
        self.assertEqual(wind_chill(0, 50, 0), 0)
