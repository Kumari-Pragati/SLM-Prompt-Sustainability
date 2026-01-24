import unittest
from mbpp_339_code import find_Divisor

class TestFindDivisor(unittest.TestCase):
    def test_equal_numbers(self):
        self.assertEqual(find_Divisor(5, 5), 5)

    def test_non_equal_numbers(self):
        self.assertEqual(find_Divisor(5, 2), 2)

    def test_zero_divisor(self):
        with self.assertRaises(ZeroDivisionError):
            find_Divisor(5, 0)

    def test_negative_numbers(self):
        self.assertEqual(find_Divisor(-5, -5), -5)

    def test_mixed_sign_numbers(self):
        self.assertEqual(find_Divisor(-5, 5), 2)
