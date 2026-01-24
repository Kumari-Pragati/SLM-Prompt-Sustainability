import unittest
from mbpp_775_code import odd_position

class TestOddPosition(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(odd_position([1, 3, 5]))

    def test_typical_case_with_even_numbers(self):
        self.assertFalse(odd_position([2, 4, 6]))

    def test_typical_case_with_mixed_numbers(self):
        self.assertFalse(odd_position([1, 2, 3, 4, 5, 6]))

    def test_empty_list(self):
        self.assertTrue(odd_position([]))

    def test_single_element_list(self):
        self.assertTrue(odd_position([1]))

    def test_single_element_list_with_even_number(self):
        self.assertFalse(odd_position([2]))

    def test_negative_numbers(self):
        self.assertTrue(odd_position([-1, -3, -5]))

    def test_negative_numbers_with_even_numbers(self):
        self.assertFalse(odd_position([-2, -4, -6]))

    def test_negative_numbers_with_mixed_numbers(self):
        self.assertFalse(odd_position([-1, 2, -3, 4, -5, 6]))
