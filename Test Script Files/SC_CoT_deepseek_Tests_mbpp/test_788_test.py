import unittest
from mbpp_788_code import new_tuple

class TestNewTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(new_tuple([1, 2, 3], "test"), (1, 2, 3, "test"))

    def test_empty_list(self):
        self.assertEqual(new_tuple([], "test"), ("test",))

    def test_single_element_list(self):
        self.assertEqual(new_tuple(["a"], "test"), ("a", "test"))

    def test_large_list(self):
        self.assertEqual(new_tuple(list(range(1, 1000)), "test"), tuple(range(1, 1000)) + ("test",))

    def test_string_input(self):
        self.assertEqual(new_tuple("abc", "test"), ("abc", "test"))

    def test_integer_input(self):
        self.assertEqual(new_tuple(123, "test"), (123, "test"))

    def test_float_input(self):
        self.assertEqual(new_tuple(123.45, "test"), (123.45, "test"))

    def test_boolean_input(self):
        self.assertEqual(new_tuple(True, "test"), (True, "test"))

    def test_none_input(self):
        self.assertEqual(new_tuple(None, "test"), (None, "test"))

    def test_empty_string(self):
        self.assertEqual(new_tuple("", "test"), ("", "test"))
