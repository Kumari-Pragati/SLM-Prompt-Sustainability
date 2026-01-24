import unittest
from mbpp_504_code import sum_Of_Series

class TestSumOfSeries(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(sum_Of_Series(1), 1)
        self.assertEqual(sum_Of_Series(2), 8)
        self.assertEqual(sum_Of_Series(3), 27)
        self.assertEqual(sum_Of_Series(4), 64)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_Of_Series(0), 0)
        self.assertEqual(sum_Of_Series(1000), 123456736)
        self.assertEqual(sum_Of_Series(100000), 1234567890123456736)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            sum_Of_Series(-1)
