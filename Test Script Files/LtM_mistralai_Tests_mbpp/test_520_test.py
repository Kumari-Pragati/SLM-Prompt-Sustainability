import unittest
from mbpp_520_code import get_lcm

class TestGetLCM(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(get_lcm([2, 4]), 8)
        self.assertEqual(get_lcm([8, 16]), 16)
        self.assertEqual(get_lcm([10, 20]), 100)

    def test_edge_cases(self):
        self.assertEqual(get_lcm([1, 2]), 2)
        self.assertEqual(get_lcm([2, 1]), 2)
        self.assertEqual(get_lcm([0, 4]), 0)
        self.assertEqual(get_lcm([4, 0]), 0)
        self.assertEqual(get_lcm([-2, 3]), 6)
        self.assertEqual(get_lcm([3, -2]), 6)

    def test_boundary_cases(self):
        self.assertEqual(get_lcm([2147483647, 1]), 2147483647)
        self.assertEqual(get_lcm([1, 2147483647]), 2147483647)
        self.assertEqual(get_lcm([-2147483648, 1]), 2147483648)
        self.assertEqual(get_lcm([1, -2147483648]), 2147483648)

    def test_complex_cases(self):
        self.assertEqual(get_lcm([1, 2, 3, 4, 5]), 120)
        self.assertEqual(get_lcm([1, 2, 3, 4, 5, 6]), 720)
        self.assertEqual(get_lcm([1, 2, 3, 4, 5, 6, 7]), 5040)
