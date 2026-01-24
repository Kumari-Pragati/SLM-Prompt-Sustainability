import unittest
from mbpp_811_code import check_identical

class TestCheckIdentical(unittest.TestCase):
    def test_identical_lists(self):
        self.assertTrue(check_identical([1, 2, 3], [1, 2, 3]))

    def test_different_lengths(self):
        self.assertFalse(check_identical([1, 2, 3], [1, 2]))

    def test_different_elements(self):
        self.assertFalse(check_identical([1, 2, 3], [2, 3, 4]))

    def test_empty_lists(self):
        self.assertTrue(check_identical([], []))

    def test_single_element_lists(self):
        self.assertTrue(check_identical([1], [1]))
