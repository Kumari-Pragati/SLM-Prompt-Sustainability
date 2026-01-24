import unittest
from mbpp_650_code import are_Equal

class TestAreEqual(unittest.TestCase):
    def test_equal_arrays(self):
        self.assertTrue(are_Equal([1, 2, 3], [1, 2, 3], 3, 3))

    def test_non_equal_arrays(self):
        self.assertFalse(are_Equal([1, 2, 3], [1, 2, 4], 3, 3))

    def test_arrays_of_different_lengths(self):
        self.assertFalse(are_Equal([1, 2, 3], [1, 2], 3, 2))

    def test_arrays_of_same_length_with_duplicates(self):
        self.assertTrue(are_Equal([1, 2, 2, 3], [1, 2, 2, 3], 4, 4))

    def test_arrays_of_same_length_with_duplicates_and_non_duplicates(self):
        self.assertTrue(are_Equal([1, 2, 2, 3, 4], [1, 2, 2, 3, 4], 5, 5))

    def test_arrays_of_same_length_with_duplicates_and_non_duplicates_and_duplicates(self):
        self.assertTrue(are_Equal([1, 2, 2, 2, 3, 4, 4], [1, 2, 2, 2, 3, 4, 4], 7, 7))
