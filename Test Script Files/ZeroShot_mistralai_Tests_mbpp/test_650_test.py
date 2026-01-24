import unittest
from mbpp_650_code import are_Equal

class TestAreEqual(unittest.TestCase):

    def test_are_equal_same_arrays(self):
        self.assertTrue(are_Equal([1, 2, 3], [1, 2, 3], 3, 3))
        self.assertTrue(are_Equal([4, 4, 4], [4, 4, 4], 3, 3))
        self.assertTrue(are_Equal([5, 5, 5, 5], [5, 5, 5, 5], 4, 4))

    def test_are_equal_different_lengths(self):
        self.assertFalse(are_Equal([1, 2, 3], [1, 2, 3, 4], 3, 4))
        self.assertFalse(are_Equal([1, 2, 3], [1, 2], 3, 2))

    def test_are_equal_different_elements(self):
        self.assertFalse(are_Equal([1, 2, 3], [2, 2, 3], 3, 3))
        self.assertFalse(are_Equal([1, 2, 3], [1, 3, 2], 3, 3))
        self.assertFalse(are_Equal([1, 2, 3], [1, 2, 4], 3, 3))
