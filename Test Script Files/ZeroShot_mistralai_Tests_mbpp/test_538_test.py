import unittest
from mbpp_538_code import string_list_to_tuple

class TestStringListToTuple(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], string_list_to_tuple([]))

    def test_single_element_list(self):
        self.assertListEqual(["a"], string_list_to_tuple(["a"]))

    def test_multiple_elements_list(self):
        self.assertListEqual(["a", "b", "c"], string_list_to_tuple(["a", "b", "c"]))

    def test_mixed_elements_list(self):
        self.assertListEqual(["a", 1, "b", [2, 3], "c"], string_list_to_tuple(["a", 1, "b", [2, 3], "c"]))

    def test_spaces_at_beginning_and_end(self):
        self.assertListEqual(["a", "b", "c"], string_list_to_tuple(["   a   ", "b", "   c   "].split()))

    def test_spaces_in_middle(self):
        self.assertListEqual(["a", "b", "c"], string_list_to_tuple(["a b c".split()]))

    def test_only_spaces_list(self):
        self.assertListEqual([], string_list_to_tuple(["   ".split()]))
