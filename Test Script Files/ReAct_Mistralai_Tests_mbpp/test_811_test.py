import unittest
from mbpp_811_code import check_identical

class TestCheckIdentical(unittest.TestCase):

    def test_identical_lists(self):
        self.assertTrue(check_identical([1, 2, 3], [1, 2, 3]))

    def test_identical_lists_case_sensitive_strings(self):
        self.assertTrue(check_identical(['Hello', 'World'], ['Hello', 'World']))
        self.assertFalse(check_identical(['Hello', 'world'], ['Hello', 'World']))

    def test_identical_lists_empty(self):
        self.assertTrue(check_identical([], []))

    def test_identical_lists_single_element(self):
        self.assertTrue(check_identical([1], [1]))

    def test_identical_lists_different_order(self):
        self.assertFalse(check_identical([1, 2, 3], [3, 2, 1]))

    def test_identical_lists_different_types(self):
        self.assertFalse(check_identical([1, 2, 3], [1, 2, '3']))

    def test_identical_lists_different_lengths(self):
        self.assertFalse(check_identical([1, 2, 3], [1, 2]))

    def test_identical_lists_with_none(self):
        self.assertFalse(check_identical([1, 2, None], [1, 2, None]))
        self.assertFalse(check_identical([1, 2, None], [1, 2, None, 4]))
