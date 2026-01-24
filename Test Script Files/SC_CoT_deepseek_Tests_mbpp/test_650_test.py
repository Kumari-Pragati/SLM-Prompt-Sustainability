import unittest
from mbpp_650_code import are_Equal

class TestAreEqual(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(are_Equal([1, 2, 3], [1, 2, 3], 3, 3))

    def test_edge_case_different_lengths(self):
        self.assertFalse(are_Equal([1, 2, 3], [1, 2], 3, 2))

    def test_edge_case_empty_arrays(self):
        self.assertTrue(are_Equal([], [], 0, 0))

    def test_corner_case_same_elements_different_order(self):
        self.assertTrue(are_Equal([1, 2, 3], [3, 2, 1], 3, 3))

    def test_invalid_input_null_array(self):
        with self.assertRaises(TypeError):
            are_Equal(None, [1, 2, 3], 3, 3)

    def test_invalid_input_null_array2(self):
        with self.assertRaises(TypeError):
            are_Equal([1, 2, 3], None, 3, 3)

    def test_invalid_input_negative_length(self):
        with self.assertRaises(ValueError):
            are_Equal([1, 2, 3], [1, 2, 3], -1, 3)

    def test_invalid_input_negative_length2(self):
        with self.assertRaises(ValueError):
            are_Equal([1, 2, 3], [1, 2, 3], 3, -1)

    def test_invalid_input_mismatching_lengths(self):
        with self.assertRaises(ValueError):
            are_Equal([1, 2, 3], [1, 2], 3, 2)
