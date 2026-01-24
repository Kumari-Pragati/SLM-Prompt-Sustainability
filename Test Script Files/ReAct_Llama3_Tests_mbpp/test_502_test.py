import unittest
from mbpp_502_code import find

class TestFindFunction(unittest.TestCase):

    def test_find_positive_numbers(self):
        self.assertEqual(find(10, 3), 1)

    def test_find_negative_numbers(self):
        self.assertEqual(find(-10, 3), -1)

    def test_find_zero(self):
        self.assertEqual(find(0, 3), 0)

    def test_find_zero_modulus(self):
        self.assertEqual(find(0, 0), 0)

    def test_find_negative_zero(self):
        self.assertEqual(find(-10, 0), -10)

    def test_find_large_numbers(self):
        self.assertEqual(find(1000, 3), 1)

    def test_find_large_negative_numbers(self):
        self.assertEqual(find(-1000, 3), -1)

    def test_find_large_negative_zero(self):
        self.assertEqual(find(-1000, 0), -1000)
