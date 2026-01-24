import unittest
from mbpp_811_code import check_identical

class TestCheckIdentical(unittest.TestCase):

    # Test for simple / typical inputs
    def test_identical_lists(self):
        self.assertTrue(check_identical([1, 2, 3], [1, 2, 3]))

    # Test for edge and boundary conditions
    def test_empty_lists(self):
        self.assertTrue(check_identical([], []))

    def test_one_empty_list(self):
        self.assertFalse(check_identical([1, 2, 3], []))

    def test_identical_with_duplicates(self):
        self.assertTrue(check_identical([1, 2, 2], [1, 2, 2]))

    # Test for more complex or corner cases
    def test_different_lengths(self):
        self.assertFalse(check_identical([1, 2, 3], [1, 2]))

    def test_different_elements(self):
        self.assertFalse(check_identical([1, 2, 3], [4, 5, 6]))

    def test_identical_with_different_order(self):
        self.assertFalse(check_identical([1, 2, 3], [3, 2, 1]))
