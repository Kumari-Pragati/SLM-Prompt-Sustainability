import unittest
from mbpp_365_code import count_Digit

class TestCountDigit(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(count_Digit(12345), 5)
        self.assertEqual(count_Digit(987654321), 9)

    def test_zero(self):
        self.assertEqual(count_Digit(0), 1)

    def test_negative_numbers(self):
        self.assertEqual(count_Digit(-12345), 5)
        self.assertEqual(count_Digit(-987654321), 9)

    def test_single_digit_numbers(self):
        self.assertEqual(count_Digit(5), 1)
        self.assertEqual(count_Digit(0), 1)

    def test_large_numbers(self):
        self.assertEqual(count_Digit(10**100), 101)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Digit('12345')
        with self.assertRaises(TypeError):
            count_Digit(None)
        with self.assertRaises(TypeError):
            count_Digit([])
        with self.assertRaises(TypeError):
            count_Digit({})
