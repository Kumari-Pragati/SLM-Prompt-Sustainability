import unittest
from mbpp_14_code import find_Volume

class TestFindVolume(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertAlmostEqual(find_Volume(2, 3, 4), 6.0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(find_Volume(-2, -3, -4), -6.0)

    def test_zero(self):
        self.assertEqual(find_Volume(0, 0, 0), 0)

    def test_decimal_numbers(self):
        self.assertAlmostEqual(find_Volume(2.5, 3.5, 4.5), 9.375)

    def test_non_integer_numbers(self):
        self.assertAlmostEqual(find_Volume(2.5, 3, 4), 6.25)
