import unittest
from mbpp_650_code import are_Equal

class TestAreEqual(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(are_Equal([1, 2, 3], [1, 2, 3], 3, 3))
        self.assertTrue(are_Equal([4, 4, 4], [4, 4, 4], 3, 3))

    def test_edge_case_different_lengths(self):
        self.assertFalse(are_Equal([1, 2, 3], [1, 2], 3, 2))
        self.assertFalse(are_Equal([1, 2], [1, 2, 3], 2, 3))

    def test_edge_case_empty_arrays(self):
        self.assertTrue(are_Equal([], [], 0, 0))

    def test_edge_case_single_element(self):
        self.assertTrue(are_Equal([1], [1], 1, 1))

    def test_corner_case_duplicates(self):
        self.assertTrue(are_Equal([1, 1, 2], [1, 2, 1], 3, 3))
        self.assertTrue(are_Equal([1, 1, 1], [1, 1, 1], 3, 3))
