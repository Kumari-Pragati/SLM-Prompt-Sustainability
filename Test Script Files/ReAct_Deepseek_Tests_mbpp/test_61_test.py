import unittest
from mbpp_61_code import count_Substrings

class TestCountSubstrings(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Substrings('131', 3), 2)

    def test_edge_case_single_digit(self):
        self.assertEqual(count_Substrings('0', 1), 0)
        self.assertEqual(count_Substrings('1', 1), 0)

    def test_edge_case_all_digits(self):
        self.assertEqual(count_Substrings('11111', 5), 10)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_Substrings('', 0), 0)

    def test_explicitly_handled_error_case(self):
        with self.assertRaises(TypeError):
            count_Substrings(123, '3')
        with self.assertRaises(TypeError):
            count_Substrings('123', 3.0)
