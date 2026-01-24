import unittest
from mbpp_811_code import check_identical

class TestCheckIdentical(unittest.TestCase):

    def test_identical_lists(self):
        self.assertTrue(check_identical([1, 2, 3], [1, 2, 3]))

    def test_different_lists(self):
        self.assertFalse(check_identical([1, 2, 3], [1, 2, 4]))

    def test_empty_lists(self):
        self.assertTrue(check_identical([], []))

    def test_one_empty_list(self):
        self.assertFalse(check_identical([1, 2, 3], []))

    def test_different_order(self):
        self.assertFalse(check_identical([1, 2, 3], [3, 2, 1]))

    def test_identical_with_duplicates(self):
        self.assertTrue(check_identical([1, 2, 2, 3], [1, 2, 2, 3]))

    def test_different_with_duplicates(self):
        self.assertFalse(check_identical([1, 2, 2, 3], [1, 2, 2, 4]))
