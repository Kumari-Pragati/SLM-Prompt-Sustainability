import unittest
from mbpp_804_code import is_Product_Even

class TestIsProductEven(unittest.TestCase):

    def test_empty_array(self):
        self.assertFalse(is_Product_Even([], 0))

    def test_single_element_array(self):
        for num in [0, 1, 2]:
            self.assertFalse(is_Product_Even([num], 1))

    def test_even_length_array(self):
        for arr in [
            [2, 4, 6],
            [1, 3, 5],
            [0, 1, 2],
            [1, 2, 3],
        ]:
            self.assertTrue(is_Product_Even(arr, len(arr)))

    def test_odd_length_array(self):
        for arr in [
            [2, 4, 6, 7],
            [1, 3, 5, 8],
            [0, 1, 2, 3],
            [1, 2, 3, 4],
        ]:
            self.assertFalse(is_Product_Even(arr, len(arr)))

    def test_negative_numbers(self):
        for arr in [
            [-2, -4, -6],
            [-1, -3, -5],
            [-0, -1, -2],
            [-1, -2, -3],
        ]:
            self.assertTrue(is_Product_Even(arr, len(arr)))

    def test_zero_as_input(self):
        self.assertFalse(is_Product_Even([0], 0))

    def test_negative_input(self):
        self.assertFalse(is_Product_Even([-1], 1))
