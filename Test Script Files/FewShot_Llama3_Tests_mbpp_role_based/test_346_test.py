import unittest
from mbpp_346_code import zigzag

class TestZigzag(unittest.TestCase):
    def test_zero_and_zero(self):
        self.assertEqual(zigzag(0, 0), 1)

    def test_zero_and_nonzero(self):
        self.assertEqual(zigzag(0, 1), 0)

    def test_nonzero_and_nonzero(self):
        self.assertEqual(zigzag(2, 1), 2)

    def test_nonzero_and_zero(self):
        self.assertEqual(zigzag(2, 0), 1)

    def test_negative_n(self):
        self.assertEqual(zigzag(-2, 1), 1)

    def test_negative_k(self):
        self.assertEqual(zigzag(2, -1), 1)

    def test_large_n_and_k(self):
        self.assertEqual(zigzag(10, 5), 15)
