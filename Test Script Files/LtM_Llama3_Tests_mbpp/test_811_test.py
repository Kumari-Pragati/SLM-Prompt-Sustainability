import unittest
from mbpp_811_code import check_identical

class TestCheckIdentical(unittest.TestCase):
    def test_simple_identical(self):
        self.assertTrue(check_identical([1, 2, 3], [1, 2, 3]))

    def test_simple_non_identical(self):
        self.assertFalse(check_identical([1, 2, 3], [1, 2, 4]))

    def test_empty_lists(self):
        self.assertFalse(check_identical([], []))
        self.assertFalse(check_identical([], [1, 2, 3]))
        self.assertFalse(check_identical([1, 2, 3], []))

    def test_single_element_lists(self):
        self.assertTrue(check_identical([1], [1]))
        self.assertFalse(check_identical([1], [2]))

    def test_lists_with_duplicates(self):
        self.assertTrue(check_identical([1, 2, 2, 3], [1, 2, 2, 3]))
        self.assertFalse(check_identical([1, 2, 2, 3], [1, 2, 3]))

    def test_lists_with_duplicates_and_order(self):
        self.assertTrue(check_identical([1, 2, 2, 3], [1, 2, 3, 2]))
        self.assertFalse(check_identical([1, 2, 2, 3], [1, 2, 3, 4]))
