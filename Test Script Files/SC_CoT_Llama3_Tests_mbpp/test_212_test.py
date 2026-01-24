import unittest
from mbpp_212_code import fourth_Power_Sum

class TestFourthPowerSum(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(fourth_Power_Sum(5), 6250)

    def test_edge_case_n_1(self):
        self.assertEqual(fourth_Power_Sum(1), 1)

    def test_edge_case_n_0(self):
        self.assertEqual(fourth_Power_Sum(0), 0)

    def test_edge_case_n_negative(self):
        with self.assertRaises(TypeError):
            fourth_Power_Sum(-1)

    def test_edge_case_n_non_integer(self):
        with self.assertRaises(TypeError):
            fourth_Power_Sum(3.5)

    def test_large_input(self):
        self.assertEqual(fourth_Power_Sum(100), 100100100100)

    def test_zero_input(self):
        self.assertEqual(fourth_Power_Sum(0), 0)
