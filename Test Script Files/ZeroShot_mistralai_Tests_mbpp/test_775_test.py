import unittest
from mbpp_775_code import odd_position

class TestOddPosition(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(odd_position([]))

    def test_single_element(self):
        for num in [0, 1, 3, 5]:
            self.assertTrue(odd_position([num]))

    def test_even_length_list(self):
        for nums in [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]]:
            self.assertFalse(odd_position(nums))

    def test_odd_length_list(self):
        for nums in [[0, 1, 2], [1, 3, 5], [2, 4, 6], [3, 5, 7]]:
            self.assertTrue(odd_position(nums))

    def test_mixed_even_odd_length_list(self):
        for nums in [[0, 1, 2, 3], [1, 3, 5, 7], [2, 4, 6, 8]]:
            self.assertFalse(odd_position(nums))

    def test_mixed_even_odd_values_list(self):
        for nums in [[0, 1, 2, 3, 4], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]]:
            self.assertFalse(odd_position(nums))
