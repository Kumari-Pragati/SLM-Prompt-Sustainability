import unittest
from mbpp_774_code import check_email

class TestCheckEmail(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check_email('test@example.com'), 'Valid Email')

    def test_edge_case_with_no_username(self):
        self.assertEqual(check_email('@example.com'), 'Invalid Email')

    def test_edge_case_with_no_domain(self):
        self.assertEqual(check_email('test@'), 'Invalid Email')

    def test_boundary_case_with_empty_string(self):
        self.assertEqual(check_email(''), 'Invalid Email')

    def test_corner_case_with_special_characters(self):
        self.assertEqual(check_email('test@exa#mple.com'), 'Invalid Email')

    def test_corner_case_with_numbers_only(self):
        self.assertEqual(check_email('1234567890@example.com'), 'Valid Email')

    def test_corner_case_with_special_characters_in_username(self):
        self.assertEqual(check_email('t@est@exa_mple.com'), 'Invalid Email')
