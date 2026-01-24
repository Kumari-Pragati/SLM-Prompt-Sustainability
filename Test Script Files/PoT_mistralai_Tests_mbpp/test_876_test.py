import unittest
from mbpp_876_code import lcm

class TestLcm(unittest.TestCase):
    def test_lcm_typical(self):
        self.assertEqual(lcm(2, 4), 4)
        self.assertEqual(lcm(4, 2), 4)
        self.assertEqual(lcm(6, 9), 18)
        self.assertEqual(lcm(9, 6), 18)

    def test_lcm_edge(self):
        self.assertEqual(lcm(0, 4), 0)
        self.assertEqual(lcm(4, 0), 0)
        self.assertEqual(lcm(1, 1), 1)
        self.assertEqual(lcm(-2, 4), 4)
        self.assertEqual(lcm(4, -2), 4)

    def test_lcm_boundary(self):
        self.assertEqual(lcm(1, 2), 2)
        self.assertEqual(lcm(2, 1), 2)
        self.assertEqual(lcm(1, 0), 0)
        self.assertEqual(lcm(0, 1), 0)
