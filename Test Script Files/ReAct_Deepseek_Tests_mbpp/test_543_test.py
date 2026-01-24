import unittest
from mbpp_543_code import count_digits

class TestCountDigits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_digits(123, 456), 6)
        self.assertEqual(count_digits(1000, 999), 4)
        self.assertEqual(count_digits(0, 0), 1)

    def test_edge_cases(self):
        self.assertEqual(count_digits(0, 999999999), 10)
        self.assertEqual(count_digits(999999999, 0), 10)
        self.assertEqual(count_digits(999999999, 999999999), 10)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            count_digits("123", 456)
        with self.assertRaises(TypeError):
            count_digits(123, "456")
        with self.assertRaises(TypeError):
            count_digits("123", "456")
