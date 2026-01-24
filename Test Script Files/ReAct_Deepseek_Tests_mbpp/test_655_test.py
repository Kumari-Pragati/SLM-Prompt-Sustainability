import unittest
from mbpp_655_code import fifth_Power_Sum

class TestFifthPowerSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(fifth_Power_Sum(5), 4455)

    def test_boundary_case_1(self):
        self.assertEqual(fifth_Power_Sum(0), 0)

    def test_boundary_case_2(self):
        self.assertEqual(fifth_Power_Sum(1), 1)

    def test_large_number(self):
        self.assertEqual(fifth_Power_Sum(10), 30250)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            fifth_Power_Sum(-5)
