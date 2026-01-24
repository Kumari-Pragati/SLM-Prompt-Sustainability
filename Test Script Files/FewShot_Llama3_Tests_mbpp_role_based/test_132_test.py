import unittest
from mbpp_132_code import tup_string

class TestTupString(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(tup_string(("a", "b", "c")), "abc")

    def test_empty_tuple(self):
        self.assertEqual(tup_string(()), "")

    def test_single_element_tuple(self):
        self.assertEqual(tup_string(("a",)), "a")

    def test_tuple_with_spaces(self):
        self.assertEqual(tup_string(("a", "b", "c", "d")), "abcd")

    def test_tuple_with_punctuation(self):
        self.assertEqual(tup_string(("a", "b", "!")), "ab!")

    def test_tuple_with_newline(self):
        self.assertEqual(tup_string(("a", "b", "\n", "c")), "abc")
