import unittest
from mbpp_946_code import most_common_elem

class TestMostCommonElem(unittest.TestCase):
    def test_typical_input(self):
        s = "hello world"
        a = 2
        expected_output = [('o', 2), ('h', 1)]
        self.assertEqual(most_common_elem(s, a), expected_output)

    def test_edge_case_a_zero(self):
        s = "hello world"
        a = 0
        expected_output = []
        self.assertEqual(most_common_elem(s, a), expected_output)

    def test_edge_case_a_one(self):
        s = "hello world"
        a = 1
        expected_output = [('o', 2), ('h', 1)]
        self.assertEqual(most_common_elem(s, a), expected_output)

    def test_invalid_input_non_integer_a(self):
        s = "hello world"
        a = 'a'
        with self.assertRaises(TypeError):
            most_common_elem(s, a)

    def test_invalid_input_non_string_s(self):
        s = 123
        a = 2
        with self.assertRaises(TypeError):
            most_common_elem(s, a)

    def test_edge_case_empty_string(self):
        s = ""
        a = 2
        expected_output = []
        self.assertEqual(most_common_elem(s, a), expected_output)
