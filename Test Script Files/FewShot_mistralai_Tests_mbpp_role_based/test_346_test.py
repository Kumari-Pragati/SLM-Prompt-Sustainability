import unittest
from mbpp_346_code import zigzag

class TestZigzag(unittest.TestCase):
    def test_zero_and_zero(self):
        self.assertEqual(zigzag(0, 0), 1)

    def test_zero_and_non_zero(self):
        self.assertEqual(zigzag(0, 1), 0)

    def test_positive_and_zero(self):
        self.assertEqual(zigzag(1, 0), 1)

    def test_negative_and_zero(self):
        self.assertEqual(zigzag(-1, 0), 1)

    def test_positive_and_negative(self):
        self.assertEqual(zigzag(2, 1), 1)
        self.assertEqual(zigzag(2, 2), 3)
        self.assertEqual(zigzag(2, 3), 0)

    def test_large_input(self):
        self.assertEqual(zigzag(100, 50), 147857)

    def test_negative_and_large_input(self):
        self.assertEqual(zigzag(-100, 50), 147857)
