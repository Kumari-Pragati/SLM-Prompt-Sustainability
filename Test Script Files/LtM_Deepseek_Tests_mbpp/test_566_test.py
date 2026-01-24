import unittest
from mbpp_566_code import sum_digits

class TestSumDigits(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(sum_digits(123), 6)
        self.assertEqual(sum_digits(456), 15)
        self.assertEqual(sum_digits(789), 24)

    def test_edge_conditions(self):
        self.assertEqual(sum_digits(0), 0)
        self.assertEqual(sum_digits(10), 1)
        self.assertEqual(sum_digits(999), 27)

    def test_complex_cases(self):
        self.assertEqual(sum_digits(123456789), 45)
        self.assertEqual(sum_digits(987654321), 45)
