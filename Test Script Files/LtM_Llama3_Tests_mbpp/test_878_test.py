import unittest
from mbpp_878_code import check_tuples

class TestCheckTuples(unittest.TestCase):
    def test_simple_valid(self):
        self.assertTrue(check_tuples((1, 2, 3), [1, 2, 3]))

    def test_empty_input(self):
        self.assertFalse(check_tuples([], [1, 2, 3]))

    def test_empty_K(self):
        self.assertFalse(check_tuples([1, 2, 3], []))

    def test_single_element(self):
        self.assertTrue(check_tuples([1], [1]))

    def test_single_element_not_in_K(self):
        self.assertFalse(check_tuples([1], [2, 3]))

    def test_multiple_elements(self):
        self.assertTrue(check_tuples([1, 2, 3], [1, 2, 3]))

    def test_multiple_elements_not_in_K(self):
        self.assertFalse(check_tuples([1, 2, 3], [4, 5]))

    def test_K_with_duplicates(self):
        self.assertTrue(check_tuples([1, 2, 2], [1, 2]))

    def test_K_with_duplicates_and_missing(self):
        self.assertFalse(check_tuples([1, 2, 3], [1, 2, 2, 4]))
