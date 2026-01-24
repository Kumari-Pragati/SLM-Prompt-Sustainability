import unittest
from mbpp_650_code import are_Equal

class TestAreEqual(unittest.TestCase):
    def test_equal_arrays(self):
        self.assertTrue(are_Equal([1, 2, 3], [1, 2, 3], 3, 3))

    def test_equal_length_different_elements(self):
        self.assertFalse(are_Equal([1, 2, 3], [1, 2, 4], 3, 4))

    def test_different_length_arrays(self):
        self.assertFalse(are_Equal([1, 2, 3], [1, 2], 3, 2))

    def test_empty_arrays(self):
        self.assertTrue(are_Equal([], [], 0, 0))

    def test_negative_array_length(self):
        self.assertRaises(ValueError, are_Equal, [1, 2, 3], [1, 2, 4], -1, 3)

    def test_negative_array_elements(self):
        self.assertRaises(TypeError, are_Equal, [-1, -2, -3], [-1, -2, 4], 3, 3)
