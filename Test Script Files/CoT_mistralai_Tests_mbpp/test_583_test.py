import unittest
from mbpp_583_code import catalan_number

class TestCatalanNumber(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(catalan_number(0), 1)
        self.assertEqual(catalan_number(1), 1)

    def test_positive_numbers(self):
        for i in range(2, 10):
            self.assertEqual(catalan_number(i), 5*(i-1)**2 / (i+1))

    def test_large_number(self):
        self.assertEqual(catalan_number(100), 1367914096)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            catalan_number(-1)

    def test_zero_or_non_integer_input(self):
        with self.assertRaises(TypeError):
            catalan_number(0.5)
            catalan_number("str")
