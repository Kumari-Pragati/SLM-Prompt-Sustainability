import unittest
from mbpp_169_code import get_pell

class TestGetPell(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(get_pell(1), 1)
        self.assertEqual(get_pell(2), 2)
        self.assertEqual(get_pell(3), 2)
        self.assertEqual(get_pell(4), 3)
        self.assertEqual(get_pell(5), 5)
        self.assertEqual(get_pell(6), 7)
        self.assertEqual(get_pell(7), 11)
        self.assertEqual(get_pell(8), 13)
        self.assertEqual(get_pell(9), 17)
        self.assertEqual(get_pell(10), 23)

    def test_zero(self):
        self.assertEqual(get_pell(0), 0)

    def test_negative_integer(self):
        self.assertEqual(get_pell(-1), 0)
        self.assertEqual(get_pell(-2), 0)

    def test_large_integer(self):
        self.assertEqual(get_pell(1000), 2679)
