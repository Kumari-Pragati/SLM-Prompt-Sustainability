import unittest
from mbpp_926_code import rencontres_number

class TestRencontresNumber(unittest.TestCase):
    def test_zero_zero(self):
        self.assertEqual(rencontres_number(0, 0), 1)

    def test_one_zero(self):
        self.assertEqual(rencontres_number(1, 0), 0)

    def test_zero_one(self):
        self.assertEqual(rencontres_number(0, 1), 0)

    def test_negative_n(self):
        self.assertRaises(ValueError, lambda: rencontres_number(-1, 0))

    def test_negative_m(self):
        self.assertRaises(ValueError, lambda: rencontres_number(1, -1))

    def test_large_n(self):
        self.assertEqual(rencontres_number(100, 10), expected=10094)

    def test_large_m(self):
        self.assertEqual(rencontres_number(10, 90), expected=10000000000)

    def test_equal_n_m(self):
        self.assertEqual(rencontres_number(5, 5), 1)

    def test_large_difference(self):
        self.assertEqual(rencontres_number(10, 1), expected=10)
