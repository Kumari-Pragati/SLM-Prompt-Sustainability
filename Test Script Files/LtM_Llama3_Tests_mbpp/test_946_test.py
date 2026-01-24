import unittest
from mbpp_946_code import most_common_elem

class TestMostCommonElem(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(most_common_elem("hello world", 2), [('o', 2), (' ', 1)])

    def test_empty_string(self):
        self.assertEqual(most_common_elem("", 2), [])

    def test_single_element_string(self):
        self.assertEqual(most_common_elem("a", 2), [('a', 1)])

    def test_edge_case_a_greater_than_length(self):
        self.assertEqual(most_common_elem("hello world", 10), [('o', 2), (' ', 1), ('h', 1), ('w', 1), ('r', 1), ('l', 3), ('d', 1)])

    def test_edge_case_a_equal_to_length(self):
        self.assertEqual(most_common_elem("hello world", 7), [('o', 2), (' ', 1), ('h', 1), ('w', 1), ('r', 1)])

    def test_edge_case_a_less_than_length(self):
        self.assertEqual(most_common_elem("hello world", 1), [('o', 2)])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            most_common_elem(123, 2)

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            most_common_elem("hello world", 'a')
