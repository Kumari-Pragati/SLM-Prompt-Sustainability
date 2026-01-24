import unittest
from mbpp_470_code import add_pairwise

class TestAddPairwise(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(add_pairwise((1, 2, 3, 4)), (3, 5, 7))

    def test_single_element(self):
        self.assertEqual(add_pairwise((1,)), ())

    def test_empty_tuple(self):
        self.assertEqual(add_pairwise(()), ())

    def test_large_tuple(self):
        self.assertEqual(add_pairwise(tuple(range(1, 1001))), tuple(range(3, 1002)))

    def test_negative_numbers(self):
        self.assertEqual(add_pairwise((-1, -2, -3, -4)), (-3, -5, -7))

    def test_zeroes(self):
        self.assertEqual(add_pairwise((0, 0, 0, 0)), (0, 0))

    def test_large_numbers(self):
        self.assertEqual(add_pairwise((1000000000, 2000000000, 3000000000)), (3000000000, 5000000000))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            add_pairwise(123)
        with self.assertRaises(TypeError):
            add_pairwise((1, 2, 'a'))
        with self.assertRaises(TypeError):
            add_pairwise((1, 2, None))
