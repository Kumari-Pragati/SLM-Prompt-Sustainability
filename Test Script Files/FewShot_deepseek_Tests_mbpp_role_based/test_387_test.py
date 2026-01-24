import unittest
from mbpp_387_code import even_or_odd

class TestEvenOrOdd(unittest.TestCase):
    def test_typical_case_even(self):
        self.assertEqual(even_or_odd('8'), 'Even')

    def test_typical_case_odd(self):
        self.assertEqual(even_or_odd('1'), 'Odd')

    def test_boundary_case_last_digit_0(self):
        self.assertEqual(even_or_odd('0'), 'Even')

    def test_boundary_case_last_digit_A(self):
        self.assertEqual(even_or_odd('A'), 'Even')

    def test_boundary_case_last_digit_E(self):
        self.assertEqual(even_or_odd('E'), 'Even')

    def test_boundary_case_last_digit_not_even_or_odd(self):
        self.assertEqual(even_or_odd('B'), 'Odd')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            even_or_odd(123)
