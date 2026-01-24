import unittest
from mbpp_390_code import add_string

class TestAddString(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(add_string([]), [])

    def test_single_element_list(self):
        self.assertEqual(add_string(["a"]), ["a"])

    def test_multiple_elements_list(self):
        self.assertEqual(add_string(["a", "b", "c"]), ["a", "b", "c"])

    def test_string_format_with_numbers(self):
        self.assertEqual(add_string([1, 2, 3]), ["1", "2", "3"])

    def test_string_format_with_negative_numbers(self):
        self.assertEqual(add_string([-1, -2, -3]), ["-1", "-2", "-3"])

    def test_string_format_with_floats(self):
        self.assertEqual(add_string([1.1, 2.2, 3.3]), ["1.1", "2.2", "3.3"])

    def test_string_format_with_empty_string(self):
        self.assertEqual(add_string(["", "a", "b"]), ["", "a", "b"])
