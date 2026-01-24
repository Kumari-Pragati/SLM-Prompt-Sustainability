import unittest
from mbpp_132_code import tup_string

class TestTupString(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(tup_string(("a", "b", "c")), "abc")

    def test_empty(self):
        self.assertEqual(tup_string(()), "")

    def test_single_element(self):
        self.assertEqual(tup_string(("a",)), "a")

    def test_multiple_elements(self):
        self.assertEqual(tup_string(("a", "b", "c", "d")), "abcd")

    def test_non_string_elements(self):
        self.assertEqual(tup_string(("1", 2, "c", "d")), "123c")

    def test_mixed_case(self):
        self.assertEqual(tup_string(("A", "b", "C", "d")), "AbCd")
