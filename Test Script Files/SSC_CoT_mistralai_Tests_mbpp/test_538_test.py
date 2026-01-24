import unittest
from mbpp_538_code import string_list_to_tuple

class TestStringListToTuple(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(string_list_to_tuple(["hello", "world", " ", " "]), ("hello", "world"))

    def test_empty_input(self):
        self.assertEqual(string_list_to_tuple([]), ())

    def test_single_input(self):
        self.assertEqual(string_list_to_tuple(["test"]), ("test",))

    def test_edge_cases(self):
        self.assertEqual(string_list_to_tuple(["\thello\t"]), ("hello",))
        self.assertEqual(string_list_to_tuple(["\nhello\n"]), ("hello",))
        self.assertEqual(string_list_to_tuple(["hello\r"]), ("hello",))

    def test_invalid_input(self):
        self.assertRaises(TypeError, string_list_to_tuple, 123)
        self.assertRaises(TypeError, string_list_to_tuple, ["hello", 123])
