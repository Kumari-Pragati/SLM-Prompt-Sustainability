import unittest
from mbpp_398_code import sum_of_digits

class TestSumOfDigits(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_of_digits([]), 0)

    def test_single_number(self):
        self.assertEqual(sum_of_digits([123]), 6)
        self.assertEqual(sum_of_digits([-123]), 6)

    def test_multiple_numbers(self):
        self.assertEqual(sum_of_digits([123, 456, -789]), 21 + 6 + (-9))

    def test_mixed_types(self):
        self.assertEqual(sum_of_digits([123, 'abc', 456]), 6 + 0 + 456)

    def test_floats(self):
        self.assertEqual(sum_of_digits([123.456]), 3 + 4 + 5)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_digits([-123, 456, -789]), (-123) + 456 + (-789))

    def test_large_numbers(self):
        self.assertEqual(sum_of_digits([123456789]), 36)

    def test_zero(self):
        self.assertEqual(sum_of_digits([0]), 0)

    def test_invalid_input(self):
        self.assertRaises(TypeError, sum_of_digits, ['a', 'b', 'c'])
