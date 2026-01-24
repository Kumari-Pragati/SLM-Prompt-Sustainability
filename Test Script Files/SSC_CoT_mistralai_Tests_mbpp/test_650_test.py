import unittest
from mbpp_650_code import are_Equal

class TestAreEqual(unittest.TestCase):

    def test_normal_case(self):
        self.assertTrue(are_Equal([1, 2, 3], [1, 2, 3], 3, 3))
        self.assertTrue(are_Equal([4, 4, 4], [4, 4, 4], 3, 3))

    def test_edge_case_equal_length(self):
        self.assertTrue(are_Equal([1, 2, 3, 4], [1, 2, 3, 4], 4, 4))
        self.assertTrue(are_Equal([], [], 0, 0))

    def test_edge_case_different_length(self):
        self.assertFalse(are_Equal([1, 2, 3], [1, 2, 3, 4], 3, 4))
        self.assertFalse(are_Equal([1, 2, 3], [1, 2], 3, 2))

    def test_boundary_case_empty_arrays(self):
        self.assertFalse(are_Equal([], [1, 2, 3], 0, 3))
        self.assertFalse(are_Equal([1, 2, 3], [], 3, 0))

    def test_invalid_input_different_types(self):
        self.assertRaises(TypeError, are_Equal, [1, 2, 3], 'abc', 3, 3)
        self.assertRaises(TypeError, are_Equal, [1, 2, 3], [1, 2, 3], 'def', 3)
