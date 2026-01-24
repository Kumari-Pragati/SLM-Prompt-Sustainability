import unittest
from mbpp_650_code import are_Equal

class TestAreEqual(unittest.TestCase):

    def test_equal_arrays(self):
        self.assertTrue(are_Equal([1, 2, 3], [1, 2, 3], 3, 3))
        self.assertTrue(are_Equal([5, 3, 1], [5, 3, 1], 3, 3))

    def test_empty_arrays(self):
        self.assertTrue(are_Equal([], [], 0, 0))

    def test_single_element_arrays(self):
        self.assertTrue(are_Equal([1], [1], 1, 1))
        self.assertFalse(are_Equal([1], [2], 1, 1))

    def test_different_lengths(self):
        self.assertFalse(are_Equal([1, 2, 3], [1, 2], 3, 2))
        self.assertFalse(are_Equal([1, 2], [1, 2, 3], 2, 3))

    def test_duplicates(self):
        self.assertTrue(are_Equal([1, 1, 2, 2], [1, 2, 1, 2], 4, 4))
        self.assertTrue(are_Equal([1, 1, 2, 2], [2, 1, 2, 1], 4, 4))

    def test_negative_numbers(self):
        self.assertTrue(are_Equal([-1, -2, -3], [-1, -2, -3], 3, 3))

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            are_Equal([1, 2, 3], [1, 2, "3"], 3, 3)
