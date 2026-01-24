import unittest
from mbpp_14_code import find_Volume

class TestFindVolume(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_Volume(2, 3, 4), 24)

    def test_zero(self):
        self.assertEqual(find_Volume(0, 0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(find_Volume(-2, -3, -4), -24)

    def test_zero_and_positive_numbers(self):
        self.assertEqual(find_Volume(0, 2, 3), 6)

    def test_zero_and_negative_numbers(self):
        self.assertEqual(find_Volume(0, -2, -3), -6)

    def test_negative_numbers_and_positive_numbers(self):
        self.assertEqual(find_Volume(-2, 2, 3), -6)

    def test_invalid_input_zero_length(self):
        with self.assertRaises(ValueError):
            find_Volume(0, 3, 4)

    def test_invalid_input_zero_breadth(self):
        with self.assertRaises(ValueError):
            find_Volume(2, 0, 3)

    def test_invalid_input_zero_height(self):
        with self.assertRaises(ValueError):
            find_Volume(2, 3, 0)
