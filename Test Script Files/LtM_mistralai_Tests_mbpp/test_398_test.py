import unittest
from mbpp_398_code import sum_of_digits

class TestSumOfDigits(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(sum_of_digits([123, 456]), 9)
        self.assertEqual(sum_of_digits([0]), 0)
        self.assertEqual(sum_of_digits([10, 20, 30]), 6)

    def test_edge_cases(self):
        self.assertEqual(sum_of_digits([-123, 0, 456]), 9)
        self.assertEqual(sum_of_digits([123, -456]), 9)
        self.assertEqual(sum_of_digits([123.456]), 0)
        self.assertEqual(sum_of_digits([123, 'abc']), 0)
        self.assertEqual(sum_of_digits([123, 456, -789]), 9)

    def test_complex_cases(self):
        self.assertEqual(sum_of_digits([1234567890]), 45)
        self.assertEqual(sum_of_digits([12345678901]), 54)
        self.assertEqual(sum_of_digits([123456789012]), 66)
        self.assertEqual(sum_of_digits([1234567890123]), 78)
