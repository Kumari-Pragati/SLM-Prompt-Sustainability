import unittest

from mbpp_339_code import find_Divisor

class TestFindDivisor(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Divisor(10, 5), 5)

    def test_same_number(self):
        self.assertEqual(find_Divisor(10, 10), 10)

    def test_zero_input(self):
        self.assertEqual(find_Divisor(0, 10), 2)

    def test_negative_input(self):
        self.assertEqual(find_Divisor(-10, -5), 2)

    def test_large_numbers(self):
        self.assertEqual(find_Divisor(10**6, 10**6), 10**6)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Divisor("10", 5)
