import unittest
from mbpp_876_code import lcm

class TestLcm(unittest.TestCase):
    def test_lcm_normal(self):
        self.assertEqual(lcm(2, 4), 4)
        self.assertEqual(lcm(12, 16), 48)
        self.assertEqual(lcm(81, 12), 36)

    def test_lcm_edge_cases(self):
        self.assertEqual(lcm(0, 4), 0)
        self.assertEqual(lcm(4, 0), 0)
        self.assertEqual(lcm(1, 1), 1)
        self.assertEqual(lcm(-2, 4), 4)
        self.assertEqual(lcm(4, -2), 4)

    def test_lcm_boundary(self):
        self.assertEqual(lcm(1, 2), 2)
        self.assertEqual(lcm(2, 1), 2)
        self.assertEqual(lcm(1, 1), 1)
        self.assertEqual(lcm(2**63 - 1, 2), 2**63)
        self.assertEqual(lcm(2, 2**63 - 1), 2**63)
