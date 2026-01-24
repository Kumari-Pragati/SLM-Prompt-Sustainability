import unittest
from mbpp_650_code import are_Equal

class TestAreEqual(unittest.TestCase):

    def test_same_length_equal_arrays(self):
        self.assertTrue(are_Equal([1, 2, 3], [1, 2, 3], 3, 3))

    def test_same_length_unequal_arrays(self):
        self.assertFalse(are_Equal([1, 2, 3], [1, 2, 4], 3, 3))

    def test_different_length_equal_arrays(self):
        self.assertFalse(are_Equal([1, 2, 3], [1, 2, 3, 4], 3, 4))

    def test_different_length_unequal_arrays(self):
        self.assertFalse(are_Equal([1, 2, 3], [1, 2, 4], 3, 4))

    def test_empty_arrays(self):
        self.assertTrue(are_Equal([], [], 0, 0))

    def test_single_element_arrays(self):
        self.assertTrue(are_Equal([1], [1], 1, 1))
        self.assertFalse(are_Equal([1], [2], 1, 1))

    def test_duplicate_elements(self):
        self.assertTrue(are_Equal([1, 2, 2], [1, 2, 2], 3, 3))
        self.assertFalse(are_Equal([1, 2, 2], [1, 2, 3], 3, 3))

    def test_negative_numbers(self):
        self.assertTrue(are_Equal([-1, -2, -3], [-1, -2, -3], 3, 3))
        self.assertFalse(are_Equal([-1, -2, -3], [-1, -2, -4], 3, 3))

    def test_large_numbers(self):
        self.assertTrue(are_Equal([1000, 2000, 3000], [1000, 2000, 3000], 3, 3))
        self.assertFalse(are_Equal([1000, 2000, 3000], [1000, 2001, 3000], 3, 3))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            are_Equal("not a list", [1, 2, 3], 3, 3)
        with self.assertRaises(TypeError):
            are_Equal([1, 2, 3], "not a list", 3, 3)
        with self.assertRaises(TypeError):
            are_Equal([1, 2, 3], [1, 2, 3], "not an integer", 3)
        with self.assertRaises(TypeError):
            are_Equal([1, 2, 3], [1, 2, 3], 3, "not an integer")
