import unittest
from mbpp_7_code import find_char_long

class TestFindCharLong(unittest.TestCase):
    def test_typical_use_case(self):
        text = "This is a typical use case"
        self.assertEqual(find_char_long(text), ['typical', 'use', 'case'])

    def test_edge_case(self):
        text = "a"
        self.assertEqual(find_char_long(text), [])

    def test_boundary_case(self):
        text = "This is a boundary case"
        self.assertEqual(find_char_long(text), ['boundary', 'case'])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_char_long(123)
