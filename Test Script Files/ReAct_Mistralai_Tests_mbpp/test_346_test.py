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

    def test_positive_and_positive(self):
        for n in range(1, 10):
            for k in range(1, n + 1):
                self.assertEqual(zigzag(n, k), zigzag(n, k - 1) + zigzag(n - 1, n - k))

    def test_positive_and_negative(self):
        for n in range(1, 10):
            for k in range(1, n):
                self.assertEqual(zigzag(n, -k), zigzag(n, k))

    def test_negative_and_negative(self):
        for n in range(1, 10):
            for k in range(1, n):
                self.assertEqual(zigzag(-n, -k), zigzag(-n, k))
