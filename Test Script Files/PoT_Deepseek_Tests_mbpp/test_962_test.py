import unittest
from mbpp_962_code import sum_Even

class TestSumEven(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_Even(2, 10), 24)

    def test_edge_case_with_even_range(self):
        self.assertEqual(sum_Even(2, 12), 30)

    def test_boundary_case_with_odd_range(self):
        self.assertEqual(sum_Even(1, 1), 0)

    def test_boundary_case_with_large_range(self):
        self.assertEqual(sum_Even(1, 1000000), 250000250000)

    def test_invalid_input_range(self):
        with self.assertRaises(Exception):
            sum_Even(10, 2)

    def test_invalid_input_type(self):
        with self.assertRaises(Exception):
            sum_Even("a", 10)
