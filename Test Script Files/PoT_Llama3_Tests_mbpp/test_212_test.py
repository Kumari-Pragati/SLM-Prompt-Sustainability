import unittest
from mbpp_212_code import fourth_Power_Sum

class TestFourthPowerSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(fourth_Power_Sum(3), 625)

    def test_edge_case(self):
        self.assertEqual(fourth_Power_Sum(1), 1)
        self.assertEqual(fourth_Power_Sum(0), 0)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            fourth_Power_Sum(-1)

    def test_edge_case_non_integer(self):
        with self.assertRaises(TypeError):
            fourth_Power_Sum(3.5)

    def test_edge_case_large(self):
        self.assertEqual(fourth_Power_Sum(100), 100000000000)

    def test_edge_case_zero(self):
        self.assertEqual(fourth_Power_Sum(0), 0)
