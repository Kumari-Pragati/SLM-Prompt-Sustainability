import unittest
from mbpp_811_code import check_identical

class TestCheckIdentical(unittest.TestCase):

    def test_simple_identical_lists(self):
        self.assertTrue(check_identical([1, 2, 3], [1, 2, 3]))
        self.assertTrue(check_identical([], []))
        self.assertTrue(check_identical([0], [0]))

    def test_simple_non_identical_lists(self):
        self.assertFalse(check_identical([1, 2, 3], [1, 2, 4]))
        self.assertFalse(check_identical([1, 2], [1, 2, 3]))
        self.assertFalse(check_identical([1], [1, 2]))

    def test_edge_cases(self):
        self.assertTrue(check_identical([1], [1, None]))
        self.assertTrue(check_identical([None], [1, None]))
        self.assertTrue(check_identical([None], []))
        self.assertTrue(check_identical([], [None]))

    def test_complex_cases(self):
        self.assertTrue(check_identical([1, 1, 2, 2], [2, 1, 2, 1]))
        self.assertFalse(check_identical([1, 1, 2, 2], [2, 1, 3, 1]))
        self.assertFalse(check_identical([1, 1, 2, 2], [1, 2, 2, 1]))
