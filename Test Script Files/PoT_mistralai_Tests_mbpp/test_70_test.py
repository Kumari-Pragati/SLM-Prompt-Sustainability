import unittest
from mbpp_70_code import get_equal

class TestGetEqual(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_equal([(1, 2, 3), (1, 2, 3), (1, 2, 3)], 3), "All tuples have same length")
        self.assertEqual(get_equal([(1, 2, 3), (1, 2), (1, 2, 3)], 3), "All tuples do not have same length")
        self.assertEqual(get_equal([(1, 2, 3), (1, 2, 3), (1, 2, 3, 4)], 3), "All tuples do not have same length")

    def test_edge_case(self):
        self.assertEqual(get_equal([], 3), "All tuples do not have same length")
        self.assertEqual(get_equal([(1, 2, 3)], 3), "All tuples have same length")
        self.assertEqual(get_equal([(1, 2, 3), (1, 2, 3)], 2), "All tuples do not have same length")
        self.assertEqual(get_equal([(1, 2, 3), (1, 2, 3)], 4), "All tuples do not have same length")
