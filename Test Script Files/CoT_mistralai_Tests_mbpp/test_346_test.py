import unittest
from mbpp_346_code import zigzag

class TestZigzag(unittest.TestCase):
    def test_zero_and_zero(self):
        self.assertEqual(zigzag(0, 0), 1)

    def test_zero_and_non_zero(self):
        self.assertEqual(zigzag(0, 1), 0)

    def test_positive_and_zero(self):
        self.assertEqual(zigzag(1, 0), 0)

    def test_positive_and_non_zero(self):
        self.assertEqual(zigzag(1, 1), 1)
        self.assertEqual(zigzag(1, 2), 0)
        self.assertEqual(zigzag(1, 3), 1)

    def test_negative_and_zero(self):
        self.assertEqual(zigzag(-1, 0), 0)

    def test_negative_and_non_zero(self):
        self.assertEqual(zigzag(-1, 1), 0)
        self.assertEqual(zigzag(-1, 2), 1)
        self.assertEqual(zigzag(-1, 3), 0)

    def test_large_input(self):
        self.assertEqual(zigzag(10, 3), 8)
        self.assertEqual(zigzag(10, 4), 12)
        self.assertEqual(zigzag(10, 5), 16)

    def test_negative_large_input(self):
        self.assertEqual(zigzag(-10, 3), 8)
        self.assertEqual(zigzag(-10, 4), 12)
        self.assertEqual(zigzag(-10, 5), 16)
