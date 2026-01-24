import unittest
from mbpp_56_code import check

class TestCheck(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(check(1))

    def test_even_numbers(self):
        self.assertTrue(check(2))

    def test_odd_numbers(self):
        self.assertTrue(check(3))

    def test_large_numbers(self):
        self.assertTrue(check(100))

    def test_zero(self):
        with self.assertRaises(TypeError):
            check(0)

    def test_negative_numbers(self):
        with self.assertRaises(TypeError):
            check(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            check(1.5)
