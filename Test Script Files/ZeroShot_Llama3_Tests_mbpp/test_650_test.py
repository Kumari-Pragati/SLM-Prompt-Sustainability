import unittest
from mbpp_650_code import are_Equal

class TestAreEqual(unittest.TestCase):

    def test_are_Equal_same_length(self):
        self.assertTrue(are_Equal([1, 2, 3], [1, 2, 3], 3, 3))

    def test_are_Equal_diff_length(self):
        self.assertFalse(are_Equal([1, 2, 3], [1, 2, 4], 3, 4))

    def test_are_Equal_sorted(self):
        self.assertTrue(are_Equal([1, 2, 3], [1, 2, 3], 3, 3))

    def test_are_Equal_unsorted(self):
        self.assertFalse(are_Equal([3, 2, 1], [1, 2, 3], 3, 3))

    def test_are_Equal_empty(self):
        self.assertTrue(are_Equal([], [], 0, 0))

    def test_are_Equal_single_element(self):
        self.assertTrue(are_Equal([1], [1], 1, 1))

    def test_are_Equal_negative_numbers(self):
        self.assertTrue(are_Equal([-1, -2, -3], [-1, -2, -3], 3, 3))

    def test_are_Equal_duplicates(self):
        self.assertTrue(are_Equal([1, 1, 2], [1, 1, 2], 3, 3))
