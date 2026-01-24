import unittest
from mbpp_308_code import large_product

class TestLargeProduct(unittest.TestCase):

    def test_large_product(self):
        self.assertEqual(large_product([1, 2, 3], [4, 5, 6], 3), [12, 11, 9])
        self.assertEqual(large_product([-1, 2, 3], [4, 5, 6], 3), [12, 11, 9])
        self.assertEqual(large_product([-1, -2, 3], [4, 5, 6], 3), [12, 11, 9])
        self.assertEqual(large_product([1, 2, 3], [-4, -5, -6], 3), [12, 11, 9])
        self.assertEqual(large_product([-1, -2, -3], [-4, -5, -6], 3), [-12, -11, -9])
        self.assertEqual(large_product([1, 2, 3], [4, 5, 6], 0), [])
        self.assertEqual(large_product([1, 2, 3], [4, 5, 6], 10), [12, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1])
