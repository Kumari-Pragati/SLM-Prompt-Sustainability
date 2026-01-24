import unittest
from mbpp_308_code import large_product

class TestLargeProduct(unittest.TestCase):

    def test_large_product(self):
        self.assertEqual(large_product([1, 2, 3], [4, 5, 6], 2), [36, 30])
        self.assertEqual(large_product([-1, -2, -3], [-4, -5, -6], 2), [-1, -1])
        self.assertEqual(large_product([1, 2, 3], [4, 5, 6], 3), [36, 30, 24])
        self.assertEqual(large_product([0, 0, 0], [4, 5, 6], 3), [0, 0, 0])
        self.assertEqual(large_product([1, 2, 3], [0, 0, 0], 3), [0, 0, 0])
        self.assertEqual(large_product([1, 2, 3], [4, 5, 6], 0), [])
