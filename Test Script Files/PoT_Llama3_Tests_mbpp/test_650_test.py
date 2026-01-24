import unittest
from mbpp_650_code import are_Equal

class TestAreEqual(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(are_Equal([1, 2, 3], [1, 2, 3], 3, 3))

    def test_edge_case_equal(self):
        self.assertTrue(are_Equal([1, 2, 3], [1, 2, 3], 3, 3))

    def test_edge_case_not_equal(self):
        self.assertFalse(are_Equal([1, 2, 3], [4, 5, 6], 3, 3))

    def test_edge_case_diff_length(self):
        self.assertFalse(are_Equal([1, 2, 3], [1, 2], 3, 2))

    def test_edge_case_empty(self):
        self.assertTrue(are_Equal([], [], 0, 0))

    def test_edge_case_single_element(self):
        self.assertTrue(are_Equal([1], [1], 1, 1))

    def test_edge_case_single_element_diff(self):
        self.assertFalse(are_Equal([1], [2], 1, 1))

    def test_edge_case_empty_diff(self):
        self.assertFalse(are_Equal([], [1], 0, 1))

    def test_edge_case_empty_diff2(self):
        self.assertFalse(are_Equal([1], [], 1, 0))
