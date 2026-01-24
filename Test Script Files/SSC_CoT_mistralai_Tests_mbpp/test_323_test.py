import unittest
from mbpp_323_code import re_arrange

class TestReArrange(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(re_arrange([-1, 0, 1, -2, 2, -3, 3]), [-1, 1, -2, 0, 2, -3, 3])
        self.assertEqual(re_arrange([1, -1, 2, -2, 3, -3, 4], 7), [1, 2, -2, 3, -3, 4, -1])

    def test_edge_cases(self):
        self.assertEqual(re_arrange([], 0), [])
        self.assertEqual(re_arrange([-1], 1), [-1])
        self.assertEqual(re_arrange([1, -1], 2), [1, -1])
        self.assertEqual(re_arrange([-1, 0, 1], 3), [-1, 1, 0])
        self.assertEqual(re_arrange([-1, 0, 1, 2], 4), [-1, 1, 2, 0])
        self.assertEqual(re_arrange([-1, 0, 1, 2, -3], 5), [-1, 1, 2, -3, 0])

    def test_boundary_cases(self):
        self.assertEqual(re_arrange([-1, 0, 1, 2, -3], 0), [-1, 0, 1, 2, -3])
        self.assertEqual(re_arrange([-1, 0, 1, 2, -3], 6), [-1, 1, 2, -3, 0])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, re_arrange, 1, 2.5)
        self.assertRaises(TypeError, re_arrange, ['a', 'b', 'c'], 3)
