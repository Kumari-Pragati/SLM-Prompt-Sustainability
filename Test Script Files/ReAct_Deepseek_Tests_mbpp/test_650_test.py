import unittest
from mbpp_650_code import are_Equal

class TestAreEqual(unittest.TestCase):

    def test_equal_arrays_with_same_length(self):
        self.assertTrue(are_Equal([1, 2, 3], [1, 2, 3], 3, 3))

    def test_equal_arrays_with_different_length(self):
        self.assertFalse(are_Equal([1, 2, 3], [1, 2, 3, 4], 3, 4))

    def test_unequal_arrays_with_same_length(self):
        self.assertFalse(are_Equal([1, 2, 3], [3, 2, 1], 3, 3))

    def test_empty_arrays(self):
        self.assertTrue(are_Equal([], [], 0, 0))

    def test_arrays_with_duplicates(self):
        self.assertTrue(are_Equal([1, 2, 2], [2, 1, 2], 3, 3))

    def test_arrays_with_negative_numbers(self):
        self.assertTrue(are_Equal([-1, -2, -3], [-3, -2, -1], 3, 3))

    def test_arrays_with_mixed_numbers(self):
        self.assertFalse(are_Equal([1, -2, 3], [3, -2, 1], 3, 3))
