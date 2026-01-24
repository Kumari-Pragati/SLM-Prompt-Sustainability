import unittest
from mbpp_59_code import is_octagonal

class TestIsOctagonal(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(is_octagonal(1), 1)
        self.assertEqual(is_octagonal(2), 10)
        self.assertEqual(is_octagonal(3), 27)
        self.assertEqual(is_octagonal(4), 50)
        self.assertEqual(is_octagonal(5), 77)

    def test_edge_cases(self):
        self.assertEqual(is_octagonal(0), 0)
        self.assertEqual(is_octagonal(100), 39800)
        self.assertEqual(is_octagonal(1000), 3998000)

    def test_negative_numbers(self):
        self.assertEqual(is_octagonal(-1), -1)
        self.assertEqual(is_octagonal(-2), -10)
        self.assertEqual(is_octagonal(-3), -27)
        self.assertEqual(is_octagonal(-4), -50)
        self.assertEqual(is_octagonal(-5), -77)

    def test_large_numbers(self):
        self.assertEqual(is_octagonal(10000), 399980000)
