import unittest
from mbpp_390_code import add_string

class TestAddString(unittest.TestCase):
    def test_positive_list_and_string(self):
        self.assertEqual(add_string([1, 2, 3], "{}"), ["1", "2", "3"])

    def test_empty_list_and_string(self):
        self.assertEqual(add_string([], "{}"), [])

    def test_list_with_zero_and_string(self):
        self.assertEqual(add_string([0], "{}"), ["0"])

    def test_list_with_negative_and_string(self):
        self.assertEqual(add_string([-1, -2, -3], "{}"), ["-1", "-2", "-3"])

    def test_list_with_float_and_string(self):
        self.assertEqual(add_string([1.1, 2.2, 3.3], "{}"), ["1.1", "2.2", "3.3"])

    def test_list_with_string_and_string(self):
        self.assertEqual(add_string(["Hello", "World"], "{}"), ["Hello", "World"])

    def test_list_with_mixed_types_and_string(self):
        self.assertEqual(add_string([1, "Hello", 2.2], "{}"), ["1", "Hello", "2.2"])

    def test_string_with_empty_list(self):
        self.assertEqual(add_string([""], "{}"), [])

    def test_string_with_none(self):
        self.assertEqual(add_string(None, "{}"), [])

    def test_string_with_empty_string(self):
        self.assertEqual(add_string(["{}"], "{}"), [""])
