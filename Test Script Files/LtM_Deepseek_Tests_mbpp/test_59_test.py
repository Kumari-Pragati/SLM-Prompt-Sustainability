import unittest
from mbpp_59_code import is_octagonal

class TestIsOctagonal(unittest.TestCase):

    def test_simple_octagonal_numbers(self):
        self.assertEqual(is_octagonal(1), 1)
        self.assertEqual(is_octagonal(2), 10)
        self.assertEqual(is_octagonal(3), 27)
        self.assertEqual(is_octagonal(4), 58)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(is_octagonal(0), 0)
        self.assertEqual(is_octagonal(100), 30800)
        self.assertEqual(is_octagonal(1000), 3000800)

    def test_more_complex_or_corner_cases(self):
        self.assertEqual(is_octagonal(10000), 300008000)
        self.assertEqual(is_octagonal(100000), 30000080000)
