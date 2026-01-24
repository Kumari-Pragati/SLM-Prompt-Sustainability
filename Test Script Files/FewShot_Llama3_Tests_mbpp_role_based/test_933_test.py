import unittest
from mbpp_933_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(camel_to_snake("camelCase"), "camel_case")

    def test_multiple_uppercase(self):
        self.assertEqual(camel_to_snake("multiUpperCamelCase"), "multi_upper_camel_case")

    def test_single_word(self):
        self.assertEqual(camel_to_snake("hello"), "hello")

    def test_empty_string(self):
        self.assertEqual(camel_to_snake(""), "")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            camel_to_snake(123)
