import unittest
from mbpp_346_code import zigzag

class TestZigzag(unittest.TestCase):

    def test_zero_case(self):
        self.assertEqual(zigzag(0, 0), 1)

    def test_zero_k(self):
        self.assertEqual(zigzag(3, 0), 0)

    def test_positive_numbers(self):
        self.assertEqual(zigzag(3, 2), zigzag(3, 2))
        self.assertEqual(zigzag(4, 2), zigzag(4, 2))
        self.assertEqual(zigzag(5, 3), zigzag(5, 3))

    def test_negative_numbers(self):
        self.assertEqual(zigzag(-3, -2), zigzag(-3, -2))
        self.assertEqual(zigzag(-4, -2), zigzag(-4, -2))
        self.assertEqual(zigzag(-5, -3), zigzag(-5, -3))
