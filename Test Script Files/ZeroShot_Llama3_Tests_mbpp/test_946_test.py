import unittest
from mbpp_946_code import most_common_elem

class TestMostCommonElem(unittest.TestCase):

    def test_most_common_elem(self):
        self.assertEqual(most_common_elem("hello world", 2), [('o', 2), (' ', 1), ('h', 1), ('w', 1), ('r', 1), ('l', 1), ('d', 1)])
        self.assertEqual(most_common_elem("hello world", 3), [('o', 2), (' ', 1), ('h', 1), ('w', 1), ('r', 1), ('l', 1), ('d', 1)])
        self.assertEqual(most_common_elem("hello world", 1), [('o', 2)])
        self.assertEqual(most_common_elem("hello world", 0), [])

    def test_most_common_elem_empty_string(self):
        self.assertEqual(most_common_elem("", 2), [])

    def test_most_common_elem_non_string(self):
        with self.assertRaises(TypeError):
            most_common_elem(123, 2)

    def test_most_common_elem_non_integer(self):
        with self.assertRaises(TypeError):
            most_common_elem("hello world", "a")
