import unittest
from mbpp_650_code import are_Equal

class TestAreEqual(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(are_Equal([1, 2, 3], [1, 2, 3], 3, 3))
        self.assertTrue(are_Equal([4, 4, 4], [4, 4, 4], 3, 3))

    def test_edge_cases(self):
        self.assertFalse(are_Equal([1, 2, 3], [1, 2, 4], 3, 4))
        self.assertFalse(are_Equal([1, 2, 3], [], 3, 0))
        self.assertFalse(are_Equal([], [1, 2, 3], 0, 3))

    def test_boundary_cases(self):
        self.assertTrue(are_Equal([0], [0], 1, 1))
        self.assertTrue(are_equal([2147483647], [2147483647], 1, 1))

    def test_complex_cases(self):
        self.assertTrue(are_Equal([1, 2, 3, 2], [1, 2, 3, 2], 4, 4))
        self.assertFalse(are_Equal([1, 2, 3], [1, 2, 3, 4], 3, 4))
        self.assertFalse(are_Equal([1, 2, 3], [1, 2, 3, 4], 4, 3))
