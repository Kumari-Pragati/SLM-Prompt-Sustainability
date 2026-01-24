import unittest
from mbpp_339_code import find_Divisor

class TestFindDivisor(unittest.TestCase):

    def test_simple_equal(self):
        self.assertEqual(find_Divisor(5, 5), 5)

    def test_simple_different(self):
        self.assertEqual(find_Divisor(5, 6), 2)

    def test_zero(self):
        self.assertEqual(find_Divisor(0, 1), 2)
        self.assertEqual(find_Divisor(1, 0), 2)

    def test_negative(self):
        self.assertEqual(find_Divisor(-5, -3), -3)
        self.assertEqual(find_Divisor(-3, -5), -3)

    def test_large_numbers(self):
        self.assertEqual(find_Divisor(1000000, 2), 2)
        self.assertEqual(find_Divisor(2, 1000000), 2)

    def test_non_integer(self):
        self.assertEqual(find_Divisor(5.0, 2), 2)
        self.assertEqual(find_Divisor(2, 5.0), 2)
