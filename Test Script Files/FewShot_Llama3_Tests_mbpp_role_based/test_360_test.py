import unittest
from mbpp_360_code import get_carol

class TestGetCarol(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(get_carol(1), 3)

    def test_negative_integer(self):
        self.assertRaises(TypeError, get_carol, -1)

    def test_zero(self):
        self.assertRaises(TypeError, get_carol, 0)

    def test_non_integer(self):
        self.assertRaises(TypeError, get_carol, 3.5)

    def test_large_integer(self):
        self.assertEqual(get_carol(10), 5764801)
