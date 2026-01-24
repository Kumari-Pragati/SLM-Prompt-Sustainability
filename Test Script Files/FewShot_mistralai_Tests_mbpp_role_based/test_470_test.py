import unittest
from mbpp_470_code import add_pairwise

class TestAddPairwise(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add_pairwise((1, 2, 3, 4)), (3, 5, 6))

    def test_zero(self):
        self.assertEqual(add_pairwise((0, 0, 0, 0)), (0, 0, 0))

    def test_negative_numbers(self):
        self.assertEqual(add_pairwise((-1, -2, -3, -4)), (-3, -5, -6))

    def test_single_element(self):
        self.assertEqual(add_pairwise((1)), (1,))

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            add_pairwise([])
