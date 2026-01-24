import unittest
from mbpp_504_code import sum_Of_Series

class TestSumOfSeries(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(sum_Of_Series(3), 36)

    def test_edge_case(self):
        self.assertEqual(sum_Of_Series(1), 1)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            sum_Of_Series(-1)

    def test_edge_case_zero(self):
        self.assertEqual(sum_Of_Series(0), 0)

    def test_edge_case_large(self):
        self.assertEqual(sum_Of_Series(100), 338350)

    def test_edge_case_large_negative(self):
        with self.assertRaises(TypeError):
            sum_Of_Series(-100)

    def test_edge_case_large_zero(self):
        self.assertEqual(sum_Of_Series(0), 0)

    def test_edge_case_large_negative_zero(self):
        with self.assertRaises(TypeError):
            sum_Of_Series(-0)
