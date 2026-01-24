import unittest
from mbpp_365_code import count_Digit

class TestCountDigit(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(count_Digit(123), 3)
        self.assertEqual(count_Digit(987654321), 10)

    def test_zero(self):
        self.assertEqual(count_Digit(0), 0)

    def test_negative_integer(self):
        self.assertEqual(count_Digit(-123), 3)
        self.assertEqual(count_Digit(-987654321), 10)

    def test_floats(self):
        self.assertEqual(count_Digit(123.45), 1)
        self.assertEqual(count_Digit(-123.45), 1)

    def test_large_positive_integer(self):
        self.assertEqual(count_Digit(10**20), 20)

    def test_large_negative_integer(self):
        self.assertEqual(count_Digit(-10**20), 20)

    def test_string(self):
        with self.assertRaises(ValueError):
            count_Digit('abc')

    def test_list(self):
        with self.assertRaises(TypeError):
            count_Digit([1, 2, 3])
