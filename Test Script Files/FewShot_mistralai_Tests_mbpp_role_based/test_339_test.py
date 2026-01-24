import unittest
from mbpp_339_code import find_Divisor

class TestFindDivisor(unittest.TestCase):
    def test_same_number(self):
        self.assertEqual(find_Divisor(4, 4), 4)

    def test_positive_numbers(self):
        self.assertEqual(find_Divisor(6, 3), 2)
        self.assertEqual(find_Divisor(8, 2), 2)
        self.assertEqual(find_Divisor(10, 5), 2)

    def test_zero(self):
        self.assertEqual(find_Divisor(0, 0), 0)
        self.assertEqual(find_Divisor(0, 2), 2)

    def test_negative_numbers(self):
        self.assertEqual(find_Divisor(-6, 3), 2)
        self.assertEqual(find_Divisor(-8, -2), 2)
        self.assertEqual(find_Divisor(-10, -5), 2)

    def test_one(self):
        self.assertEqual(find_Divisor(1, 1), 1)
        self.assertEqual(find_Divisor(1, 2), None)
