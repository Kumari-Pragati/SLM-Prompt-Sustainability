import unittest
from mbpp_504_code import sum_Of_Series

class TestSumOfSeries(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_Of_Series(5), 440)

    def test_edge_case_zero(self):
        self.assertEqual(sum_Of_Series(0), 0)

    def test_edge_case_negative(self):
        with self.assertRaises(ValueError):
            sum_Of_Series(-5)

    def test_edge_case_large_number(self):
        self.assertEqual(sum_Of_Series(1000), 25025000)
