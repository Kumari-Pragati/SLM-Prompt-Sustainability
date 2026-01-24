import unittest
from mbpp_472_code import check_Consecutive

class TestCheckConsecutive(unittest.TestCase):

    def test_simple_valid_input(self):
        self.assertTrue(check_Consecutive([1, 2, 3, 4, 5]))

    def test_simple_invalid_input(self):
        self.assertFalse(check_Consecutive([1, 3, 2, 5, 4]))

    def test_empty_input(self):
        self.assertTrue(check_Consecutive([]))

    def test_single_element_input(self):
        self.assertTrue(check_Consecutive([1]))

    def test_minimum_maximum_values(self):
        self.assertTrue(check_Consecutive(list(range(1, 101))))
        self.assertFalse(check_Consecutive([100, 99, 98, 97, 96]))

    def test_negative_numbers(self):
        self.assertTrue(check_Consecutive([-10, -9, -8, -7, -6]))
        self.assertFalse(check_Consecutive([-10, -8, -9, -7, -6]))

    def test_duplicates(self):
        self.assertFalse(check_Consecutive([1, 1, 2, 3, 4]))
