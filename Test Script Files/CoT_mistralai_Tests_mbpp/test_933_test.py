import unittest
from mbpp_933_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(camel_to_snake(""), "")

    def test_single_word(self):
        self.assertEqual(camel_to_snake("CamelCase"), "camel_case")

    def test_multiple_words(self):
        self.assertEqual(camel_to_snake("PascalCase"), "pascal_case")

    def test_mixed_case(self):
        self.assertEqual(camel_to_snake("MixedCase"), "mixed_case")

    def test_number_in_middle(self):
        self.assertEqual(camel_to_snake("CamelNumberCase"), "camel_number_case")

    def test_number_at_start(self):
        self.assertEqual(camel_to_snake("123CamelCase"), "123_camel_case")

    def test_number_at_end(self):
        self.assertEqual(camel_to_snake("CamelCase456"), "camel_case_456")

    def test_number_in_middle_and_end(self):
        self.assertEqual(camel_to_snake("123Camel456Case"), "123_camel_456_case")

    def test_invalid_input(self):
        self.assertRaises(TypeError, camel_to_snake, 123)
        self.assertRaises(TypeError, camel_to_snake, None)
        self.assertRaises(TypeError, camel_to_snake, [])
        self.assertRaises(TypeError, camel_to_snake, ())
