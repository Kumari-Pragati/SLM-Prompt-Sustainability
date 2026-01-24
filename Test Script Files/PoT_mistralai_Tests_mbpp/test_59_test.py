import unittest
from mbpp_59_code import is_octagonal

class TestIsOctagonal(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(is_octagonal(1), 3)
        self.assertEqual(is_octagonal(2), 8)
        self.assertEqual(is_octagonal(3), 13)
        self.assertEqual(is_octagonal(4), 20)
        self.assertEqual(is_octagonal(5), 23)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(is_octagonal(0), 0)
        self.assertEqual(is_octagonal(10), 105)
        self.assertEqual(is_octagonal(-1), -3)
        self.assertEqual(is_octagonal(20), 380)
