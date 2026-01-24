import unittest
from mbpp_650_code import are_Equal

class TestAreEqual(unittest.TestCase):

    def test_simple_equal_arrays(self):
        self.assertTrue(are_Equal([1, 2, 3], [1, 2, 3], 3, 3))

    def test_simple_unequal_arrays(self):
        self.assertFalse(are_Equal([1, 2, 3], [1, 2, 4], 3, 3))

    def test_empty_arrays(self):
        self.assertTrue(are_Equal([], [], 0, 0))

    def test_different_length_arrays(self):
        self.assertFalse(are_Equal([1, 2, 3], [1, 2], 3, 2))

    def test_arrays_with_duplicates(self):
        self.assertTrue(are_Equal([1, 2, 2], [2, 1, 2], 3, 3))

    def test_arrays_with_same_elements_different_order(self):
        self.assertTrue(are_Equal([3, 2, 1], [1, 2, 3], 3, 3))

    def test_arrays_with_same_elements_same_order(self):
        self.assertTrue(are_Equal([1, 2, 3], [1, 2, 3], 3, 3))
