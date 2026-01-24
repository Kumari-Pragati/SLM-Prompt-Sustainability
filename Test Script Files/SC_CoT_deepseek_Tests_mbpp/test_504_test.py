import unittest

from mbpp_504_code import sum_Of_Series

class TestSumOfSeries(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_Of_Series(5), 225)

    def test_boundary_case(self):
        self.assertEqual(sum_Of_Series(1), 1)

    def test_edge_case(self):
        self.assertEqual(sum_Of_Series(0), 0)

    def test_negative_input(self):
        with self.assertRaises(Exception):
            sum_Of_Series(-5)

    def test_non_integer_input(self):
        with self.assertRaises(Exception):
            sum_Of_Series(2.5)

    def test_large_input(self):
        self.assertEqual(sum_Of_Series(100), 5050050)
