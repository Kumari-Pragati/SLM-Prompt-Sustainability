import unittest
from mbpp_19_code import test_duplicate

class TestDuplicate(unittest.TestCase):

    def test_typical_case_with_duplicates(self):
        self.assertTrue(test_duplicate([1, 2, 2, 3, 4]))

    def test_typical_case_without_duplicates(self):
        self.assertFalse(test_duplicate([1, 2, 3, 4]))

    def test_empty_list(self):
        self.assertFalse(test_duplicate([]))

    def test_single_element_list(self):
        self.assertFalse(test_duplicate([1]))

    def test_duplicate_elements(self):
        self.assertTrue(test_duplicate([1, 1, 1, 1]))

    def test_negative_numbers(self):
        self.assertTrue(test_duplicate([-1, -2, -2, -3]))

    def test_mixed_numbers(self):
        self.assertTrue(test_duplicate([1, -1, 2, -2]))

    def test_zero(self):
        self.assertTrue(test_duplicate([0, 0]))
