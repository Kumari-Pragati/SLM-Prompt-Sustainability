import unittest
from mbpp_965_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(camel_to_snake("helloWorld"), "hello_world")
        self.assertEqual(camel_to_snake("abc"), "abc")
        self.assertEqual(camel_to_snake("CamelCase"), "camel_case")

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(camel_to_snake(""), "")
        self.assertEqual(camel_to_snake("abc123"), "abc_123")
        self.assertEqual(camel_to_snake("ALLCAPS"), "allcaps")

    def test_complex_and_corner_cases(self):
        self.assertEqual(camel_to_snake("CamelCaseWithNumbers123"), "camel_case_with_numbers_123")
        self.assertEqual(camel_to_snake("CamelCaseWithUnderscores"), "camel_case_with_underscores")
        self.assertEqual(camel_to_snake("CamelCaseWithSpecialChars!@#"), "camel_case_with_special_chars")
