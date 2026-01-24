import unittest
from mbpp_339_code import find_Divisor

class TestFindDivisor(unittest.TestCase):

    def test_same_numbers(self):
        self.assertEqual(find_Divisor(5, 5), 5)

    def test_different_numbers(self):
        self.assertEqual(find_Divisor(10, 20), 2)

    def test_zero_input(self):
        self.assertEqual(find_Divisor(0, 10), 2)

    def test_negative_numbers(self):
        self.assertEqual(find_Divisor(-5, -15), 2)

    def test_one_input(self):
        self.assertEqual(find_Divisor(1, 1), 1)
