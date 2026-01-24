import unittest
from mbpp_538_code import string_list_to_tuple

class TestStringListToTuple(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsInstance(string_list_to_tuple([]), tuple)
        self.assertListEqual(string_list_to_tuple([]), [])

    def test_single_item(self):
        self.assertIsInstance(string_list_to_tuple(["abc"]), tuple)
        self.assertListEqual(string_list_to_tuple(["abc"]), ("abc",))

    def test_multiple_items(self):
        self.assertIsInstance(string_list_to_tuple(["abc", "def", "ghi"]), tuple)
        self.assertListEqual(string_list_to_tuple(["abc", "def", "ghi"]), ("abc", "def", "ghi"))

    def test_mixed_spaces_and_non_spaces(self):
        self.assertIsInstance(string_list_to_tuple(["abc", "  def ", "ghi"]), tuple)
        self.assertListEqual(string_list_to_tuple(["abc", "  def ", "ghi"]), ("abc", "def", "ghi"))

    def test_only_spaces(self):
        self.assertIsInstance(string_list_to_tuple(["   ", "  ", "   "]), tuple)
        self.assertListEqual(string_list_to_tuple(["   ", "  ", "   "]), ())

    def test_none_string_input(self):
        with self.assertRaises(TypeError):
            string_list_to_tuple(123)

    def test_empty_string_input(self):
        with self.assertRaises(ValueError):
            string_list_to_tuple([])
