import unittest
from mbpp_96_code import divisor

class TestDivisor(unittest.TestCase):

    def test_divisor_typical_case(self):
        self.assertEqual(divisor(10), 4)

    def test_divisor_edge_case_1(self):
        self.assertEqual(divisor(1), 1)

    def test_divisor_edge_case_2(self):
        self.assertEqual(divisor(0), 0)

    def test_divisor_invalid_input(self):
        with self.assertRaises(TypeError):
            divisor('a')

    def test_divisor_negative_number(self):
        with self.assertRaises(ValueError):
            divisor(-5)
