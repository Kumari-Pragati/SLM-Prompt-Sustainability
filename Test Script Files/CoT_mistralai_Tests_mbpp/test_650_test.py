import unittest
from mbpp_650_code import are_Equal

class TestAreEqual(unittest.TestCase):
    def test_equal_arrays(self):
        self.assertTrue(are_Equal([1, 2, 3], [1, 2, 3], 3, 3))
        self.assertTrue(are_Equal([5, 3, 1], [5, 3, 1], 3, 3))

    def test_different_lengths(self):
        self.assertFalse(are_Equal([1, 2, 3], [1, 2], 3, 2))
        self.assertFalse(are_Equal([1, 2, 3], [1, 2, 3, 4], 3, 4))

    def test_empty_arrays(self):
        self.assertTrue(are_Equal([], [], 0, 0))

    def test_single_element_arrays(self):
        self.assertTrue(are_Equal([1], [1], 1, 1))
        self.assertFalse(are_Equal([1], [2], 1, 1))

    def test_sorted_arrays_different_order(self):
        self.assertFalse(are_Equal([1, 2, 3], [3, 2, 1], 3, 3))
        self.assertFalse(are_Equal([5, 3, 1], [1, 3, 5], 3, 3))

    def test_duplicates(self):
        self.assertTrue(are_Equal([1, 1, 2, 2], [1, 2, 1, 2], 4, 4))
        self.assertTrue(are_Equal([1, 1, 2, 2], [2, 2, 1, 1], 4, 4))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, are_Equal, 1, 2, 3, 4)
        self.assertRaises(TypeError, are_Equal, [1, 2], 'string', 3, 2)
        self.assertRaises(TypeError, are_Equal, [1, 2], [1, 2], 'number', 3)
