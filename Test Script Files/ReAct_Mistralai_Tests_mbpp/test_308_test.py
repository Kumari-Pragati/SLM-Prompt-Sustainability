import unittest
from mbpp_308_code import large_product

class TestLargeProduct(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(large_product([], [], 0), [])

    def test_single_element_lists(self):
        self.assertListEqual(large_product([1], [2], 1), [2])
        self.assertListEqual(large_product([2], [1], 1), [2])

    def test_simple_multiplication(self):
        self.assertListEqual(large_product([1, 2, 3], [4, 5], 2), [8, 6])

    def test_large_numbers(self):
        self.assertListEqual(large_product([1000, 2000, 3000], [4000, 5000], 1), [4000, 5000])
        self.assertListEqual(large_product([1000, 2000, 3000], [4000, 5000], 2), [8000, 6000])

    def test_negative_numbers(self):
        self.assertListEqual(large_product([-1, -2, -3], [-4, -5], 2), [20, 15])

    def test_boundary_cases(self):
        self.assertListEqual(large_product([1, 2, 3], [4, 5], 1), [4, 3])
        self.assertListEqual(large_product([1, 2, 3], [4, 5], 2), [4, 3])
        self.assertListEqual(large_product([1, 2, 3], [4, 5], 3), [4])

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            large_product(1, 2, 3)
        with self.assertRaises(TypeError):
            large_product('a', 'b', 3)
        with self.assertRaises(ValueError):
            large_product([1], [2], -1)
