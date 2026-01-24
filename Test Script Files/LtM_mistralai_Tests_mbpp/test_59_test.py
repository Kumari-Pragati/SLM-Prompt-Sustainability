import unittest
from mbpp_59_code import is_octagonal

class TestIsOctagonal(unittest.TestCase):

    def test_simple_positive(self):
        self.assertEqual(is_octagonal(1), 3)
        self.assertEqual(is_octagonal(2), 8)
        self.assertEqual(is_octagonal(3), 13)

    def test_edge_cases(self):
        self.assertEqual(is_octagonal(0), 0)
        self.assertEqual(is_octagonal(10), 103)
        self.assertEqual(is_octagonal(-1), -3)

    def test_complex_cases(self):
        self.assertEqual(is_octagonal(42), 1317)
        self.assertEqual(is_octagonal(100), 30002)
