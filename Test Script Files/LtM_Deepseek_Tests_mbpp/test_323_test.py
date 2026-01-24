import unittest
from mbpp_323_code import re_arrange

class TestReArrange(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(re_arrange([1, -2, 3, -4, 5], 5), [1, -2, 3, -4, 5])

    def test_boundary_conditions(self):
        self.assertEqual(re_arrange([], 0), [])
        self.assertEqual(re_arrange([1], 1), [1])
        self.assertEqual(re_arrange([-1], 1), [-1])

    def test_edge_cases(self):
        self.assertEqual(re_arrange([1, -1, 2, -2, 3, -3], 6), [1, -1, 2, -2, 3, -3])
        self.assertEqual(re_arrange([-1, 1, -2, 2, -3, 3], 6), [-1, 1, -2, 2, -3, 3])

    def test_complex_cases(self):
        self.assertEqual(re_arrange([1, -1, 2, -2, 3, -3, 4, -4], 8), [1, -1, 2, -2, 3, -3, 4, -4])
        self.assertEqual(re_arrange([-1, 1, -2, 2, -3, 3, -4, 4], 8), [-1, 1, -2, 2, -3, 3, -4, 4])
