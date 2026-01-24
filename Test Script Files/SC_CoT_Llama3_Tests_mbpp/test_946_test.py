import unittest
from mbpp_946_code import most_common_elem

class TestMostCommonElem(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(most_common_elem('hello world', 2), [('o', 2), (' ', 1)])

    def test_edge_cases(self):
        self.assertEqual(most_common_elem('abc', 0), [])
        self.assertEqual(most_common_elem('abc', 5), [('a', 1), ('b', 1), ('c', 1)])

    def test_edge_case_with_zero(self):
        self.assertEqual(most_common_elem('', 2), [])

    def test_edge_case_with_negative(self):
        with self.assertRaises(ValueError):
            most_common_elem('abc', -1)

    def test_edge_case_with_non_integer(self):
        with self.assertRaises(TypeError):
            most_common_elem('abc', 'a')

    def test_edge_case_with_non_string(self):
        with self.assertRaises(TypeError):
            most_common_elem([1, 2, 3], 2)

    def test_edge_case_with_non_integer_value(self):
        with self.assertRaises(TypeError):
            most_common_elem('abc', {'a': 1})

    def test_edge_case_with_non_string_input(self):
        with self.assertRaises(TypeError):
            most_common_elem([1, 2, 3], 2)
