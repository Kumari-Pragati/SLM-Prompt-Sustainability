import unittest
from mbpp_109_code import odd_Equivalent

class TestOddEquivalent(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(odd_Equivalent("", 5), 0)

    def test_single_digit_string(self):
        self.assertEqual(odd_Equivalent("1", 1), 1)

    def test_multiple_digit_string(self):
        self.assertEqual(odd_Equivalent("11111", 5), 5)

    def test_string_with_no_ones(self):
        self.assertEqual(odd_Equivalent("00000", 5), 0)

    def test_string_with_mixed_digits(self):
        self.assertEqual(odd_Equivalent("10101", 5), 3)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            odd_Equivalent(123, 5)

    def test_invalid_input_type_2(self):
        with self.assertRaises(TypeError):
            odd_Equivalent("123", "five")
