import unittest
from mbpp_132_code import tup_string

class TestTupString(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(tup_string(("a", "b", "c")), "abc")

    def test_empty_tuple(self):
        self.assertEqual(tup_string(()), "")

    def test_single_element(self):
        self.assertEqual(tup_string(("x",)), "x")

    def test_multiple_elements(self):
        self.assertEqual(tup_string(("1", "2", "3")), "123")

    def test_non_string_elements(self):
        with self.assertRaises(TypeError):
            tup_string((1, 2, 3))

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            tup_string(("a", 1, "b"))

    def test_string_elements_with_spaces(self):
        self.assertEqual(tup_string(("a", "b c", "d e f")), "a b c d e f")

    def test_string_elements_with_newlines(self):
        self.assertEqual(tup_string(("a", "b\nc", "d\ne f")), "a b\nc d\ne f")
