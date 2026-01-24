import unittest
from mbpp_543_code import count_digits

class TestCountDigits(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_digits(123, 456), 6)
        self.assertEqual(count_digits(987654, 321), 7)

    def test_edge_conditions(self):
        self.assertEqual(count_digits(0, 0), 1)
        self.assertEqual(count_digits(0, 12345), 6)
        self.assertEqual(count_digits(987654321, 0), 9)

    def test_boundary_conditions(self):
        self.assertEqual(count_digits(10**9, 10**9), 10)
        self.assertEqual(count_digits(10**18, 10**18), 19)

    def test_complex_cases(self):
        self.assertEqual(count_digits(1234567890, 9876543210), 10)
        self.assertEqual(count_digits(1234567890123456789, 9876543210987654321), 19)
