import unittest
from mbpp_538_code import string_list_to_tuple

class TestStringListToTuple(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(string_list_to_tuple(["hello", "world"]), ("hello", "world"))

    def test_empty_input(self):
        self.assertEqual(string_list_to_tuple([]), ())

    def test_single_input(self):
        self.assertEqual(string_list_to_tuple(["example"]), ("example",))

    def test_all_space_input(self):
        self.assertEqual(string_list_to_tuple(["   "]), ())

    def test_mixed_input(self):
        self.assertEqual(string_list_to_tuple(["hello", " ", "world"]), ("hello", "world"))
