import unittest
from mbpp_566_code import sum_digits

class TestSumDigits(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(sum_digits(0), 0)
        self.assertEqual(sum_digits(12), 3)
        self.assertEqual(sum_digits(100), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_digits(-123), 6)
        self.assertEqual(sum_digits(999), 18)
        self.assertEqual(sum_digits(1024), 6)

    def test_complex_inputs(self):
        self.assertEqual(sum_digits(123456), 35)
        self.assertEqual(sum_digits(1230456), 9)
        self.assertEqual(sum_digits(123000456), 1)
