import unittest
from mbpp_59_code import is_octagonal

class TestIsOctagonal(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(is_octagonal(1), 1)
        self.assertEqual(is_octagonal(2), 10)
        self.assertEqual(is_octagonal(3), 27)
        self.assertEqual(is_octagonal(4), 50)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(is_octagonal(0), 0)
        self.assertEqual(is_octagonal(10), 300)
        self.assertEqual(is_octagonal(100), 30000)

    def test_corner_cases(self):
        self.assertEqual(is_octagonal(1000), 3000000)
        self.assertEqual(is_octagonal(10000), 300000000)
