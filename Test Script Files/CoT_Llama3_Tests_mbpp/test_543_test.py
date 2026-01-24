import unittest
from mbpp_543_code import count_digits

class TestCountDigits(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(count_digits(123, 456), 3)
        self.assertEqual(count_digits(789, 012), 3)
        self.assertEqual(count_digits(100, 200), 3)

    def test_edge_cases(self):
        self.assertEqual(count_digits(0, 0), 0)
        self.assertEqual(count_digits(0, 1), 1)
        self.assertEqual(count_digits(1, 0), 1)

    def test_boundary_cases(self):
        self.assertEqual(count_digits(999, 999), 4)
        self.assertEqual(count_digits(1000, 1000), 4)
        self.assertEqual(count_digits(9999, 9999), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_digits('abc', 123)
        with self.assertRaises(TypeError):
            count_digits(123, 'abc')
        with self.assertRaises(TypeError):
            count_digits('abc', 'def')
