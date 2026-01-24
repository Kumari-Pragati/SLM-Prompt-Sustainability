import unittest
from mbpp_790_code import even_position

class TestEvenPosition(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(even_position([]))

    def test_single_element(self):
        for num in [0, 1]:
            self.assertTrue(even_position([num]))

    def test_even_length(self):
        for nums in [(2, 4), (0, 2, 4), (2, 4, 6)]:
            self.assertTrue(even_position(nums))

    def test_odd_length(self):
        for nums in [(1, 3), (0, 2, 3), (1, 3, 5)]:
            self.assertFalse(even_position(nums))

    def test_mixed_even_odd_length(self):
        for nums in [(0, 1, 2), (1, 2, 3, 4), (0, 2, 4, 6, 8)]:
            self.assertFalse(even_position(nums))

    def test_all_even(self):
        self.assertTrue(even_position([0, 2, 4, 6]))

    def test_all_odd(self):
        self.assertFalse(even_position([1, 3, 5, 7]))

    def test_mixed_even_odd(self):
        self.assertFalse(even_position([0, 1, 2, 3, 4, 5]))

    def test_negative_numbers(self):
        self.assertTrue(even_position([-2, -4, -6]))

    def test_zero(self):
        self.assertTrue(even_position([0, 0, 0]))
