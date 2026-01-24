import unittest
from mbpp_860_code import check_alphanumeric

class TestCheckAlphanumeric(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check_alphanumeric('abc123'), 'Accept')

    def test_typical_case_with_uppercase(self):
        self.assertEqual(check_alphanumeric('ABC123'), 'Accept')

    def test_typical_case_with_special_characters(self):
        self.assertEqual(check_alphanumeric('abc123!@#'), 'Accept')

    def test_edge_case_with_empty_string(self):
        self.assertEqual(check_alphanumeric(''), 'Discard')

    def test_edge_case_with_only_special_characters(self):
        self.assertEqual(check_alphanumeric('!@#$%^&*'), 'Discard')

    def test_edge_case_with_only_spaces(self):
        self.assertEqual(check_alphanumeric(' '), 'Discard')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            check_alphanumeric(123)
