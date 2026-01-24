import unittest
from mbpp_765_code import is_polite

class TestIsPolite(unittest.TestCase):
    def test_positive_integer(self):
        self.assertGreaterEqual(is_polite(1), 2)

    def test_zero(self):
        self.assertGreaterEqual(is_polite(0), 1)

    def test_negative_integer(self):
        self.assertLessEqual(is_polite(-1), 0)

    def test_float(self):
        self.assertRaises(TypeError, is_polite, 3.14)

    def test_string(self):
        self.assertRaises(TypeError, is_polite, 'hello')
