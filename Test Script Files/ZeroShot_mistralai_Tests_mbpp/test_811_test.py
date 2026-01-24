import unittest
from mbpp_811_code import check_identical

class TestCheckIdentical(unittest.TestCase):

    def test_identical_lists(self):
        self.assertTrue(check_identical([1, 2, 3], [1, 2, 3]))
        self.assertTrue(check_identical([], []))
        self.assertTrue(check_identical([1.0, 2.0, 3.0], [1.0, 2.0, 3.0]))

    def test_not_identical_lists(self):
        self.assertFalse(check_identical([1, 2, 3], [1, 2, 4]))
        self.assertFalse(check_identical([1, 2, 3], [3, 2, 1]))
        self.assertFalse(check_identical([1.0, 2.0, 3.0], [1.0, 2.1, 3.0]))
        self.assertFalse(check_identical([1, 2, 3], [1, 2, 3, 4]))
        self.assertFalse(check_identical([1, 2, 3], [1, 2]))
