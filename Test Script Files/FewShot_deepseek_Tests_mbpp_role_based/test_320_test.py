import unittest
from mbpp_320_code import sum_difference

class TestSumDifference(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_difference(5), 110)

    def test_boundary_conditions(self):
        self.assertEqual(sum_difference(1), 0)
        self.assertEqual(sum_difference(0), 0)

    def test_large_number(self):
        self.assertGreater(sum_difference(100), 0)

    def test_negative_number(self):
        with self.assertRaises(Exception):
            sum_difference(-5)
