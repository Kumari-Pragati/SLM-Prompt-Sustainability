import unittest
from mbpp_45_code import get_gcd

class TestGetGcd(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(get_gcd([2, 3]), 1)
        self.assertEqual(get_gcd([4, 6]), 2)
        self.assertEqual(get_gcd([10, 15]), 5)

    def test_edge_cases(self):
        self.assertEqual(get_gcd([0, 0]), 0)
        self.assertEqual(get_gcd([1, 1]), 1)
        self.assertEqual(get_gcd([2, 2]), 2)

    def test_boundary_cases(self):
        self.assertEqual(get_gcd([1, 2]), 1)
        self.assertEqual(get_gcd([3, 4]), 1)
        self.assertEqual(get_gcd([5, 6]), 1)

    def test_corner_cases(self):
        self.assertEqual(get_gcd([7, 7]), 7)
        self.assertEqual(get_gcd([8, 8]), 8)
        self.assertEqual(get_gcd([9, 9]), 9)
