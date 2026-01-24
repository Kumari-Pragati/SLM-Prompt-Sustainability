import unittest
from mbpp_390_code import add_string

class TestAddString(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(add_string([], "{}"), [])

    def test_single_item_list(self):
        self.assertEqual(add_string([1], "{}"), ["1"])

    def test_multiple_items_list(self):
        self.assertEqual(add_string([1, 2, 3], "{}"), ["1", "2", "3"])

    def test_negative_number_list(self):
        self.assertEqual(add_string([-1, -2, -3], "{}"), ["-1", "-2", "-3"])

    def test_string_list(self):
        self.assertEqual(add_string(["a", "b", "c"], "{}"), ["a", "b", "c"])

    def test_list_with_float(self):
        self.assertEqual(add_string([1.5, 2.5, 3.5], "{}"), ["1.5", "2.5", "3.5"])

    def test_list_with_empty_string(self):
        self.assertEqual(add_string([], "{}"), [])

    def test_list_with_none(self):
        self.assertEqual(add_string([None], "{}"), ["None"])

    def test_list_with_mixed_types(self):
        self.assertEqual(add_string([1, "a", None, 3.5], "{}"), ["1", "a", "None", "3.5"])

    def test_string_format_error(self):
        with self.assertRaises(ValueError):
            add_string([1], "{} {}")
