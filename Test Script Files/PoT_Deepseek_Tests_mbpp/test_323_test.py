import unittest
from mbpp_323_code import re_arrange

class TestRearrange(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(re_arrange([1, -2, 3, -4, 5], 5), [1, -2, 3, -4, 5])

    def test_edge_case(self):
        self.assertEqual(re_arrange([], 0), [])
        self.assertEqual(re_arrange([1], 1), [1])

    def test_boundary_case(self):
        self.assertEqual(re_arrange([1, -1, 2, -2], 4), [1, -1, 2, -2])
        self.assertEqual(re_arrange([1, -1, 2, -2, 3], 5), [1, -1, 2, -2, 3])

    def test_corner_case(self):
        self.assertEqual(re_arrange([-1, 2, -3, 4, -5], 5), [-1, 2, -3, 4, -5])
        self.assertEqual(re_arrange([-1, 2, -3, 4, -5, 6], 6), [-1, 2, -3, 4, -5, 6])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            re_arrange("not a list", 5)
        with self.assertRaises(TypeError):
            re_arrange([1, 2, 3], "not an integer")
