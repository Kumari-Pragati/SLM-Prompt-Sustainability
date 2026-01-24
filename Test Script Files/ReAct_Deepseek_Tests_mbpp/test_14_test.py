import unittest
from mbpp_14_code import find_Volume

class TestFindVolume(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(find_Volume(10, 20, 30), 3000)

    def test_zero_dimensions(self):
        self.assertEqual(find_Volume(0, 0, 0), 0)

    def test_negative_dimensions(self):
        with self.assertRaises(Exception):
            find_Volume(-10, 20, 30)

    def test_large_numbers(self):
        self.assertAlmostEqual(find_Volume(10000000000, 20000000000, 30000000000), 1.5e21)

    def test_decimal_dimensions(self):
        self.assertAlmostEqual(find_Volume(10.5, 20.5, 30.5), 3238.125)
