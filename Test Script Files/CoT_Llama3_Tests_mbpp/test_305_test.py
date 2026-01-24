import unittest
from mbpp_305_code import start_withp

class TestStartWithp(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(start_withp(["Pete is a programmer", "Pam is a programmer"]), ('Pete', 'programmer'))
    def test_edge_case_empty_list(self):
        self.assertIsNone(start_withp([]))
    def test_edge_case_single_element_list(self):
        self.assertIsNone(start_withp(["Pete"]))
    def test_edge_case_single_element_list_with_spaces(self):
        self.assertIsNone(start_withp(["Pete "]))
    def test_edge_case_single_element_list_with_punctuation(self):
        self.assertIsNone(start_withp(["Pete."]))
    def test_edge_case_single_element_list_with_punctuation_and_spaces(self):
        self.assertIsNone(start_withp(["Pete. "]))
    def test_edge_case_single_element_list_with_punctuation_and_spaces_and_uppercase(self):
        self.assertIsNone(start_withp(["Pete. "]))
    def test_edge_case_single_element_list_with_punctuation_and_spaces_and_uppercase_and_numbers(self):
        self.assertIsNone(start_withp(["Pete. 123"]))
    def test_edge_case_single_element_list_with_punctuation_and_spaces_and_uppercase_and_numbers_and_special_chars(self):
        self.assertIsNone(start_withp(["Pete. 123!@#"]))
    def test_edge_case_single_element_list_with_punctuation_and_spaces_and_uppercase_and_numbers_and_special_chars_and_newline(self):
        self.assertIsNone(start_withp(["Pete. 123!@# \n"]))
