import unittest
from mbpp_445_code import index_multiplication

class TestIndexMultiplication(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(index_multiplication((1, 2, 3), (4, 5, 6)), ((4, 10, 18)))
        self.assertEqual(index_multiplication((0, 2, 4), (1, 3, 5)), ((0, 6, 20)))

    def test_zero(self):
        self.assertEqual(index_multiplication((0, 0, 0), (0, 0, 0)), ((0, 0, 0)))

    def test_negative_numbers(self):
        self.assertEqual(index_multiplication((-1, -2, -3), (-4, -5, -6)), ((4, 10, 18)))
        self.assertEqual(index_multiplication((-0, -2, -4), (-1, -3, -5)), ((0, 6, 20)))

    def test_mixed_numbers(self):
        self.assertEqual(index_multiplication((1, -2, 3), (4, -5, 6)), ((4, 10, 18)))
        self.assertEqual(index_multiplication((-1, 2, -3), (4, 5, 6)), ((-4, 10, -18)))

    def test_empty_tuples(self):
        self.assertEqual(index_multiplication((), ()), ())
        self.assertEqual(index_multiplication((1,), ()), ())
        self.assertEqual(index_multiplication((), (1,)) , ())

    def test_single_element_tuples(self):
        self.assertEqual(index_multiplication((1,), (2,)), ((2,)))
        self.assertEqual(index_multiplication((2,), (1,)), ((2,)))
