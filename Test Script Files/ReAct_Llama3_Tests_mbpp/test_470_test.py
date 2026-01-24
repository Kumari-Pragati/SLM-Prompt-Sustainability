import unittest
from mbpp_470_code import add_pairwise

class TestAddPairwise(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(add_pairwise(()), ())

    def test_single_element_tuple(self):
        self.assertEqual(add_pairwise((1,)), ())

    def test_two_elements_tuple(self):
        self.assertEqual(add_pairwise((1, 2)), (3,))

    def test_three_elements_tuple(self):
        self.assertEqual(add_pairwise((1, 2, 3)), (4, 5))

    def test_even_length_tuple(self):
        self.assertEqual(add_pairwise((1, 2, 3, 4)), (3, 5, 7))

    def test_odd_length_tuple(self):
        self.assertEqual(add_pairwise((1, 2, 3, 4, 5)), (3, 5, 7, 8))

    def test_long_tuple(self):
        self.assertEqual(add_pairwise((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)), (3, 5, 7, 8, 9, 11, 12, 13, 14, 15))
