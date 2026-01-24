import unittest
from mbpp_169_code import get_pell

class TestGetPell(unittest.TestCase):
    def test_small_numbers(self):
        self.assertEqual(get_pell(1), 1)
        self.assertEqual(get_pell(2), 2)

    def test_typical_numbers(self):
        self.assertEqual(get_pell(5), 11)
        self.assertEqual(get_pell(10), 57)
        self.assertEqual(get_pell(20), 267)

    def test_large_numbers(self):
        self.assertEqual(get_pell(100), 4759)
        self.assertEqual(get_pell(1000), 239031)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, get_pell, -1)
        self.assertRaises(ValueError, get_pell, 0)
