import unittest
from mbpp_650_code import are_Equal

class TestAreEqual(unittest.TestCase):
    def test_equal_arrays(self):
        self.assertTrue(are_Equal([1, 2, 3], [1, 2, 3], 3, 3))

    def test_non_equal_arrays(self):
        self.assertFalse(are_Equal([1, 2, 3], [4, 5, 6], 3, 3))

    def test_arrays_of_different_lengths(self):
        self.assertFalse(are_Equal([1, 2, 3], [1, 2], 3, 2))

    def test_arrays_with_duplicates(self):
        self.assertTrue(are_Equal([1, 2, 2, 3], [1, 2, 2, 3], 4, 4))

    def test_arrays_with_negative_numbers(self):
        self.assertTrue(are_Equal([-1, -2, -3], [-1, -2, -3], 3, 3))

    def test_arrays_with_zero(self):
        self.assertTrue(are_Equal([0, 0, 0], [0, 0, 0], 3, 3))
