import unittest
from mbpp_775_code import odd_position

class TestOddPosition(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(odd_position([]))

    def test_single_element(self):
        for num in [0, 1, 3, 5]:
            self.assertTrue(odd_position([num]))

    def test_even_length_list(self):
        for nums in [[0, 1], [1, 0], [2, 4], [4, 2]]:
            self.assertFalse(odd_position(nums))

    def test_odd_length_list(self):
        for nums in [[0, 1, 2], [1, 0, 3], [2, 3, 0], [3, 2, 1]]:
            self.assertTrue(odd_position(nums))

    def test_mixed_parity_list(self):
        for nums in [[0, 1, 2, 3], [1, 0, 3, 2], [2, 3, 0, 1], [3, 2, 1, 0]]:
            self.assertFalse(odd_position(nums))

    def test_invalid_input(self):
        self.assertRaises(TypeError, odd_position, 'string')
