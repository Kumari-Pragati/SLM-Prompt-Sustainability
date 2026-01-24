import unittest
from mbpp_61_code import count_Substrings

class TestCountSubstrings(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Substrings('123', 3), 1)

    def test_edge_case_with_single_digit(self):
        self.assertEqual(count_Substrings('1', 1), 0)

    def test_edge_case_with_all_same_digits(self):
        self.assertEqual(count_Substrings('111', 3), 3)

    def test_edge_case_with_all_different_digits(self):
        self.assertEqual(count_Substrings('12345', 5), 5)

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            count_Substrings(123, 3)

    def test_invalid_input_n(self):
        with self.assertRaises(TypeError):
            count_Substrings('123', '3')

    def test_invalid_input_string_and_n(self):
        with self.assertRaises(TypeError):
            count_Substrings(123, '3')
