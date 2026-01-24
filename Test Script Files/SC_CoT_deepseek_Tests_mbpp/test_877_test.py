import unittest
from mbpp_877_code import sort_String

class TestSortString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_String("hello"), "ehllo")

    def test_empty_string(self):
        self.assertEqual(sort_String(""), "")

    def test_single_character_string(self):
        self.assertEqual(sort_String("a"), "a")

    def test_string_with_numbers(self):
        self.assertEqual(sort_String("123456"), "123456")

    def test_string_with_special_characters(self):
        self.assertEqual(sort_String("@#$%^&*"), "@#$%^*")

    def test_string_with_mixed_case(self):
        self.assertEqual(sort_String("HeLlO"), "HeLO")

    def test_string_with_repeated_characters(self):
        self.assertEqual(sort_String("aabbcc"), "aabbcc")

    def test_string_with_spaces(self):
        self.assertEqual(sort_String("hello world"), " dehllloorw")

    def test_string_with_unicode_characters(self):
        self.assertEqual(sort_String("àáâãäå"), "àáâãäå")

    def test_string_with_none(self):
        with self.assertRaises(TypeError):
            sort_String(None)
