import unittest
from mbpp_520_code import get_lcm

class TestGetLCM(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_lcm([2, 4]), 8)
        self.assertEqual(get_lcm([8, 16]), 32)
        self.assertEqual(get_lcm([10, 20]), 100)

    def test_edge_case_1(self):
        self.assertEqual(get_lcm([1, 2]), 2)
        self.assertEqual(get_lcm([2, 1]), 2)

    def test_edge_case_2(self):
        self.assertEqual(get_lcm([0, 4]), 0)
        self.assertEqual(get_lcm([4, 0]), 0)

    def test_edge_case_3(self):
        self.assertEqual(get_lcm([1, 1]), 1)

    def test_boundary_case_1(self):
        self.assertEqual(get_lcm([-2, 4]), 4)
        self.assertEqual(get_lcm([4, -2]), 4)

    def test_boundary_case_2(self):
        self.assertEqual(get_lcm([2147483647, 1]), 2147483647)
        self.assertEqual(get_lcm([1, 2147483647]), 2147483647)
