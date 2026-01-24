import unittest
from mbpp_790_code import even_position

class TestEvenPosition(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(even_position([0, 2, 4, 6]))

    def test_typical_case_with_odd_numbers(self):
        self.assertFalse(even_position([1, 2, 3, 4]))

    def test_empty_list(self):
        self.assertTrue(even_position([]))

    def test_single_element(self):
        self.assertTrue(even_position([0]))

    def test_single_element_odd(self):
        self.assertFalse(even_position([1]))

    def test_negative_numbers(self):
        self.assertTrue(even_position([-2, -4, -6]))

    def test_negative_numbers_with_odd(self):
        self.assertFalse(even_position([-1, -2, -3, -4]))

    def test_mixed_positive_negative(self):
        self.assertFalse(even_position([-1, 0, 1, 2]))

    def test_mixed_positive_negative_with_zero(self):
        self.assertTrue(even_position([0, -2, 0, -4]))
