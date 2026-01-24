import unittest
from mbpp_19_code import test_duplicate

class TestDuplicate(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(test_duplicate([1, 2, 3, 4, 5]))

    def test_duplicate_case(self):
        self.assertTrue(test_duplicate([1, 2, 2, 3, 4]))

    def test_empty_list(self):
        self.assertFalse(test_duplicate([]))

    def test_single_element(self):
        self.assertFalse(test_duplicate([1]))

    def test_duplicate_in_list(self):
        self.assertTrue(test_duplicate([1, 1, 2, 3, 4]))

    def test_negative_numbers(self):
        self.assertTrue(test_duplicate([-1, -2, -3, -4]))

    def test_duplicate_negative_numbers(self):
        self.assertTrue(test_duplicate([-1, -2, -2, -3, -4]))

    def test_duplicate_in_list_with_zero(self):
        self.assertTrue(test_duplicate([0, 0, 1, 2, 3]))

    def test_duplicate_in_list_with_zero_and_negative(self):
        self.assertTrue(test_duplicate([-1, 0, 0, 1, 2]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            test_duplicate("1, 2, 3, 4, 5")
