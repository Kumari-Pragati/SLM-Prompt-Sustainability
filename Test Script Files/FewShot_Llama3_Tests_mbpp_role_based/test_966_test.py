import unittest
from mbpp_966_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(remove_empty(()), [])

    def test_tuple_with_empty_strings(self):
        self.assertEqual(remove_empty(("", "", "a", "b", "c")), ["a", "b", "c"])

    def test_tuple_with_empty_strings_and_empty_tuples(self):
        self.assertEqual(remove_empty((("",), ("",), "a", "b", "c")), ["a", "b", "c"])

    def test_tuple_with_empty_strings_and_empty_tuples_and_empty_lists(self):
        self.assertEqual(remove_empty((("",), ("",), "", "a", "b", "c")), ["a", "b", "c"])

    def test_tuple_with_non_empty_elements(self):
        self.assertEqual(remove_empty(("a", "b", "c")), ["a", "b", "c"])

    def test_tuple_with_mixed_elements(self):
        self.assertEqual(remove_empty(("a", "", "b", "c", "", "d")), ["a", "b", "c", "d"])
