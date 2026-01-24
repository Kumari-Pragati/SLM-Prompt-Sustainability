import unittest
from mbpp_811_code import check_identical

class TestCheckIdentical(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(check_identical([1, 2, 3], [1, 2, 3]))
        self.assertFalse(check_identical([1, 2, 3], [1, 2, 4]))

    def test_empty_lists(self):
        self.assertTrue(check_identical([], []))

    def test_single_element_lists(self):
        self.assertTrue(check_identical([1], [1]))
        self.assertFalse(check_identical([1], [2]))

    def test_different_order(self):
        self.assertTrue(check_identical([1, 2, 3], [3, 2, 1]))

    def test_nested_lists(self):
        self.assertTrue(check_identical([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
        self.assertFalse(check_identical([[1, 2], [3, 4]], [[1, 2], [3, 5]]))

    def test_unequal_lengths(self):
        self.assertFalse(check_identical([1, 2, 3], [1, 2]))
