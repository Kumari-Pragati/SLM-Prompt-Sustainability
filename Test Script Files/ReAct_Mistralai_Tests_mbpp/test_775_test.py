import unittest
from mbpp_775_code import odd_position

class TestOddPosition(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(odd_position([]))

    def test_single_element(self):
        for num in [0, 1, 3, 5]:
            self.assertTrue(odd_position([num]))

    def test_even_length_list(self):
        for nums in [[0, 2], [2, 0], [4, 6], [6, 4]]:
            self.assertFalse(odd_position(nums))

    def test_odd_length_list(self):
        for nums in [[1, 3, 5], [3, 1, 5], [5, 3, 1], [5, 1, 3]]:
            self.assertTrue(odd_position(nums))

    def test_mixed_even_odd_length_list(self):
        for nums in [[0, 1, 2], [2, 1, 0], [4, 1, 6], [6, 1, 4]]:
            self.assertFalse(odd_position(nums))

    def test_mixed_odd_even_length_list(self):
        for nums in [[1, 3, 5, 7], [3, 1, 5, 7], [5, 3, 1, 7], [5, 1, 3, 7]]:
            self.assertTrue(odd_position(nums))

    def test_negative_numbers(self):
        for nums in [[1, -1, 3], [-1, 1, -3], [-3, -1, 1]]:
            self.assertTrue(odd_position(nums))

    def test_all_zero(self):
        self.assertTrue(odd_position([0, 0, 0]))

    def test_all_negative(self):
        self.assertTrue(odd_position([-1, -2, -3]))

    def test_all_positive(self):
        self.assertTrue(odd_position([1, 2, 3]))
