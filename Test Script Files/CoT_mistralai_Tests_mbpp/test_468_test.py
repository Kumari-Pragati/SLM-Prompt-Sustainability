import unittest
from mbpp_468_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(max_product([], 0), 0)

    def test_single_element_array(self):
        for num in range(10):
            self.assertEqual(max_product([num], 1), num)

    def test_positive_numbers(self):
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 6, 24, 120]
        for i, val in enumerate(arr):
            self.assertEqual(max_product(arr, i+1), expected[i])

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        expected = [1, -2, 2, 6, 30]
        for i, val in enumerate(arr):
            self.assertEqual(max_product(arr, i+1), expected[i])

    def test_mixed_numbers(self):
        arr = [1, -2, 3, -4, 5]
        expected = [1, -2, 6, -24, 120]
        for i, val in enumerate(arr):
            self.assertEqual(max_product(arr, i+1), expected[i])

    def test_zero_in_array(self):
        arr = [0, 1, 2, 3, 4]
        expected = [0, 1, 2, 6, 24]
        for i, val in enumerate(arr):
            self.assertEqual(max_product(arr, i+1), expected[i])

    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            max_product([1, 2, 3], 4)

    def test_invalid_input_array(self):
        with self.assertRaises(TypeError):
            max_product('abc', 1)
