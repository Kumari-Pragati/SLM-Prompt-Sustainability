import unittest
from mbpp_811_code import check_identical

class TestCheckIdentical(unittest.TestCase):

    def test_identical_lists(self):
        self.assertTrue(check_identical([1, 2, 3], [1, 2, 3]))

    def test_non_identical_lists(self):
        self.assertFalse(check_identical([1, 2, 3], [1, 2, 4]))

    def test_empty_lists(self):
        self.assertTrue(check_identical([], []))

    def test_lists_of_different_lengths(self):
        self.assertFalse(check_identical([1, 2, 3], [1, 2]))

    def test_lists_with_duplicates(self):
        self.assertTrue(check_identical([1, 2, 2, 3], [1, 2, 2, 3]))

    def test_lists_with_duplicates_and_non_identical(self):
        self.assertFalse(check_identical([1, 2, 2, 3], [1, 2, 3, 4]))
