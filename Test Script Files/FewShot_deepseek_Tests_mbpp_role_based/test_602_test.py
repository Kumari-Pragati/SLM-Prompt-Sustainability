import unittest
from mbpp_602_code import first_repeated_char

class TestFirstRepeatedChar(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(first_repeated_char('abcab'), 'a')

    def test_edge_case_single_char(self):
        self.assertEqual(first_repeated_char('a'), 'None')

    def test_boundary_case_empty_string(self):
        self.assertEqual(first_repeated_char(''), 'None')

    def test_boundary_case_repeated_last_char(self):
        self.assertEqual(first_repeated_char('abcba'), 'b')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            first_repeated_char(123)
