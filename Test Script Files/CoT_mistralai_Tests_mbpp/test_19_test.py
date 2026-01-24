import unittest
from mbpp_19_code import test_duplicate

class TestDuplicate(unittest.TestCase):
    def test_no_duplicates(self):
        self.assertFalse(test_duplicate([1, 2, 3, 4, 5]))

    def test_single_duplicate(self):
        self.assertTrue(test_duplicate([1, 2, 2, 3, 4, 5]))

    def test_multiple_duplicates(self):
        self.assertTrue(test_duplicate([1, 2, 2, 2, 3, 4, 5]))

    def test_empty_list(self):
        self.assertFalse(test_duplicate([]))

    def test_single_element(self):
        self.assertFalse(test_duplicate([1]))

    def test_duplicates_in_order(self):
        self.assertTrue(test_duplicate([1, 1, 2, 3, 4, 5]))

    def test_duplicates_not_in_order(self):
        self.assertTrue(test_duplicate([1, 3, 1, 2, 4, 5]))

    def test_duplicates_at_beginning(self):
        self.assertTrue(test_duplicate([1, 1, 2, 3, 4, 5]))

    def test_duplicates_at_end(self):
        self.assertTrue(test_duplicate([1, 2, 3, 4, 5, 1]))

    def test_duplicates_in_middle(self):
        self.assertTrue(test_duplicate([1, 2, 3, 4, 5, 1]))

    def test_negative_numbers(self):
        self.assertTrue(test_duplicate([-1, -2, -2, -3, -4, -5]))

    def test_mixed_numbers(self):
        self.assertTrue(test_duplicate([1, -2, -2, 3, 4, 5]))
