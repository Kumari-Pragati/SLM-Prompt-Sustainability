import unittest
from mbpp_339_code import find_Divisor

class TestFindDivisor(unittest.TestCase):

    def test_same_numbers(self):
        self.assertEqual(find_Divisor(5, 5), 5)
        self.assertEqual(find_Divisor(10, 10), 10)

    def test_different_numbers(self):
        self.assertEqual(find_Divisor(5, 10), 2)
        self.assertEqual(find_Divisor(15, 30), 2)

    def test_zero(self):
        self.assertEqual(find_Divisor(0, 10), 2)
        self.assertEqual(find_Divisor(10, 0), 2)

    def test_negative_numbers(self):
        self.assertEqual(find_Divisor(-5, -10), 2)
        self.assertEqual(find_Divisor(-15, 30), 2)

    def test_same_negative_numbers(self):
        self.assertEqual(find_Divisor(-5, -5), -5)
        self.assertEqual(find_Divisor(-10, -10), -10)
