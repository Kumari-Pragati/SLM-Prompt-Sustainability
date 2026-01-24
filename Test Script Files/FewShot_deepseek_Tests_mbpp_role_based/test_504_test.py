import unittest
from mbpp_504_code import sum_Of_Series

class TestSumOfSeries(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sum_Of_Series(5), 225)

    def test_boundary_conditions(self):
        self.assertEqual(sum_Of_Series(0), 0)
        self.assertEqual(sum_Of_Series(1), 1)

    def test_large_number(self):
        self.assertEqual(sum_Of_Series(100), 495050)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            sum_Of_Series(-5)
