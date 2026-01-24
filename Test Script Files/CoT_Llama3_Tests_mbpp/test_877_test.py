import unittest
from mbpp_877_code import sort_String

class TestSortString(unittest.TestCase):
    def test_sort_string(self):
        self.assertEqual(sort_String("hello"), "ehllo")
        self.assertEqual(sort_String("abc"), "abc")
        self.assertEqual(sort_String("defgh"), "defgh")
        self.assertEqual(sort_String("123"), "123")
        self.assertEqual(sort_String("aabbcc"), "aabbcc")
        self.assertEqual(sort_String(""), "")

    def test_sort_string_edge_cases(self):
        self.assertEqual(sort_String("z"), "z")
        self.assertEqual(sort_String("Z"), "Z")
        self.assertEqual(sort_String("0"), "0")
        self.assertEqual(sort_String("9"), "9")
        self.assertEqual(sort_String("abc123"), "abc123")

    def test_sort_string_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sort_String(None)
        with self.assertRaises(TypeError):
            sort_String(123)
