import unittest
from mbpp_169_code import get_pell

class TestGetPell(unittest.TestCase):

    def test_get_pell_small_numbers(self):
        self.assertEqual(get_pell(0), 0)
        self.assertEqual(get_pell(1), 1)
        self.assertEqual(get_pell(2), 2)

    def test_get_pell_large_numbers(self):
        self.assertEqual(get_pell(10), 144)
        self.assertEqual(get_pell(20), 17711)
        self.assertEqual(get_pell(30), 196418)

    def test_get_pell_negative_numbers(self):
        with self.assertRaises(ValueError):
            get_pell(-1)
