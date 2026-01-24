import unittest
from mbpp_650_code import are_Equal

class TestAreEqual(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(are_Equal([1, 2, 3], [1, 2, 3], 3, 3))
        self.assertFalse(are_Equal([1, 2, 3], [1, 2, 4], 3, 3))
        self.assertFalse(are_Equal([1, 2, 3], [1, 2, 3], 2, 3))

    def test_empty(self):
        self.assertFalse(are_Equal([], [], 0, 0))
        self.assertFalse(are_Equal([1], [], 1, 0))
        self.assertFalse(are_Equal([], [1], 0, 1))

    def test_single_element(self):
        self.assertTrue(are_Equal([1], [1], 1, 1))
        self.assertFalse(are_Equal([1], [2], 1, 1))

    def test_sorted(self):
        self.assertTrue(are_Equal([1, 2, 3], [1, 2, 3], 3, 3))
        self.assertFalse(are_Equal([1, 2, 3], [3, 2, 1], 3, 3))

    def test_unsorted(self):
        self.assertTrue(are_Equal([3, 2, 1], [1, 2, 3], 3, 3))
        self.assertFalse(are_Equal([3, 2, 1], [2, 1, 3], 3, 3))
