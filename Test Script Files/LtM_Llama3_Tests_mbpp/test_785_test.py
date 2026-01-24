import unittest
from mbpp_785_code import tuple_str_int

class TestTupleStrInt(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(tuple_str_int("1,2,3"), (1, 2, 3))

    def test_edge_empty_input(self):
        self.assertEqual(tuple_str_int(""), ())

    def test_edge_single_element_input(self):
        self.assertEqual(tuple_str_int("1"), (1,))

    def test_edge_multiple_separators_input(self):
        self.assertEqual(tuple_str_int("1,2,3,4,5"), (1, 2, 3, 4, 5))

    def test_edge_separators_with_spaces_input(self):
        self.assertEqual(tuple_str_int("1, 2, 3, 4, 5"), (1, 2, 3, 4, 5))

    def test_edge_separators_with_newlines_input(self):
        self.assertEqual(tuple_str_int("1,\n2,\n3,\n4,\n5"), (1, 2, 3, 4, 5))

    def test_edge_separators_with_tabs_input(self):
        self.assertEqual(tuple_str_int("1,\t2,\t3,\t4,\t5"), (1, 2, 3, 4, 5))

    def test_edge_separators_with_parentheses_input(self):
        self.assertEqual(tuple_str_int("(1,2,3,4,5)"), (1, 2, 3, 4, 5))

    def test_edge_separators_with_ellipsis_input(self):
        self.assertEqual(tuple_str_int("1,2,3,...,5"), (1, 2, 3, 5))

    def test_edge_separators_with_mixed_input(self):
        self.assertEqual(tuple_str_int("1,2,3,4,5,...,7"), (1, 2, 3, 4, 5, 7))

    def test_invalid_input_non_numeric(self):
        with self.assertRaises(ValueError):
            tuple_str_int("1,2,a,3,4")

    def test_invalid_input_non_separated(self):
        with self.assertRaises(ValueError):
            tuple_str_int("123456")
