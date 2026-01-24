import unittest
from mbpp_774_code import check_email

class TestCheckEmail(unittest.TestCase):
    def test_simple_valid_email(self):
        self.assertEqual(check_email("test@example.com"), "Valid Email")

    def test_simple_valid_email_with_dot(self):
        self.assertEqual(check_email("test.example@com"), "Valid Email")

    def test_simple_valid_email_with_underscore(self):
        self.assertEqual(check_email("test_example@com"), "Valid Email")

    def test_simple_valid_email_with_numbers(self):
        self.assertEqual(check_email("test123@example.com"), "Valid Email")

    def test_simple_valid_email_with_numbers_and_underscore(self):
        self.assertEqual(check_email("test123_example@com"), "Valid Email")

    def test_simple_valid_email_with_numbers_and_dot(self):
        self.assertEqual(check_email("test123.example@com"), "Valid Email")

    def test_simple_valid_email_with_numbers_underscore_and_dot(self):
        self.assertEqual(check_email("test123_example.com"), "Valid Email")

    def test_edge_case_min_length_domain(self):
        self.assertEqual(check_email("test@ex.com"), "Valid Email")

    def test_edge_case_max_length_domain(self):
        self.assertEqual(check_email("test@example.co.uk"), "Valid Email")

    def test_edge_case_min_length_domain_with_numbers(self):
        self.assertEqual(check_email("test1@ex.com"), "Valid Email")

    def test_edge_case_max_length_domain_with_numbers(self):
        self.assertEqual(check_email("test1@example.co.uk"), "Valid Email")

    def test_edge_case_min_length_domain_with_underscore(self):
        self.assertEqual(check_email("test_@ex.com"), "Valid Email")

    def test_edge_case_max_length_domain_with_underscore(self):
        self.assertEqual(check_email("test_@example.co.uk"), "Valid Email")

    def test_edge_case_min_length_domain_with_numbers_and_underscore(self):
        self.assertEqual(check_email("test1_@ex.com"), "Valid Email")

    def test_edge_case_max_length_domain_with_numbers_and_underscore(self):
        self.assertEqual(check_email("test1_@example.co.uk"), "Valid Email")

    def test_edge_case_min_length_domain_with_numbers_underscore_and_dot(self):
        self.assertEqual(check_email("test1_example.ex.com"), "Valid Email")

    def test_edge_case_max_length_domain_with_numbers_underscore_and_dot(self):
        self.assertEqual(check_email("test1_example.co.uk"), "Valid Email")

    def test_invalid_email_no_at_symbol(self):
        self.assertEqual(check_email("testexample.com"), "Invalid Email")

    def test_invalid_email_no_dot(self):
        self.assertEqual(check_email("test@examplecom"), "Invalid Email")

    def test_invalid_email_no_domain(self):
        self.assertEqual(check_email("test@"), "Invalid Email")

    def test_invalid_email_no_extension(self):
        self.assertEqual(check_email("test@example"), "Invalid Email")

    def test_invalid_email_no_extension_with_numbers(self):
        self.assertEqual(check_email("test1@example"), "Invalid Email")

    def test_invalid_email_no_extension_with_underscore(self):
        self.assertEqual(check_email("test_@example"), "Invalid Email")

    def test