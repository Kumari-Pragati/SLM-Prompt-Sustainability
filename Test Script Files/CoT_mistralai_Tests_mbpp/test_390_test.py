import unittest
from mbpp_390_code import add_string

class TestAddString(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(add_string([], "{}"), [])

    def test_single_element_list(self):
        self.assertEqual(add_string([1], "{}"), ["1"])

    def test_multiple_elements_list(self):
        self.assertEqual(add_string([1, 2, 3], "{}"), ["1", "2", "3"])

    def test_list_with_string(self):
        self.assertEqual(add_string(["Hello", "World"], "{}"), ["Hello", "World"])

    def test_list_with_float(self):
        self.assertEqual(add_string([3.14], "{}"), ["3.14"])

    def test_list_with_negative_integer(self):
        self.assertEqual(add_string([-1], "{}"), ["-1"])

    def test_list_with_empty_string(self):
        self.assertEqual(add_string([""], "{}"), [""])

    def test_list_with_none(self):
        self.assertEqual(add_string([None], "{}"), ["None"])

    def test_list_with_mixed_types(self):
        self.assertEqual(add_string([1, "Hello", 3.14, None], "{}"), ["1", "Hello", "3.14", "None"])

    def test_string_with_format_specifier(self):
        self.assertEqual(add_string([1, 2, 3], "{} {}"), ["1", "2", "3"])

    def test_string_with_multiple_format_specifiers(self):
        self.assertEqual(add_string([1, 2, 3, 4], "{} {} {}", "{} {}"), ["1 2", "3 4"])

    def test_string_with_invalid_format_specifier(self):
        self.assertRaises(ValueError, lambda: add_string([1], "{}x"))
