import unittest
from mbpp_470_code import add_pairwise

class TestAddPairwise(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(add_pairwise((1, 2, 3, 4)), (3, 5, 7))

    def test_single_element(self):
        self.assertEqual(add_pairwise((1,)), ())

    def test_empty_tuple(self):
        self.assertEqual(add_pairwise(()), ())

    def test_negative_numbers(self):
        self.assertEqual(add_pairwise((-1, -2, -3, -4)), (-3, -5, -7))

    def test_zeroes(self):
        self.assertEqual(add_pairwise((0, 0, 0, 0)), (0, 0))

    def test_large_numbers(self):
        self.assertEqual(add_pairwise((1000, 2000, 3000)), (3000, 5000))

    def test_float_numbers(self):
        self.assertAlmostEqual(add_pairwise((1.1, 2.2, 3.3)), (3.3, 5.5))
