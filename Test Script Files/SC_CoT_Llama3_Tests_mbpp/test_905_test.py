import unittest
from mbpp_905_code import sum_of_square

class TestSumOfSquare(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(sum_of_square(2), 20)

    def test_edge_case_n_zero(self):
        with self.assertRaises(ValueError):
            sum_of_square(0)

    def test_edge_case_n_one(self):
        self.assertEqual(sum_of_square(1), 1)

    def test_edge_case_n_negative(self):
        with self.assertRaises(ValueError):
            sum_of_square(-1)

    def test_edge_case_n_large(self):
        self.assertEqual(sum_of_square(10), 385)

    def test_edge_case_n_half(self):
        self.assertEqual(sum_of_square(5), 385)

    def test_edge_case_n_zero_and_half(self):
        with self.assertRaises(ValueError):
            sum_of_square(0.5)

    def test_edge_case_n_non_integer(self):
        with self.assertRaises(TypeError):
            sum_of_square(2.5)
