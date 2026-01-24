import unittest
from mbpp_887_code import is_odd

class TestIsOdd(unittest.TestCase):

    def test_positive_odd(self):
        self.assertTrue(is_odd(1))

    def test_positive_even(self):
        self.assertFalse(is_odd(2))

    def test_negative_odd(self):
        self.assertTrue(is_odd(-1))

    def test_negative_even(self):
        self.assertFalse(is_odd(-2))

    def test_zero(self):
        self.assertFalse(is_odd(0))

    def test_large_odd(self):
        self.assertTrue(is_odd(9999999999999999999))

    def test_large_even(self):
        self.assertFalse(is_odd(10000000000000000000))

    def test_float_odd(self):
        self.assertTrue(is_odd(1.5))

    def test_float_even(self):
        self.assertFalse(is_odd(2.5))

    def test_string(self):
        self.assertFalse(is_odd('1'))

    def test_list(self):
        self.assertFalse(is_odd([1]))

    def test_tuple(self):
        self.assertFalse(is_odd((1,)))

    def test_dict(self):
        self.assertFalse(is_odd({'1': 1}))
