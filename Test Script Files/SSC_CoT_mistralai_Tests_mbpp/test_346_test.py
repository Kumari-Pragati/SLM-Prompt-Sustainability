import unittest
from mbpp_346_code import zigzag

class TestZigzag(unittest.TestCase):
    def test_zero_and_zero(self):
        self.assertEqual(zigzag(0, 0), 1)

    def test_zero_and_non_zero(self):
        self.assertEqual(zigzag(0, 1), 0)

    def test_positive_numbers(self):
        self.assertEqual(zigzag(3, 1), 1)
        self.assertEqual(zigzag(3, 2), 2)
        self.assertEqual(zigzag(3, 3), 1)

    def test_negative_numbers(self):
        self.assertEqual(zigzag(-3, 1), 0)
        self.assertEqual(zigzag(-3, 2), 2)
        self.assertEqual(zigzag(-3, 3), 1)

    def test_negative_k(self):
        self.assertEqual(zigzag(3, -1), 0)
        self.assertEqual(zigzag(3, -2), 0)
        self.assertEqual(zigzag(3, -3), 0)

    def test_negative_n(self):
        self.assertEqual(zigzag(-3, 1), 0)
        self.assertEqual(zigzag(-3, 2), 2)
        self.assertEqual(zigzag(-3, 3), 1)
