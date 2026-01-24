import unittest
from mbpp_504_code import sum_Of_Series

class TestSumOfSeries(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_Of_Series(1), 1)
        self.assertEqual(sum_Of_Series(2), 8)
        self.assertEqual(sum_Of_Series(3), 33)
        self.assertEqual(sum_Of_Series(4), 125)
        self.assertEqual(sum_Of_Series(5), 293)

    def test_edge_case(self):
        self.assertEqual(sum_Of_Series(0), 0)
        self.assertEqual(sum_Of_Series(1000), 1000000000)

    def test_boundary_case(self):
        self.assertEqual(sum_Of_Series(10), 10000)
        self.assertEqual(sum_Of_Series(100), 10000000)
        self.assertEqual(sum_Of_Series(1000), 10000000000)
