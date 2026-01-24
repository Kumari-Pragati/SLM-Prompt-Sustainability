import unittest
from mbpp_771_code import check_expression

class TestCheckExpression(unittest.TestCase):
    def test_typical_valid_expression(self):
        self.assertTrue(check_expression("((()))"))
        self.assertTrue(check_expression("({[()]})"))
        self.assertTrue(check_expression("({[()]})"))

    def test_typical_invalid_expression(self):
        self.assertFalse(check_expression("((("))
        self.assertFalse(check_expression("({[)]}}"))
        self.assertFalse(check_expression("({[()]}}"))

    def test_edge_case_empty_expression(self):
        self.assertTrue(check_expression(""))

    def test_edge_case_single_character_expression(self):
        self.assertTrue(check_expression("a"))
        self.assertTrue(check_expression("("))
        self.assertTrue(check_expression("{"))
        self.assertTrue(check_expression("["))

    def test_edge_case_single_opening_character_expression(self):
        self.assertFalse(check_expression("("))
        self.assertFalse(check_expression("{"))
        self.assertFalse(check_expression("["))

    def test_edge_case_single_closing_character_expression(self):
        self.assertFalse(check_expression(")"))
        self.assertFalse(check_expression("}"))
        self.assertFalse(check_expression("]"))

    def test_edge_case_mismatched_opening_and_closing_characters(self):
        self.assertFalse(check_expression("({[)]}}"))
        self.assertFalse(check_expression("({[()]}}"))
        self.assertFalse(check_expression("({[()]}}"))

    def test_edge_case_mismatched_opening_and_closing_characters_with_spaces(self):
        self.assertFalse(check_expression("({ [ ] ] } }"))
        self.assertFalse(check_expression("({ [ ] ] } }"))

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            check_expression(123)

    def test_invalid_input_non_string_with_spaces(self):
        with self.assertRaises(TypeError):
            check_expression("123 456")
