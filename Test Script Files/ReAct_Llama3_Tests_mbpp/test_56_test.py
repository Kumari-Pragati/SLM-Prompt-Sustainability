import unittest
from mbpp_56_code import check

class TestCheckFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(check(1))
        self.assertTrue(check(2))
        self.assertTrue(check(3))
        self.assertTrue(check(4))
        self.assertTrue(check(5))

    def test_negative_numbers(self):
        self.assertFalse(check(-1))
        self.assertFalse(check(-2))
        self.assertFalse(check(-3))
        self.assertFalse(check(-4))
        self.assertFalse(check(-5))

    def test_zero(self):
        self.assertFalse(check(0))

    def test_large_numbers(self):
        self.assertTrue(check(1000))
        self.assertTrue(check(2000))
        self.assertTrue(check(3000))
        self.assertTrue(check(4000))
        self.assertTrue(check(5000))

    def test_edge_cases(self):
        self.assertFalse(check(1))
        self.assertFalse(check(2))
        self.assertFalse(check(3))
        self.assertFalse(check(4))
        self.assertFalse(check(5))
