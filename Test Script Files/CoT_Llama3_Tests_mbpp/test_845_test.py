import unittest
from mbpp_845_code import find_Digits

class TestFindDigits(unittest.TestCase):
    def test_negative_input(self):
        self.assertEqual(find_Digits(-1), 0)

    def test_single_digit_input(self):
        self.assertEqual(find_Digits(0), 1)
        self.assertEqual(find_Digits(1), 1)

    def test_multiple_digits_input(self):
        self.assertEqual(find_Digits(10), 2)
        self.assertEqual(find_Digits(100), 3)
        self.assertEqual(find_Digits(1000), 4)

    def test_edge_cases(self):
        self.assertEqual(find_Digits(0.5), 1)
        self.assertEqual(find_Digits(1.5), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Digits('a')
