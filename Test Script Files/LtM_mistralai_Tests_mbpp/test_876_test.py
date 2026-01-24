import unittest
from mbpp_876_code import lcm

class TestLcm(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(lcm(2, 4), 4)
        self.assertEqual(lcm(4, 2), 4)
        self.assertEqual(lcm(6, 9), 18)
        self.assertEqual(lcm(9, 6), 18)

    def test_edge_cases(self):
        self.assertEqual(lcm(1, 1), 1)
        self.assertEqual(lcm(0, 4), 0)
        self.assertEqual(lcm(4, 0), 0)
        self.assertEqual(lcm(-2, 3), 6)
        self.assertEqual(lcm(3, -2), 6)

    def test_boundary_cases(self):
        self.assertEqual(lcm(2147483647, 1), 2147483647)
        self.assertEqual(lcm(1, 2147483647), 1)
